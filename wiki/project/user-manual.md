---
type: "Project Context"
title: "Benutzerhandbuch"
description: "Addon verwenden und Dialogaudio mit den vorhandenen CLI-Befehlen bearbeiten."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: cli
    resource: "../../cli-main.py"
  - id: options
    resource: "../../AI_VoiceOver/Options.lua"
  - id: defaults
    resource: "../../AI_VoiceOver/VoiceOver.lua"
  - id: data
    resource: "../../AI_VoiceOverData_Vanilla/AI_VoiceOverData_Vanilla.toc"
  - id: tts
    resource: "../../tts_cli/tts_cloning.py"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:35:08Z
---
# Benutzerhandbuch

## Was VoiceOver leistet

VoiceOver spielt vorproduzierte NPC- und Questaufnahmen im Spiel ab. Der Player und das passende Datenpaket werden gemeinsam benötigt. Eine Installation allein erzeugt keine fehlenden Aufnahmen. Entwickler können Audio mit der Python-CLI vorbereiten; für Spieler ist der TTS-Dienst nicht Teil des laufenden Addons.

Diese Anleitung basiert auf dem Quellcode. Ingame-Bedienung, heutige Clientkompatibilität und die vollständige MySQL-/TTS-Kette wurden mit der Wiki-Übernahme nicht ausgeführt.

## Addon installieren

1. Ein Playerpaket für die tatsächlich verwendete Clientversion und ein dazu passendes Datenpaket bereitstellen. Die [Auslieferungsseite](deployment.md) erklärt vorhandene Paketvarianten und Grenzen der alten Downloadlinks.
2. `AI_VoiceOver` und `AI_VoiceOverData_Vanilla` in den `Interface/AddOns`-Ordner des gewählten WoW-Clients legen. Es darf keine zusätzliche gleichnamige Ordnerebene zwischen `AddOns` und den TOC-Dateien entstehen.
3. Bei Verwendung eines Quellcheckouts statt eines Releasepakets den richtigen Client-TOC wählen. Legacy-Pakete verwenden `AI_VoiceOver.toc`; vorhandene Quellen heißen beispielsweise `AI_VoiceOver_1.12.toc`, `AI_VoiceOver_2.4.3.toc` und `AI_VoiceOver_3.3.5.toc`. Moderne Varianten haben eigene Suffixe. Ein vorhandener TOC belegt keine Kompatibilität mit einer neueren Spielversion.
4. Sicherstellen, dass das Datenpaket die im [Datenmodul-TOC](../../AI_VoiceOverData_Vanilla/AI_VoiceOverData_Vanilla.toc) aufgeführten `generated/*.lua`-Dateien und die zugehörigen MP3s enthält. Ein frischer Checkout bringt die generierten Audiodateien nicht automatisch mit.
5. Das Spiel starten bzw. die Oberfläche neu laden und den Player aktivieren. Das Datenmodul wird vom Player bei Bedarf geladen; die Anzeige „disabled“ oder „out of date“ des Datenmoduls allein belegt laut dessen Metadaten keinen Ausfall. Den tatsächlichen Ladezustand unter **Data Modules** prüfen.

## Im Spiel hören und steuern

Öffne einen vertonten NPC-Dialog oder eine passende Questannahme bzw. einen Questabschluss. Der Player sucht die Aufnahme und reiht sie in die Warteschlange ein. Nicht jeder Dialog ist vertont. Automatische Questfortschrittswiedergabe ist aktuell nicht registriert.

Die Standardbelegung des Minimapbuttons ist:

| Aktion | Ergebnis |
| --- | --- |
| Linksklick | **Open Options** – Einstellungen öffnen |
| Mittelklick | **Play/Pause Audio** – Warteschlange pausieren/fortsetzen, soweit der Client dies unterstützt |
| Rechtsklick | **Clear Queue** – Wiedergabe beenden und Warteschlange leeren |

Die Belegung ist konfigurierbar. Die vorhandenen Befehle **Play Audio**, **Pause Audio**, **Skip Line** und **Clear Queue** setzen fort, pausieren, überspringen den aktuellen Eintrag oder leeren die Queue. Die Optionen enthalten unter anderem Soundkanal, Gossip-Häufigkeit, Stoppen beim Gesprächsende, Größe/Position/Sichtbarkeit der Queue und Profile. Legacy-Clients haben zusätzliche Musikkanal-/Porträtoptionen. Einstellungen werden in `VoiceOverDB` gespeichert.

## Audio bearbeiten

Voraussetzung sind die [Entwicklungsumgebung](local-development.md), eine erreichbare passende Datenbank, ein betriebsbereiter `lib-tts`-Dienst mit Referenzstimmen und zusammenpassende JSON-Dateien. Die Befehle laufen aus dem Repository-Root. Die globale Sprachoption steht vor dem Modus; aktuell wird die TTS-Anfrage unabhängig davon auf Deutsch gesendet.

Für eine gezielte Quest-Regenerierung, beispielsweise bei bewusst ausgewählter Quest-ID 70:

```bash
python cli-main.py --lang deDE regenerate quest 70-accept
python cli-main.py --lang deDE gen_lookup_tables
```

Die Regenerierung verwendet vorhandene Exporte und kann die Audiodatei ersetzen. `gen_lookup_tables` aktualisiert anschließend Zuordnungen und Dauerntabelle. Vorher den zu bearbeitenden Audio-/JSON-Stand sichern; ein automatisches Undo existiert nicht. Die beispielhafte Quest-ID ist kein Anspruch auf vorhandene Audiodaten.

## TTS-Adresse einstellen

Bearbeite `.env` im Repository-Root. Falls sie fehlt, kopiere `.env.example` nach `.env`.

```dotenv
TTS_PROTOCOL=http
TTS_HOST=localhost
TTS_PORT=8000
```

`TTS_PROTOCOL` ist `http` oder `https`. `TTS_HOST` enthält nur den Hostnamen oder die IP-Adresse, ohne Protokoll, Port oder Pfad. `TTS_PORT` ist der Port des Dienstes. Beispielsweise ergeben `https`, `tts.example.org` und `8443` die Basisadresse `https://tts.example.org:8443`. Synthese und Audiodownload verwenden dieselbe Adresse.

Fehlende Werte verwenden die gezeigten Defaults; bereits gesetzte Umgebungsvariablen haben Vorrang. Starte die CLI nach Änderungen neu. `.env` bleibt lokal und wird von Git ignoriert. Im Devcontainer bezeichnet `localhost` den Container selbst; für einen externen Dienst trage dessen erreichbaren Host ein.

## CLI nachschlagen

| Unterbefehl | Wirkung und Voraussetzung |
| --- | --- |
| `init-db` | VMaNGOS-Dump herunterladen/importieren und deutsche Datenbanktexte korrigieren; nur für ein bewusst gewähltes Entwicklungsziel |
| `fix-de` | Deutsche Textkorrekturen in bestehenden Datenbanktabellen ausführen |
| `interactive` | Alle abgefragten Dialoge vorverarbeiten und vertonen; trotz Name derzeit kein Auswahlassistent |
| `gen_lookup_tables` | MySQL abfragen, `output.json`, Lua-Lookups und MP3-Längen aktualisieren; keine Synthese |
| `create_voice_clone_map` | Aus `sql.json`, `gossip.json`, `sound_length.json` eine neue zufällige Referenzzuordnung erzeugen; überschreibt die Map |
| `extract_model_data` | Aus vorhandenen Display-/Modelldaten `generated/warcraft-display-metadata.csv` erzeugen |
| `regenerate quest <id-source>` | Einzelnen Questdialog regenerieren, z. B. `70-accept` |
| `regenerate gossip <hash>` | Einzelnen Gossipdialog anhand seines bestehenden Hashes regenerieren |
| `regenerate_for_npc "<Name>"` | Dialoge eines exakt im Export vorhandenen NPC-Namens regenerieren |
| `regenerate_by_text "<Text>"` | Dialoge über eine Suche ohne Beachtung der Groß-/Kleinschreibung auswählen |
| `regenerate_by_race <race_id> [sex_id]` | Dialoge nach DisplayRaceID, optional DisplaySexID auswählen |
| `regenerate_all_with_voice <voice>` | Dialoge der NPCs mit einer bestimmten Referenzstimme regenerieren |
| `switch_voice <old_voice> <new_voice>` | Referenzstimme in der Map ersetzen und betroffene NPCs neu vertonen |

`python cli-main.py --help` und `python cli-main.py <modus> --help` zeigen die tatsächlich unterstützten Argumente. Ohne Modus startet die CLI die vollständige Verarbeitung; ein leerer Aufruf ist deshalb kein Hilfe- oder Gesundheitscheck.

## Hilfe bei Problemen

| Symptom | Prüfen und nächste Handlung |
| --- | --- |
| Kein Datenmodul | Ordnerstruktur, `RequiredDeps`, generierte Lua-Dateien und Ladezustand in **Data Modules** prüfen |
| Einzelne Aufnahme fehlt | Dateiname, `m-`/`f-`-Variante, Sprach-/Exportstand und Dauerntabelle abgleichen; gegebenenfalls gezielt regenerieren |
| `Connection refused` bei TTS | Den tatsächlich verwendeten Netzwerkraum und die [TTS-Adresse in `.env`](#tts-adresse-einstellen) prüfen; `localhost` bezeichnet im Devcontainer den Container selbst |
| MySQL nicht erreichbar | Host-Compose-Status und feste Werte in `env_vars.py` prüfen; Host-/Devcontainer-Adresse unterscheiden |
| `KeyError` bei Stimme | Exakten NPC-Namen und Referenz in `voice-clone-map.json` prüfen; nicht ungeprüft die gesamte Map neu erstellen |
| Falsche Sprache | `--lang` steuert derzeit nicht den festen deutschen TTS-Payload; eine Sprachumstellung benötigt eine Codeänderung |
| Erfolgsmeldung, aber keine MP3 | CLI-Fehlertext, TTS-Logs und tatsächliche Ausgabedatei prüfen; ein Exitcode allein ist kein Generierungsnachweis |

Für reproduzierbare Fehler im Fork ein Issue in [Ringert/wow-voiceover](https://github.com/Ringert/wow-voiceover/issues) mit Client-/Python-Version, relevantem Befehl, erwartetem und beobachtetem Ergebnis erstellen. Keine persönlichen Zugangsdaten, ganzen Home-Verzeichnisse oder privaten Sprachsamples anhängen.
