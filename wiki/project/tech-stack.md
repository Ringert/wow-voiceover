---
type: "Project Context"
title: "Projekt-Tech-Stack"
description: "Sprachen, Laufzeiten, Bibliotheken und getrennte Entwicklungs- und Produktwerkzeuge."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: requirements
    resource: "../../requirements.txt"
  - id: container
    resource: "../../.devcontainer/Dockerfile"
  - id: compose
    resource: "../../docker-compose.yml"
  - id: toc
    resource: "../../AI_VoiceOver/addon.xml"
  - id: version
    resource: "../../.python-version"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Projekt-Tech-Stack

| Bereich | Tatsächlicher Bestand | Maßgebliche Datei |
| --- | --- | --- |
| CLI | Python 3.10; `argparse`, Pandas, PyMySQL, Requests | [cli-main.py](../../cli-main.py), [requirements.txt](../../requirements.txt) |
| Datenbank | MySQL 8, VMaNGOS-Tabellen und exportierte Display-Metadaten | [docker-compose.yml](../../docker-compose.yml), [init_db.py](../../tts_cli/init_db.py) |
| Audio | MP3-Ausgabe, FFmpeg/ffprobe, pydub und mutagen | [tts_cloning.py](../../tts_cli/tts_cloning.py), [length_table.py](../../tts_cli/length_table.py) |
| TTS | HTTP-Client für einen getrennten `lib-tts`-Dienst; kein Server in diesem Repository | [tts_cloning.py](../../tts_cli/tts_cloning.py) |
| Addon | WoW-Lua/XML/TOC, Ace3, LibStub, LibDataBroker und weitere eingebundene Bibliotheken | [addon.xml](../../AI_VoiceOver/addon.xml), [embeds.xml](../../AI_VoiceOver/embeds.xml) |
| Clientvarianten | TOCs für 1.12, 2.4.3, 3.3.5, Vanilla, TBC, Wrath und Mainline; Bibliotheksvarianten für Legacy-Clients | [AI_VoiceOver](../../AI_VoiceOver/) |
| Datenmodul | Lua-Lookups, Dauerntabelle und MP3-Dateien | [Datenmodul-TOC](../../AI_VoiceOverData_Vanilla/AI_VoiceOverData_Vanilla.toc) |
| Arbeitscontainer | Python-3.10-Bookworm-Basis, `/opt/venv`, PyTorch/TorchAudio 2.6.0 CPU, Playwright Chromium, GitHub CLI | [Dockerfile](../../.devcontainer/Dockerfile), [Containeranleitung](../../.devcontainer/README.md) |
| Entwicklungsprozess | Codex-Rollen in TOML, Markdown-Wiki mit YAML-Metadaten, GitHub Actions mit `github-script` | [Codex-Konfiguration](../../.codex/config.toml), [Workflows](../../.github/workflows/) |
| Workflowtests | Node.js mit eingebautem `node:test`, keine npm-Pakete; nur Werkzeugtests, kein Produktstack | [Workflowtests](../../tools/github-workflows/test/) |

Die existierende `.python-version` enthält den pyenv-Umgebungsnamen `wow-voiceover`, keine Python-Versionsnummer. Auf einem neuen Host muss diese Umgebung vorhanden sein oder Python 3.10 explizit gewählt werden.

`requirements.txt` enthält überwiegend direkte Versionspins, aber keine vollständige transitive Lockdatei. Torch/TorchAudio werden getrennt im Containerimage installiert. Das ist kein Nachweis für CUDA-Unterstützung oder die Modellkompatibilität des getrennten TTS-Servers. Die aktuelle Containerbasis enthält weder Docker-in-Docker noch Node.js; Node wird nur bei Bedarf für die Workflowtests benötigt.

Für Lua gilt die jeweilige WoW-Client-Laufzeit. Moderne Syntax oder APIs dürfen nicht allein aufgrund einer lokal installierten Lua-Version eingeführt werden. Eingebundene Bibliotheken bleiben mit ihrer Client-Zuordnung erhalten. Änderungen folgen den [Engineering-Prinzipien](../standards/engineering-principles.md) und den tatsächlichen [Schnittstellen](architecture.md).
