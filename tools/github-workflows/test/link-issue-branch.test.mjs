import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';

// Run the shipped workflow at a controlled GitHub API boundary; no live writes.
const workflow = readFileSync(
  new URL('../../../.github/workflows/link-issue-branch.yml', import.meta.url), 'utf8',
);
const script = workflow.split('          script: |\n')[1]
  .split('\n').map((line) => line.replace(/^ {12}/, '')).join('\n');
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const execute = new AsyncFunction('github', 'context', 'core', 'process', 'setTimeout', script);

function fixture() {
  return {
    repository: {
      id: 'repository-1',
      defaultBranchRef: { name: 'master', target: { oid: 'base-sha' } },
      branch: null,
      issue: {
        id: 'story-11', state: 'OPEN', milestone: { title: 'Release 1' },
        parent: { number: 7, milestone: { title: 'Release 1' }, parent: null },
        labels: { nodes: [{ name: 'implementation-ready' }] },
        linkedBranches: { nodes: [] },
        closedByPullRequestsReferences: { nodes: [] },
      },
    },
  };
}

async function run({ state = fixture(), issueNumber = 11, projectKey = 'WOWVO',
  eventName = 'issues', propagate = true, wrongMutation = false } = {}) {
  const failures = [];
  const messages = [];
  const writes = [];
  const queries = [];
  const delays = [];
  const branch = `issue/${projectKey}-${issueNumber}`;
  const context = {
    eventName, repo: { owner: 'example', repo: 'product' },
    payload: { issue: { number: issueNumber }, inputs: { issue_number: String(issueNumber) } },
  };
  await execute({
    graphql: async (query, variables) => {
      if (query.includes('mutation(')) {
        writes.push(variables);
        if (propagate) {
          state.repository.branch = { target: { oid: 'base-sha' } };
          state.repository.issue.linkedBranches.nodes = [{ ref: { name: branch } }];
        }
        return { createLinkedBranch: { linkedBranch: {
          ref: { name: branch, target: { oid: wrongMutation ? 'wrong-sha' : 'base-sha' } },
        } } };
      }
      queries.push(variables);
      return state;
    },
  }, context, {
    setFailed: (message) => failures.push(message),
    info: (message) => messages.push(message),
  }, { env: { PROJECT_KEY: projectKey } }, (callback, delay) => {
    delays.push(delay);
    callback();
  });
  return { failures, messages, writes, queries, delays };
}

for (const defaultBranch of ['master', 'main', 'develop']) {
  test('create a linked branch from the actual default branch '+defaultBranch, async () => {
    const state = fixture();
    state.repository.defaultBranchRef.name = defaultBranch;
    const result = await run({ state });
    assert.deepEqual(result.failures, []);
    assert.deepEqual(result.writes, [{
      issueId: 'story-11', oid: 'base-sha', name: 'issue/WOWVO-11', repositoryId: 'repository-1',
    }]);
    assert.equal(result.queries.length, 2);
    assert.match(result.messages[0], new RegExp('from '+defaultBranch));
  });
}

test('manual dispatch uses its Story number and the configured project key', async () => {
  const result = await run({ eventName: 'workflow_dispatch', issueNumber: 42, projectKey: 'CUSTOM' });
  assert.deepEqual(result.failures, []);
  assert.equal(result.queries[0].number, 42);
  assert.equal(result.writes[0].name, 'issue/CUSTOM-42');
});

for (const [name, change, expected] of [
  ['missing default branch', (s) => { s.repository.defaultBranchRef = null; }, /existing default branch/],
  ['missing base commit', (s) => { s.repository.defaultBranchRef.target = null; }, /existing default branch/],
  ['missing Story', (s) => { s.repository.issue = null; }, /does not exist/],
  ['closed Story', (s) => { s.repository.issue.state = 'CLOSED'; }, /not open/],
  ['removed readiness', (s) => { s.repository.issue.labels.nodes = []; }, /no longer implementation-ready/],
  ['missing Epic', (s) => { s.repository.issue.parent = null; }, /directly below an epic/],
  ['different milestone', (s) => { s.repository.issue.parent.milestone.title = 'Other'; }, /same milestone/],
  ['nested parent', (s) => { s.repository.issue.parent.parent = { number: 1 }; }, /directly below an epic/],
  ['unlinked existing branch', (s) => { s.repository.branch = { target: { oid: 'other-sha' } }; }, /already exists without/],
  ['another linked branch', (s) => { s.repository.issue.linkedBranches.nodes = [{ ref: { name: 'another' } }]; }, /another linked branch/],
  ['another linked PR', (s) => { s.repository.issue.closedByPullRequestsReferences.nodes = [{ headRefName: 'another' }]; }, /another linked branch or pull request/],
]) {
  test(name+' cannot create a branch', async () => {
    const state = fixture();
    change(state);
    const result = await run({ state });
    assert.equal(result.failures.length, 1);
    assert.match(result.failures[0], expected);
    assert.deepEqual(result.writes, []);
  });
}

test('reconciliation preserves an already linked branch without another write', async () => {
  const state = fixture();
  state.repository.branch = { target: { oid: 'newer-sha' } };
  state.repository.issue.linkedBranches.nodes = [{ ref: { name: 'issue/WOWVO-11' } }];
  const result = await run({ state });
  assert.deepEqual(result.failures, []);
  assert.deepEqual(result.writes, []);
  assert.match(result.messages[0], /already has/);
});

test('invalid project key is rejected before calling GitHub', async () => {
  const result = await run({ projectKey: 'invalid-key' });
  assert.match(result.failures[0], /PROJECT_KEY must/);
  assert.deepEqual(result.queries, []);
  assert.deepEqual(result.writes, []);
});

test('invalid Story number is rejected before calling GitHub', async () => {
  const result = await run({ issueNumber: 0 });
  assert.match(result.failures[0], /valid issue number/);
  assert.deepEqual(result.queries, []);
  assert.deepEqual(result.writes, []);
});

test('a mutation that reports a different base commit fails verification', async () => {
  const result = await run({ wrongMutation: true });
  assert.equal(result.failures.length, 1);
  assert.match(result.failures[0], /did not create/);
  assert.deepEqual(result.messages, []);
});

test('missing native link propagation fails after bounded verification', async () => {
  const result = await run({ propagate: false });
  assert.equal(result.writes.length, 1);
  assert.equal(result.queries.length, 7);
  assert.equal(result.failures.length, 1);
  assert.match(result.failures[0], /Postcondition failed/);
  assert.deepEqual(result.messages, []);
});
