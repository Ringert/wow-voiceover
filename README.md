# VoiceOver for World of Warcraft

## v2: https://allvoice.ai
Contribute voices on [allvoice.ai](https://allvoice.ai) so I can give each NPC a unique AI voicemodel to power their dialog. The top rated voice for each NPC will be used. 


### [voiceover discord](https://discord.gg/VdhUmA8ZCt)
### [allvoice code](https://github.com/allvoice/allvoice-website)

## Overview
- TTS CLI tool to create audio files for quests and gossip text
- In-game addon for playing generated voiceovers
- CLI uses data fetched from a local MySQL database
- TTS generation via [lib-tts](https://github.com/Ringert/lib-tts) webservice

## Project wiki and Codex workflow

The [project wiki](wiki/index.md) documents this fork's current implementation,
setup and known limitations. Start with the [overview](wiki/overview.md),
[development guide](wiki/project/local-development.md),
[user manual](wiki/project/user-manual.md) and
[GitHub workflow](wiki/project/github-workflow.md).
[AGENTS.md](AGENTS.md) defines the shared standards and seven Codex roles adopted
from [Codex-Projektvorlage](https://github.com/Ringert/Codex-Projektvorlage).

The wiki records corrections to the older setup guide below: MySQL settings in
`.env` are currently ignored, TTS uses a configurable address and a fixed German payload,
and `gen_lookup_tables` creates lookup tables rather than synthesizing audio.

## Below is for developers only
Go to [releases](https://github.com/mrthinger/wow-voiceover/releases) if you're looking to install the addon.

---

## Setup Guide for New Developers

### VS Code Dev Container

For a preconfigured Python 3.10 environment with project dependencies, PyTorch,
TorchAudio, FFmpeg and Playwright Chromium, use **Dev Containers: Reopen in Container**.
See [.devcontainer/README.md](.devcontainer/README.md) for verification commands,
optional GPU configuration and the separate database/TTS service setup.

This guide will walk you through setting up the complete development environment for wow-voiceover generation.

### Prerequisites

- **OS**: Linux (recommended) or WSL2 on Windows
- **Docker** & **Docker Compose** (for MySQL database)
- **Python**: 3.10.x (via pyenv recommended)
- **ffmpeg**: For audio processing
- **Git**: For cloning repositories

### Step 1: Install System Dependencies

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install -y build-essential ffmpeg git curl docker.io docker-compose
```

#### Fedora/RHEL
```bash
sudo dnf install -y @development-tools ffmpeg git curl docker docker-compose
```

### Step 2: Install pyenv (Python Version Manager)

```bash
curl https://pyenv.run | bash

# Add to your shell configuration (~/.bashrc or ~/.zshrc)
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Reload shell configuration
source ~/.bashrc
```

### Step 3: Install Python 3.10

```bash
pyenv install 3.10.15
pyenv global 3.10.15
python --version  # Should show Python 3.10.15
```

### Step 4: Clone and Setup wow-voiceover

```bash
# Clone the repository
git clone https://github.com/mrthinger/wow-voiceover.git
cd wow-voiceover

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Setup MySQL Database

```bash
# Copy environment configuration
cp .env.example .env

# Edit .env for TTS; MySQL settings are currently hard-coded in tts_cli/env_vars.py
# nano .env

# Start MySQL container
docker compose up -d

# Wait a few seconds for MySQL to initialize, then seed the database
python cli-main.py init-db
```

This will download and import the World of Warcraft database dump.

### Step 6: Setup TTS Webservice

The TTS generation is handled by a separate webservice. You need to set it up:

```bash
# Clone the TTS service repository
cd ..
git clone https://github.com/Ringert/lib-tts.git
cd lib-tts

# Follow the setup instructions in lib-tts README
# This typically involves:
# 1. Creating a Python virtual environment
# 2. Installing dependencies
# 3. Setting up voice samples
# 4. Starting the webservice on port 8000
```

**Important**: The TTS webservice must be reachable at the address configured in `.env` (default: `http://localhost:8000`) before you can generate audio files.

Refer to [lib-tts documentation](https://github.com/Ringert/lib-tts) for detailed setup instructions.

### Step 7: Create Voice Clone Map

The voice clone map defines which voice sample to use for each NPC:

```bash
cd ~/wow-voiceover  # Return to wow-voiceover directory
source .venv/bin/activate

python cli-main.py create_voice_clone_map
```

This creates/updates `voice-clone-map.json` with voice assignments.

### Step 8: Generate Audio Files

Now you can generate voiceover audio files:

```bash
# Generate German audio (requires MySQL, voice map and lib-tts)
python cli-main.py --lang deDE interactive

# Then update lookup tables and measured audio durations
python cli-main.py --lang deDE gen_lookup_tables
```

The generated audio files will be saved in:
- `AI_VoiceOverData_Vanilla/generated/sounds/quests/`
- `AI_VoiceOverData_Vanilla/generated/sounds/gossip/`

### Step 9: Install Addon to WoW

Copy the generated files to your WoW addon directory:

```bash
export WOW_DIR="/path/to/your/World of Warcraft"

# Copy or symlink the addon folders
cp -r AI_VoiceOver "$WOW_DIR/_classic_era_/Interface/AddOns/"
cp -r AI_VoiceOverData_Vanilla "$WOW_DIR/_classic_era_/Interface/AddOns/"

# Or use symlinks for faster development:
ln -s "$(pwd)/AI_VoiceOver" "$WOW_DIR/_classic_era_/Interface/AddOns/"
ln -s "$(pwd)/AI_VoiceOverData_Vanilla" "$WOW_DIR/_classic_era_/Interface/AddOns/"
```

---

## Daily Development Workflow

### Starting Your Session

```bash
cd ~/wow-voiceover
source .venv/bin/activate
```

Make sure the TTS webservice is running:
```bash
# In a separate terminal
cd ~/lib-tts
source .venv/bin/activate  # Or whatever venv you used for lib-tts
python main.py  # Or whatever command starts the service
```

### Common Commands

```bash
# Interactive mode
python cli-main.py interactive

# Generate lookup tables for a specific language
python cli-main.py --lang deDE gen_lookup_tables

# Regenerate audio for a specific quest
python cli-main.py regenerate quest 70-accept

# Regenerate audio for specific gossip
python cli-main.py regenerate gossip a63f0a77a472eab18caf48ea8320d27e

# Regenerate all audio for an NPC
python cli-main.py regenerate_for_npc "Tirion Fordring"

# Regenerate audio by text search
python cli-main.py regenerate_by_text "Abenteurer"

# Regenerate audio for a specific race/gender
python cli-main.py regenerate_by_race 1 0  # Human Male

# Switch voice clone for NPCs
python cli-main.py switch_voice quests/70-accept gossip/abc123

# Extract model data
python cli-main.py extract_model_data
```

---

## Supported Languages

| Language Code | Language |
| ------------- | ------- |
| enUS          | English (US) |
| enGB          | English (GB) |
| koKR          | Korean |
| frFR          | French |
| deDE          | German |
| zhCN          | Simplified Chinese |
| zhTW          | Traditional Chinese |
| esES          | European Spanish |
| esMX          | Mexican Spanish |
| ruRU          | Russian |

---

## TTS Webservice Configuration

Configure the TTS service in `.env` at the repository root:

```dotenv
TTS_PROTOCOL=http
TTS_HOST=localhost
TTS_PORT=8000
```

Use `http` or `https` for the protocol, and a hostname or IP address without a
protocol, port or path for `TTS_HOST`. Both synthesis and audio downloads use
these settings. Missing settings default to `http://localhost:8000`; existing
environment variables take precedence over `.env`. Restart the CLI after edits.
The file is loaded from the repository root regardless of the working directory.
`.env` stays local and ignored by Git; `.env.example` provides the template.

### API Endpoints Used

**POST** `/api/v1/synthesize`
- Generates audio from text
- Request body:
  ```json
  {
    "text": "Your text here",
    "voice_id": "quests/70-accept",
    "language": "german"
  }
  ```
- Response:
  ```json
  {
    "file_id": "uuid",
    "file_path": "/sounds/uuid.mp3",
    "duration": 31.3975,
    "created_at": "2026-01-27T18:53:42.504275"
  }
  ```

**GET** `/api/v1/{file_path}`
- Downloads the generated audio file

---

## Project Structure

```
wow-voiceover/
├── AI_VoiceOver/              # In-game addon code
├── AI_VoiceOverData_Vanilla/  # Generated audio files and lookup tables
├── tts_cli/                   # TTS generation CLI tools
│   ├── tts_cloning.py        # Main TTS processing logic
│   ├── sql_queries.py        # Database queries
│   ├── utils.py              # Helper functions
│   └── ...
├── cli-main.py               # Main CLI entry point
├── requirements.txt          # Python dependencies
├── docker-compose.yml        # MySQL database setup
└── voice-clone-map.json      # Voice assignments per NPC
```

---

## Troubleshooting

### TTS Webservice Connection Error

If you see errors like `Connection refused` or `unable to generate audio via webservice`:
1. Ensure lib-tts is reachable at the address configured in `.env` (default: `http://localhost:8000`)
2. Test the configured address, e.g. `curl http://localhost:8000/health` with the defaults (if available)
3. Check lib-tts logs for errors

### Database Connection Issues

```bash
# Check if MySQL container is running
docker ps

# View MySQL logs
docker compose logs mysql

# Restart MySQL container
docker compose restart mysql
```

### Python Virtual Environment Issues

```bash
# Deactivate and recreate venv
deactivate
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Audio Generation Fails

1. Check that voice samples exist in lib-tts
2. Verify voice-clone-map.json has correct voice_id references
3. Check lib-tts logs for errors during synthesis

---

## Contributing

If you want to contribute to this project, please feel free to open an issue or submit a pull request.

---

## CLI Reference

### Dataframe Schema

The dataframe schema before calling `preprocess_dataframe` consists of:

| Column        | Description                                                  |
|---------------|--------------------------------------------------------------|
| `source`      | Interaction type: 'accept', 'progress', 'complete', 'gossip' |
| `quest`       | Quest ID or empty string if gossip interaction    |
| `text`        | Text template content of the interaction                           |
| `DisplayRaceID` | Race ID of the NPC          |
| `DisplaySexID`  | Gender ID of the NPC        |
| `name`        | NPC name               |
| `type`        | NPC type: 'creature', 'gameobject', or 'item' |
| `id`          | Creature/gameobject/item ID |

`DisplayRaceID = -1` is used for inanimate NPCs (gameobjects, items). It's mapped to "narrator" voice.

### Fields Added by `preprocess_dataframe`

| Column                   | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| `race`                   | NPC race, mapped from `DisplayRaceID` via `RACE_DICT` |
| `gender`                 | NPC gender, mapped from `DisplaySexID` via `GENDER_DICT` |
| `voice_name`             | Voice name: combination of race + gender |
| `templateText_race_gender` | Combination of text, race, and gender          |
| `templateText_race_gender_hash` | Hash of templateText_race_gender          |
| `cleanedText` | Rendered template text |
| `player_gender` | Player character gender (if applicable) |
| esES          | European Spanish |
| esMX          | Mexican Spanish |
| ruRU          | Russian |

## Output
The generated TTS audio files will be saved in the sounds folder, with separate subfolders for quests and gossip. Lookup tables and sound length tables will also be generated for use in the addon. 

## Addon Install
Copy over the `generated` folder to the VoiceOverData_Vanilla folder, then the VoiceOver and VoiceOverData_Vanilla folder to `World of Warcraft/_classic_era_/Interface/AddOns`. Alternatively, you can syslink instead of copying for faster development.
Example syslink:
```bash
export WOW_DIR=PATH_OF_YOUR_WOW_DIR
ln -s ./VoiceOver "$WOW_DIR/_classic_era_/Interface/AddOns"
ln -s ./VoiceOver_Vanilla "$WOW_DIR/_classic_era_/Interface/AddOns"
```
## Contributing
If you want to contribute to this project, please feel free to open an issue or submit a pull request.

# CLI Docs

## Dataframe Schema

The dataframe schema before calling the `preprocess_dataframe` function consists of the following columns:

| Column        | Description                                                  |
|---------------|--------------------------------------------------------------|
| `source`      | Indicates the type of interaction, can be 'accept', 'progress', 'complete', or 'gossip' |
| `quest`       | The quest ID or empty string if it's a gossip interaction    |
| `text`        | The text template content of the interaction                           |
| `DisplayRaceID` | The race ID of the NPC involved in the interaction          |
| `DisplaySexID`  | The gender ID of the NPC involved in the interaction        |
| `name`        | The name of the NPC involved in the interaction               |
| `type`        | The type of the NPC involved in the interaction ('creature', 'gameobject', or 'item') |
| `id`          | The creature/gameobject/item ID of the NPC involved in the interaction |

`DisplayRaceID = -1` is used for interactions with inanimate NPCs: gameobjects, items etc. It's mapped to a voice called "narrator" in `RACE_DICT`.

## New Fields Added by `preprocess_dataframe`

The `preprocess_dataframe` function adds the following new fields to the dataframe:

| Column                   | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| `race`                   | The race of the NPC, mapped from `DisplayRaceID` using `RACE_DICT` |
| `gender`                 | The gender of the NPC, mapped from `DisplaySexID` using `GENDER_DICT` |
| `voice_name`             | The voice name, which is a combination of the race and gender fields |
| `templateText_race_gender` | A combination of the text, race, and gender fields          |
| `templateText_race_gender_hash` | A hash of the `templateText_race_gender` field          |
| `cleanedText` | `text` after rendering template |
