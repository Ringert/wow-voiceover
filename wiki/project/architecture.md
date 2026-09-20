---
type: "Project Context"
title: "Projektarchitektur"
description: "Datenfluss und Schnittstellen zwischen Generierung, TTS-Service und WoW-Addon."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: cli
    resource: "../../cli-main.py"
  - id: sql
    resource: "../../tts_cli/sql_queries.py"
  - id: tts
    resource: "../../tts_cli/tts_cloning.py"
  - id: addon
    resource: "../../AI_VoiceOver/VoiceOver.lua"
  - id: modules
    resource: "../../AI_VoiceOver/DataModules.lua"
  - id: data
    resource: "../../AI_VoiceOverData_Vanilla/Module.lua"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T09:31:03Z
---
# Projektarchitektur

Das Repository verbindet zwei getrennte Laufzeiten: Offline-Generierung in Python und Wiedergabe im WoW-Client. Das Vanilla-Datenmodul ist die Übergabe zwischen ihnen.

```mermaid
flowchart LR
    DB[(MySQL / VMaNGOS)] --> CLI[Python CLI]
    MAP[voice-clone-map.json] --> CLI
    CLI -->|Text und lokale WAV als Multipart| TTS[Separater lib-tts-Dienst]
    TTS -->|Audiodownload| CLI
    CLI --> DATA[Vanilla-Datenmodul: Lua-Tabellen und MP3]
    DATA --> ADDON[WoW-Addon: Lookup und SoundQueue]
    GAME[Quest- und Gossip-Ereignisse] --> ADDON
```

## Bausteine und Einstiegspunkte

| Baustein | Verantwortung |
| --- | --- |
| [cli-main.py](../../cli-main.py) | Argumente, globale Locale und Auswahl der Arbeitsmodi |
| [sql_queries.py](../../tts_cli/sql_queries.py) | MySQL-Abfragen, Locale-Textauswahl, Export nach `output.json`, deutsche Textkorrekturen |
| [tts_cloning.py](../../tts_cli/tts_cloning.py) | Stimmenzuordnung, Text-/Gender-Varianten, Dateinamen, Synthese und Lua-Lookups |
| [length_table.py](../../tts_cli/length_table.py) | Reale MP3-Längen mit mutagen lesen und `sound_length_table.lua` schreiben |
| [init_db.py](../../tts_cli/init_db.py) | Datenbankdump herunterladen, SQL-Dateien und Display-Metadaten importieren |
| [VoiceOver.lua](../../AI_VoiceOver/VoiceOver.lua) | Addoninitialisierung, SavedVariables, Quest-/Gossip-Ereignisse |
| [DataModules.lua](../../AI_VoiceOver/DataModules.lua) | Datenmodule finden/laden, Quest- und Gossip-Dateien auflösen |
| [SoundQueue.lua](../../AI_VoiceOver/SoundQueue.lua) | Warteschlange, Wiedergabe, Pause und Entfernen von Einträgen |
| [Options.lua](../../AI_VoiceOver/Options.lua), [SoundQueueUI.lua](../../AI_VoiceOver/SoundQueueUI.lua) | Optionen, Warteschlangenanzeige und Nutzersteuerung |
| [Compatibility.lua](../../AI_VoiceOver/Compatibility.lua), [Version.lua](../../AI_VoiceOver/Version.lua) | Clientabhängige APIs und Legacy-Unterschiede |
| [Module.lua](../../AI_VoiceOverData_Vanilla/Module.lua) | Registrierung des Vanilla-Datenmoduls und relative MP3-Pfade |

`cli-main.py` verwendet ausschließlich den HTTP-Client aus `tts_cloning.py`. Modellwahl, Modellgewichte und Laufzeit liegen beim separaten Webservice. Der Client übergibt explizite Syntheseparameter im HTTP-Payload. Im Projekt gibt es keinen lokalen Syntheseweg und keinen alternativen Anbieterclient.

## Datenfluss und Seiteneffekte

1. `init-db` lädt den VMaNGOS-Dump, importiert Daten und ruft deutsche Textkorrekturen auf. Das ist eine Datenänderung, kein Bereitschaftstest.
2. `query_dataframe_for_all_quests_and_gossip` erstellt den DataFrame und überschreibt zugleich `output.json` im Arbeitsverzeichnis.
3. Der Processor lädt `voice-clone-map.json`, behält den Ursprungstext für Gossip-Hashes und erzeugt sprechbare Text-/Gender-Varianten.
4. `interactive` läuft derzeit über alle abgefragten Dialoge und erzeugt Audio seriell. Bereits vorhandene MP3s werden normalerweise übersprungen; Regenerierung kann sie überschreiben.
5. `gen_lookup_tables` schreibt Lua-Zuordnungen und misst vorhandene MP3s. Es erzeugt selbst **kein Audio**.
6. Der Client lädt das Datenmodul bei Bedarf. Dateiname und Dauerntabelle müssen zusammenpassen, damit die Queue eine Aufnahme zuordnen und zeitlich steuern kann.

## HTTP-Vertrag des Clients

`TTSProcessor.tts` verwendet die gemeinsame Basisadresse aus `tts_cli/env_vars.py`, zusammengesetzt aus `TTS_PROTOCOL`, `TTS_HOST` und `TTS_PORT` (Standard: `http://localhost:8000`). Es sendet `POST {TTS_BASE_URL}/api/v1/synthesize` als `multipart/form-data`: Das Textfeld `request` enthält JSON mit `text`, festem `language: de` und den expliziten Syntheseparametern aus `tts_cloning.py`; das Dateifeld `file` enthält die lokale WAV als `audio/wav`. `voice_id` wird nicht gesendet, da es zusammen mit `file` unzulässig ist. Die Map enthält lokale WAV-Pfade; relative Pfade werden vom Repository-Root aufgelöst. `tts_row` und sämtliche Regenerierungswege übergeben den zugeordneten Pfad an `tts`, das die Datei liest und mitsendet. Es erwartet eine JSON-Antwort mit `file_id` und lädt danach `{TTS_BASE_URL}/api/v1/sounds/{file_id}`. Die am 20. September 2026 gelesene Dienstanleitung warnt vor dem nicht registrierten Rückgabepfad in `file_path`. POST-Timeout: 300 Sekunden; Download-Timeout: 60 Sekunden. Der Rückgabedownload wird unter dem eigenen Quest-/Gossip-Dateinamen als MP3 gespeichert.

Bei Payloadänderungen ist die aktuelle Markdown-Anleitung unter `{TTS_BASE_URL}/user-manual.md` zusammen mit dem dort verlinkten `/openapi.json` maßgeblich. Die WAV-Grenze beträgt 10 MiB, das JSON-Feld höchstens 1 MiB und der gesamte Multipart-Body höchstens 11 MiB. Der Client prüft Dateiendung, Größe und RIFF/WAVE-Kennung; die vollständige Audioformatprüfung übernimmt der Dienst. Die Referenz ist dort temporär und wird nicht als Voice registriert. Sampling, Penalties, Referenzlängen, Geschwindigkeit und Normalisierung werden explizit übergeben. `pitch` ist im Schema reserviert und derzeit ohne Wirkung. `ref_text` wird mangels Referenztranskript nicht gesetzt; bei Qwen kann der Dienst dann automatisch transkribieren. Die tatsächlich wirksamen Parameter hängen vom Modelladapter im Dienst ab.

Das beschreibt den konsumierten Clientvertrag. Der Server liegt außerhalb des Checkouts; dessen Startbefehl, Authentisierung, Modelldateien und aktuelle Implementierung sind hier nicht verifiziert. Fehler werden im aktuellen Client vielfach als Text zurückgegeben. Ein Prozessende mit Exitcode 0 allein beweist daher keine vollständige Audiogenerierung.

## Bestehende Grenzen

MySQL-Verbindungswerte sind in `env_vars.py` fest codiert, obwohl `.env` geladen wird. Die TTS-Adresse ist über `.env` konfigurierbar; die Synthesesprache bleibt fest codiert. Der Arbeitscontainer startet keine Dienste; `localhost` bezeichnet dort den Container selbst. Die [Entwicklungsanleitung](local-development.md) erklärt die Folgen.

Die Namen-/Hash- und Geschlechtskonventionen sind im [Fachmodell](domain-model.md) beschrieben. Client-TOCs, `addon.xml`-Ladereihenfolge und eingebundene Legacy-Bibliotheken sind Teil des Laufzeitvertrags. Der historische [Retail-Plan](../../RETAIL-PLAN.md) gehört nicht zum belegten Architekturstand.
