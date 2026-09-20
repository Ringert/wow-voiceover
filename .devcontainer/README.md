# Python development container

Open this repository in VS Code and run **Dev Containers: Reopen in Container**.
Docker Desktop must be running with Linux containers (on Windows: WSL2 backend).
The first build downloads the Python packages and Chromium and can take several minutes.

The image provides Python 3.10, the repository's `requirements.txt`,
FFmpeg/ffprobe, a MySQL client, build tools and
Playwright Chromium. The writable environment is `/opt/venv`; no activation is
needed. Python, Pylance and debugger extensions are declared for VS Code.

```bash
python -m pip check
python cli-main.py --help
```

After changing `requirements.txt`, run **Dev Containers: Rebuild Container**.
Temporary packages installed with `python -m pip install ...` survive a restart,
but rebuilding the image recreates the environment from the Dockerfile.

## Codex and GitHub

The Codex VS Code extension (`openai.chatgpt`) is installed when VS Code opens
the container. The GitHub CLI (`gh`) is installed system-wide in the image.
Authenticate inside the container as needed:

```bash
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
gh auth status
```

Sign in to Codex through its VS Code extension. Port 1455 is forwarded for the
login callback. Extension visibility and the actual login flows must be checked
in the reopened VS Code window.

The project-specific `wow-voiceover-home-${devcontainerId}` Docker volume persists
all of `/home/vscode`, including `CODEX_HOME=/home/vscode/.codex`,
`GH_CONFIG_DIR=/home/vscode/.config/gh`, and both VS Code extension files and
installation markers in `.vscode-server`. This keeps these files together across
container rebuilds. Deleting the volume deletes this state; a different checkout
location can result in a different devcontainer ID and a fresh volume.
The workspace has a stable path, `/workspaces/wow-voiceover`, registered as a
trusted Git directory at system level to handle differing bind-mount ownership.

No personal state or credentials are copied from the Website project or host.
The Website template's Signal bridge and Docker-in-Docker feature are separate
from these fixes and are not included. Consequently its feature lockfile is not
applicable here. The standalone Codex CLI is not installed by this configuration.

Codex state directory reference:
https://developers.openai.com/de-DE/docs/config-file/environment-variables

## Services are separate

This checkout contains the CLI and WoW addon. The voice-cloning service lives in
the separate `lib-tts` repository. Its model-specific dependencies and model
weights belong exclusively to that service. This project only sends HTTP
requests and downloads generated audio; it needs no local model runtime or GPU.
After upgrading from the previous image, run **Dev Containers: Rebuild Container**
to remove the previously installed model runtime from the development environment.

Opening the container does not start services, download models, import a database,
or run audio generation. Start the existing MySQL Compose project explicitly
from a **host terminal** with `docker compose up -d`. Docker is not required
inside this development container.

Configure the TTS service through `TTS_PROTOCOL`, `TTS_HOST` and `TTS_PORT`
in the repository-root `.env`. For a service published on Docker Desktop's host
port 8000, use `http`, `host.docker.internal` and `8000`. Check its availability
with `curl --fail http://host.docker.internal:8000/health`.
MySQL remains hardcoded at `0.0.0.0:3306`; its `.env` values are currently ignored.
A healthy TTS service alone does not verify the database or full generation flow.

Only login callback port 1455 is automatically forwarded. For a future webservice
running inside this container, bind it to `0.0.0.0` and explicitly forward its
port through VS Code's **Ports** panel.
