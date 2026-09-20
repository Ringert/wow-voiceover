# Python development container

Open this repository in VS Code and run **Dev Containers: Reopen in Container**.
Docker Desktop must be running with Linux containers (on Windows: WSL2 backend).
The first build downloads the Python packages and Chromium and can take several minutes.

The image provides Python 3.10, the repository's `requirements.txt`, PyTorch and
TorchAudio 2.6.0 (CPU), FFmpeg/ffprobe, libsndfile, a MySQL client, build tools and
Playwright Chromium. The writable environment is `/opt/venv`; no activation is
needed. Python, Pylance and debugger extensions are declared for VS Code.

```bash
python -m pip check
python cli-main.py --help
python -c "import torch, torchaudio; print(torch.__version__); print('CUDA:', torch.cuda.is_available())"
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
weights are not installed here. PyTorch is provided as a development baseline;
compatibility with a particular cloning model still needs to be established.

Opening the container does not start services, download models, import a database,
or run audio generation. Start the existing MySQL Compose project explicitly
from a **host terminal** with `docker compose up -d`. Docker is not required
inside this development container.

The current application code hardcodes MySQL at `0.0.0.0:3306` and the TTS service
at `localhost:8000`; these addresses refer to the development container itself.
The code also currently ignores the MySQL values in `.env`. Before using services
on the Docker Desktop host, those application settings must be made configurable
and pointed to `host.docker.internal`. This container setup alone does not make
the existing end-to-end generation flow operational.

Only login callback port 1455 is automatically forwarded. For a future webservice
running inside this container, bind it to `0.0.0.0` and explicitly forward its
port through VS Code's **Ports** panel.

## Optional NVIDIA GPU

The default configuration also opens on machines without NVIDIA hardware.
For an NVIDIA host with working Docker GPU passthrough, change the build argument
`TORCH_INDEX_URL` in `devcontainer.json` to
`https://download.pytorch.org/whl/cu124`, add the top-level property
`"runArgs": ["--gpus=all"]`, and rebuild. Verify `torch.cuda.is_available()`
inside the rebuilt container. GPU operation has not been assumed or verified.
Newer GPUs may need a newer matching Torch/TorchAudio and CUDA combination.

Version combinations: https://docs.pytorch.org/get-started/previous-versions/
