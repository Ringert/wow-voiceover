---
type: "Project Context"
title: "Fachliches Modell"
description: "Dialoge, Stimmen, Locales und der Dateivertrag zwischen Python und Lua."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: queries
    resource: "../../tts_cli/sql_queries.py"
  - id: processor
    resource: "../../tts_cli/tts_cloning.py"
  - id: constants
    resource: "../../tts_cli/consts.py"
  - id: locales
    resource: "../../tts_cli/utils.py"
  - id: modules
    resource: "../../AI_VoiceOver/DataModules.lua"
  - id: events
    resource: "../../AI_VoiceOver/VoiceOver.lua"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T09:31:03Z
---
# Fachliches Modell

| Begriff | Bedeutung und Vertrag |
| --- | --- |
| Dialog | Questtext oder Gossip-Text, einem Sprecher und einer Interaktion zugeordnet |
| `source` | `accept`, `progress`, `complete` oder `gossip`; der Datenbestand kann mehr Interaktionen enthalten als aktuell im Addon aktiv registriert sind |
| Quest | `quest` enthält die Quest-ID; der Basisaudioname ist `<quest>-<source>` |
| Sprecher | `type` unterscheidet `creature`, `gameobject`, `item`; `id` ist die jeweilige Objekt-ID, `name` der Name |
| NPC-Stimme | `voice-clone-map.json` ordnet **NPC-Namen** einem lokalen WAV-Pfad wie `wow-voiceover/de/human/m-human-15.wav` zu; keine Zuordnung nach NPC-ID |
| NPC-Rasse/-Geschlecht | `DisplayRaceID` und `DisplaySexID` werden über `RACE_DICT` und `GENDER_DICT` übersetzt; `-1` steht für einen Erzähler bei unbelebten Quellen |
| Spieler-Geschlecht | Eigener Wert `player_gender`: `m`, `f` oder nicht gesetzt; nicht mit dem Sprecher-Geschlecht verwechseln |
| Datenmodul | Lua-Tabelle mit Lookupdaten, Priorität, Mapzuordnung, Formatversion und Audiopfaden; vom Player getrennt installierbar |
| SoundQueue | Laufende/geplante Voiceovers; Fortschritt wird unter anderem mit den gemessenen Dateilängen gesteuert |

## Text und Dateinamen

Die Abfrage liefert unter anderem `source`, `quest`, `text`, `original_text`, `DisplayRaceID`, `DisplaySexID`, `name`, `type` und `id`. `original_text` bleibt die Grundlage des Gossip-Schlüssels; `text` dient der lokalisierten bzw. bereinigten Sprachausgabe. Die Vorverarbeitung ergänzt `race`, `gender`, `voice_name`, `templateText_race_gender_hash`, `cleanedText` und `player_gender`.

Für Gossip bildet der aktuelle Python-Pfad einen MD5-Hash aus der unveränderten Zeichenkettenverkettung `original_text + race + gender`. MD5 dient hier als Dateischlüssel, nicht als Sicherheitsmechanismus. Die Lua-Zuordnung verwendet die erzeugten Lookuptabellen und Textvergleich. Änderungen an Ursprungstext, Race-/Gender-Mapping oder Normalisierung können bestehende Audioreferenzen verändern.

`$G...:...;` bzw. `$g...:...;` erzeugt männliche und weibliche Spielervarianten. Die Dateien erhalten im regulären Generierungspfad `m-` oder `f-` **vor** dem Basisnamen, etwa `m-70-accept.mp3`. Das Addon versucht entsprechende Präfixe. `REPLACE_DICT` und `clean_text` behandeln weitere Platzhalter; verbleibende `$`, `<` oder `>` führen im normalen Verarbeitungsweg zum Überspringen des Textes. Nicht jede Regenerierungsfunktion verwendet denselben Pfad; Änderungen brauchen gezielte Vertragsprüfungen.

## Dateien und führende Quellen

| Datei/Ablage | Zweck |
| --- | --- |
| `output.json` | Von der aktuellen SQL-Abfrage geschriebener Export; Regenerierungsbefehle lesen ihn wieder ein |
| `sql.json`, `gossip.json`, `sound_length.json` | Eingaben der Voice-Map-Erzeugung; nicht automatisch mit jedem neuen Export synchronisiert |
| `voice-clone-map.json` | Aktuelle NPC-Namen-Zuordnung zum lokalen WAV-Pfad einschließlich Endung |
| `AI_VoiceOverData_Vanilla/generated/sounds/quests/` | Quest-MP3s |
| `AI_VoiceOverData_Vanilla/generated/sounds/gossip/` | Gossip-MP3s |
| `AI_VoiceOverData_Vanilla/generated/*.lua` | Vom Modul-TOC geladene Lookups und `SoundLengthLookupByFileName` |
| `VoiceOverDB` | Vom Addon über WoW SavedVariables gespeicherte Profile und Charakterzustände |

`create_voice_clone_map` trifft zufällige Referenzauswahlen aus vorhandenen Daten und überschreibt die Map. Es ist kein idempotenter Vorbereitungsschritt für jeden Lauf. Gleichnamige NPCs teilen einen Map-Schlüssel. Arbeitsverzeichnis und zusammenpassende Export-/Audiodaten sind deshalb wesentlich.

## Locales und Kompatibilität

`utils.py` erkennt `enUS/enGB`, `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX` und `ruRU`; die CLI verwendet standardmäßig `deDE`. Das ist eine Parser-/Abfragefähigkeit, keine belegte Audioabdeckung. Der HTTP-Payload bleibt deutsch; außerdem bildet der vorhandene TTS-Sprachhelfer den russischen Fall auf `zu` ab. Änderungen an Mehrsprachigkeit müssen diese getrennten Ebenen beachten.

`QUEST_PROGRESS` ist in `VoiceOver.lua` aktuell auskommentiert. Vorhandene `progress`-Datensätze oder SoundEvent-Werte belegen deshalb keine aktive automatische Fortschrittswiedergabe.
