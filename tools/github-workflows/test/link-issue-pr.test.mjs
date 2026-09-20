import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';

// Execute the shipped github-script body with a controlled GitHub boundary.
const workflow = readFileSync(
  new URL('../../../.github/workflows/link-issue-pr.yml', import.meta.url), 'utf8',
);
const script = workflow.split('          script: |\n')[1]
  .split('\n').map((line) => line.replace(/^ {12}/, '')).join('\n');
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const execute = new AsyncFunction('github', 'context', 'core', 'process', 'setTimeout', script);

function fixture() {
  return {
    repository: {
      defaultBranchRef: { name: 'master' },
      issue: {
        milestone: { title: 'Release 1' },
        parent: { number: 7, milestone: { title: 'Release 1' }, parent: null },
        closedByPullRequestsReferences: { nodes: [{ number: 23 }] },
      },
      pullRequest: { headRefName: 'issue/WOWVO-11', baseRefName: 'master' },
    },
  };
}

async function run({ body = 'Closes #11\nRefs #7', branch = 'issue/WOWVO-11',
  projectKey = 'WOWVO', state = fixture(), states } = {}) {
  const failures = [];
  const messages = [];
  const requests = [];
  const delays = [];
  const context = {
    repo: { owner: 'example', repo: 'product' },
    payload: { pull_request: { number: 23, head: { ref: branch }, body } },
  };
  await execute({
    graphql: async (query, variables) => {
      requests.push({ query, variables });
      return states?.[Math.min(requests.length - 1, states.length - 1)] ?? state;
    },
  }, context, {
    setFailed: (message) => failures.push(message),
    info: (message) => messages.push(message),
  }, { env: { PROJECT_KEY: projectKey } }, (callback, delay) => {
    delays.push(delay);
    callback();
  });
  return { failures, messages, requests, delays };
}

test('a complete Story PR needs no technical child issues or follow-up documentation PR', async () => {
  const result = await run({ body: 'Closes #11\nRefs #7\n\nCode, tests, architecture and user manual updated.' });
  assert.deepEqual(result.failures, []);
  assert.equal(result.messages.length, 1);
  assert.equal(result.requests.length, 1);
  assert.deepEqual(result.requests[0].variables,
    { owner: 'example', repo: 'product', issue: 11, pr: 23 });
});

for (const [name, options, expected] of [
  ['wrong Story', { body: 'Closes #12\nRefs #7' }, /close exactly its Story/],
  ['two closed Stories', { body: 'Closes #11\nCloses #12\nRefs #7' }, /close exactly its Story/],
  ['additional cross-repository closure', { body: 'Closes #11\nFixes elsewhere/app#12\nRefs #7' }, /close exactly its Story/],
  ['additional URL closure', { body: 'Closes #11\nResolves https://github.com/elsewhere/app/issues/12\nRefs #7' }, /close exactly its Story/],
  ['missing Epic', { body: 'Closes #11' }, /exactly one parent Epic/],
  ['duplicate Epic', { body: 'Closes #11\nRefs #7\nRefs #7' }, /exactly one parent Epic/],
  ['wrong Epic', { body: 'Closes #11\nRefs #8' }, /parent Epic #7/],
  ['legacy technical task references', { body: 'Closes #11\nRefs #7\nImplements #15' }, /remove Implements\/Documents/],
  ['legacy documentation references', { body: 'Closes #11\nRefs #7\nDocuments #22' }, /remove Implements\/Documents/],
  ['separate documentation branch', { branch: 'docs/update-manual', body: 'Documents #22' }, /Invalid Story branch/],
  ['wrong project branch', { branch: 'issue/OTHER-11' }, /Unsupported Story branch/],
  ['unsafe Story number', { branch: 'issue/WOWVO-9007199254740992' }, /Unsupported Story branch/],
  ['invalid project key', { projectKey: 'invalid-key' }, /PROJECT_KEY must/],
]) {
  test(name+' is rejected', async () => {
    const result = await run(options);
    assert.equal(result.failures.length, 1);
    assert.match(result.failures[0], expected);
    assert.deepEqual(result.messages, []);
  });
}

for (const [name, change, expected] of [
  ['missing issue', (s) => { s.repository.issue = null; }, /no longer exists/],
  ['missing default branch', (s) => { s.repository.defaultBranchRef = null; }, /existing default branch/],
  ['missing milestone', (s) => { s.repository.issue.milestone = null; }, /same milestone/],
  ['different Epic milestone', (s) => { s.repository.issue.parent.milestone.title = 'Release 2'; }, /same milestone/],
  ['non-direct Epic parent', (s) => { s.repository.issue.parent.parent = { number: 1 }; }, /direct Story child/],
  ['second linked PR', (s) => { s.repository.issue.closedByPullRequestsReferences.nodes.push({ number: 24 }); }, /already linked to PR #24/],
  ['changed source branch', (s) => { s.repository.pullRequest.headRefName = 'issue/WOWVO-12'; }, /must merge/],
  ['wrong target branch', (s) => { s.repository.pullRequest.baseRefName = 'develop'; }, /into master/],
]) {
  test(name+' remains protected', async () => {
    const state = fixture();
    change(state);
    const result = await run({ state });
    assert.equal(result.failures.length, 1);
    assert.match(result.failures[0], expected);
    assert.deepEqual(result.messages, []);
  });
}

test('native link propagation can finish during bounded retries', async () => {
  const unlinked = fixture();
  unlinked.repository.issue.closedByPullRequestsReferences.nodes = [];
  const result = await run({ states: [unlinked, fixture()] });
  assert.deepEqual(result.failures, []);
  assert.equal(result.requests.length, 2);
  assert.equal(result.messages.length, 1);
});

test('missing native linkage eventually fails rather than treating PR text as proof', async () => {
  const state = fixture();
  state.repository.issue.closedByPullRequestsReferences.nodes = [];
  const result = await run({ state });
  assert.equal(result.requests.length, 6);
  assert.equal(result.failures.length, 1);
  assert.match(result.failures[0], /not natively linked/);
  assert.deepEqual(result.messages, []);
});

for (const defaultBranch of ['master', 'main', 'develop']) {
  test('a linked Story PR can target the actual default branch '+defaultBranch, async () => {
    const state = fixture();
    state.repository.defaultBranchRef.name = defaultBranch;
    state.repository.pullRequest.baseRefName = defaultBranch;
    const result = await run({ state });
    assert.deepEqual(result.failures, []);
    assert.match(result.messages[0], new RegExp('targets '+defaultBranch));
  });
}

test('an explicit project key is used consistently', async () => {
  const state = fixture();
  state.repository.pullRequest.headRefName = 'issue/CUSTOM-11';
  const result = await run({ state, branch: 'issue/CUSTOM-11', projectKey: 'CUSTOM' });
  assert.deepEqual(result.failures, []);
  assert.equal(result.messages.length, 1);
});
