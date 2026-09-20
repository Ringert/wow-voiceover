FROM mcr.microsoft.com/devcontainers/python:1-3.10-bookworm

ENV VIRTUAL_ENV=/opt/venv \
    PATH=/opt/venv/bin:${PATH} \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PLAYWRIGHT_BROWSERS_PATH=/opt/playwright

# The base image includes a Yarn feed, unused by this Python project, whose
# signing key can expire independently of Debian's package sources.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential ffmpeg default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/wow-voiceover-requirements.txt
RUN python -m venv /opt/venv \
    && /opt/venv/bin/python -m pip install --no-cache-dir -r /tmp/wow-voiceover-requirements.txt \
    && /opt/venv/bin/python -m pip check \
    && /opt/venv/bin/python -m playwright install --with-deps chromium \
    && chmod -R a+rX /opt/playwright \
    && chown -R vscode:vscode /opt/venv \
    && rm -rf /var/lib/apt/lists/* /tmp/wow-voiceover-requirements.txt

# Keep tooling and workspace trust independent of the persistent user home.
RUN apt-get update \
    && apt-get install -y --no-install-recommends gh \
    && rm -rf /var/lib/apt/lists/* \
    && git config --system --add safe.directory /workspaces/wow-voiceover \
    && mkdir -p /home/vscode/.codex /home/vscode/.config/gh \
       /home/vscode/.vscode-server/extensions /home/vscode/.vscode-server/data \
    && chown -R vscode:vscode /home/vscode/.codex /home/vscode/.config \
       /home/vscode/.vscode-server
