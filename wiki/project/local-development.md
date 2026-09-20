---
type: "Project Context"
title: "Projektspezifische Entwicklung"
description: "Einrichtung, Dienstgrenzen und nachvollziehbare Prüfungen für Python, Lua und Workflows."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: container
    resource: "../../.devcontainer/README.md"
  - id: compose
    resource: "../../docker-compose.yml"
  - id: environment
    resource: "../../tts_cli/env_vars.py"
  - id: cli
    resource: "../../cli-main.py"
  - id: import
    resource: "../../tts_cli/init_db.py"
  - id: processor
    resource: "../../tts_cli/tts_cloning.py"
  - id: tests
    resource: "../../tools/github-workflows/test/"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T09:31:03Z
---
# Projektspezifische Entwicklung

## Vorhandene Arbeitsumgebung

Öffne das Repository in VS Code mit **Dev Containers: Reopen in Container**. Die [bestehende Containeranleitung](../../.devcontainer/README.md) beschreibt den Imagebuild und persönliche Anmeldung. Der Workspace liegt unter `/workspaces/wow-voiceover`, Python 3.10 samt Projektabhängigkeiten unter `/opt/venv`; eine Aktivierung ist dort nicht nötig.

Das Volume `wow-voiceover-home-${devcontainerId}` hält `/home/vscode` mit Codex-/GitHub-Anmeldung und VS-Code-Erweiterungen über Rebuilds zusammen. Der Container installiert beim Start nichts und startet keine Projektdienste. Nur Login-Port 1455 ist in VS Code fest weitergeleitet. Die Vorlagenübernahme verändert diese vorhandene Konfiguration nicht.

Für lokale Entwicklung außerhalb des Containers sind Python 3.10, FFmpeg/ffprobe und eine virtuelle Umgebung nötig:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Playwright-Browser sind gesonderte Abhängigkeiten der Download-Hilfswerkzeuge. TTS-Modelle, deren Laufzeit und GPU-Konfiguration gehören ausschließlich zum externen Webservice. Nach der Umstellung eines älteren Images entfernt **Dev Containers: Rebuild Container** die zuvor installierten Modellbibliotheken; eine Änderung am Dockerfile entfernt keine Pakete aus einem bereits laufenden Container. `.python-version` benennt eine pyenv-Umgebung und richtet diese nicht selbst ein.

## Dienste und Konfiguration

| Komponente | Einrichtung und tatsächliche Grenze |
| --- | --- |
| MySQL | `docker-compose.yml` enthält ausschließlich `mysql:8`, Containername `mysql-server`, Port `3306:3306`, Volume `wowdb-data`, Entwicklungskennwort `wow`. Keine explizite Restart-Policy; keine automatische DB-Befüllung. |
| DB-Client | `tts_cli/env_vars.py` verwendet fest `0.0.0.0:3306`, `root`, `wow`, Datenbank `wow`. Die gleichnamigen `.env`-Werte werden derzeit nicht ausgewertet. |
| TTS | Separates Repository `Ringert/lib-tts`; Clientadresse über `TTS_PROTOCOL`, `TTS_HOST` und `TTS_PORT` in `.env` konfigurierbar, Standard `http://localhost:8000`. Server, Modelle und Referenzaudio werden hier nicht bereitgestellt. |

Die `.env` im Repository-Root wird unabhängig vom Arbeitsverzeichnis beim Import der Konfiguration geladen. Bereits gesetzte Umgebungsvariablen haben Vorrang. Fehlende TTS-Werte verwenden die obigen Standardwerte; Änderungen greifen beim nächsten CLI-Start. Das [Benutzerhandbuch](user-manual.md#tts-adresse-einstellen) erklärt die Eingaben.

MySQL bei Bedarf **in einem Hostterminal aus diesem Checkout** starten:

```bash
docker compose up -d
docker compose ps
docker compose logs --tail=100 mysql
```

Die Python-Devcontainer-Basis enthält keinen Docker-Daemon und kein Docker-in-Docker. Ein im Host laufender Dienst ist im Arbeitscontainer nicht dessen `localhost`. Vor einer Generierung aus dem Container muss `TTS_HOST` auf einen aus dem Container erreichbaren Host gesetzt werden. Die MySQL-Adresse bleibt fest codiert; `.env` allein reicht für deren Anpassung aktuell nicht. Der Hoststart von MySQL beweist deshalb noch keine funktionsfähige Verbindung aus der CLI. Ein bestätigter Startbefehl für `lib-tts` gehört zur Dokumentation dieses separaten Dienstes, nicht zu einem geratenen `python main.py` hier.

Die vorhandene Host-Portbindung und der feste MySQL-Containername sind Altbestand. Ein zweiter Checkout kann dadurch kollidieren. Keine zusätzliche `compose.yaml` mit einem Vorlagen-Platzhalter danebenlegen und keinen bestehenden Datenbestand zur Fehlerbehebung löschen. Für eine künftige Umstellung sind Erreichbarkeit und Volume-Zuordnung zusammen zu prüfen.

## Daten vorbereiten und generieren

Alle CLI-Befehle werden aus dem Repository-Root ausgeführt. Die globale Option steht **vor** dem Unterbefehl: `python cli-main.py --lang deDE <modus>`.

1. MySQL-Verbindung, Datenbankziel und TTS-Erreichbarkeit in der tatsächlich verwendeten Umgebung klären.
2. Nur für die bewusst einzurichtende Entwicklungsdatenbank `python cli-main.py init-db` ausführen. Das lädt einen veränderlichen VMaNGOS-Dump, importiert Tabellen und ruft `fix-de` auf. Vorher vorhandene Daten separat sichern; es gibt keinen belegten automatischen Rollback.
3. Vorhandene `voice-clone-map.json` und ihre lokalen WAV-Dateipfade prüfen; Referenzen werden bei jeder Synthese hochgeladen und müssen nicht im TTS-Dienst registriert sein. `create_voice_clone_map` nur bei beabsichtigter Neuverteilung verwenden: Es liest `sql.json`, `gossip.json`, `sound_length.json`, wählt zufällig und überschreibt die Map.
4. Einen kleinen ausgewählten Regenerierungsfall über den [CLI-Nachschlageteil](user-manual.md#cli-nachschlagen) bearbeiten. `interactive` bedeutet im aktuellen Code Verarbeitung aller abgefragten Dialoge und ist kein begrenzter Smoke-Test.
5. Nach Audioänderungen mit `python cli-main.py --lang deDE gen_lookup_tables` die Lua-Lookups und gemessenen Dauern aktualisieren. Der Befehl benötigt MySQL und eine lesbare Voice-Map, überschreibt `output.json` und generierte Tabellen, ruft aber keine Synthese auf.

Audio und Lua-Ausgaben liegen unter `AI_VoiceOverData_Vanilla/generated/`. Der Pfad ist von Git ignoriert. Mehrere Exporte, Locales und Regenerierungen teilen aktuell dieselben Dateien; es gibt keine separate Ausgabe je Locale.

## Prüfungen

Diese unabhängigen Prüfungen starten weder Datenbank noch TTS und generieren kein Audio. Im Devcontainer den Projektinterpreter verwenden; außerhalb davon die aktivierte Python-3.10-Umgebung:

```bash
/opt/venv/bin/python -m pip check
/opt/venv/bin/python -m compileall -q cli-main.py tts_cli
/opt/venv/bin/python cli-main.py --help
/opt/venv/bin/python cli-main.py --lang deDE gen_lookup_tables --help
git diff --check
```

Ein Login-Shell- oder Werkzeugaufruf kann stattdessen `/usr/local/bin/python` auswählen. Bei `ModuleNotFoundError` zuerst den Interpreterpfad prüfen; ein erfolgreiches `pip check` im System-Python belegt nicht, dass die Projektpakete dort installiert sind. Keine zweite Paketinstallation zur Umgehung eines falsch gewählten Interpreters nötig.

`compileall` prüft Syntax; `--help` prüft zusätzlich die geladenen CLI-Abhängigkeiten und den Parser. Beides belegt keine erfolgreiche Abfrage, Audiogenerierung oder Wiedergabe. Die lokalen WAV-Referenzen, Pfadweitergabe, Map-Änderungen und der tatsächlich codierte Multipart-Vertrag werden mit `/opt/venv/bin/python -m unittest discover -s tests -v` geprüft. Die Tests verwenden synthetische WAVs und ersetzen den HTTP-Transport; sie erzeugen keine echte Synthese. Eine automatisierte Lua-Testsuite und ein projektweiter Linter oder Typechecker sind nicht eingerichtet.

Die übernommenen GitHub-Skripte haben isolierte Verhaltenstests mit kontrollierten GraphQL-Antworten. Sie verwenden den tatsächlich ausgelieferten `github-script`-Code, ohne GitHub zu verändern. Voraussetzung ist eine Node.js-Version mit `node:test` (ab 18); Node ist kein Bestandteil des bestehenden Devcontainer-Images. Bei Bedarf kann es manuell in der laufenden Arbeitsumgebung installiert werden, etwa über `sudo apt-get update` und `sudo apt-get install -y nodejs`.

```bash
node --test tools/github-workflows/test/*.test.mjs
```

| Änderung | Erforderlicher zusätzlicher Nachweis |
| --- | --- |
| Text-/Hash-/Dateikonvention | Kleine synthetische Quest-/Gossip-Fälle einschließlich Gender-Präfixen; Python-Ausgabe gegen Lua-Verbrauch prüfen |
| SQL oder Import | Isolierte MySQL-8-Datenbank mit begrenzten Fixtures; Seiteneffekte und Wiederholung prüfen |
| TTS-HTTP-Client | Multipart-Felder ohne `voice_id`, WAV-Inhalt/-Grenzen, Pfadweitergabe, fehlende `file_id`, Fehler und Überschreibeverhalten kontrolliert prüfen; echte Verbindung gesondert benennen |
| Addon/Kompatibilität | Passende WoW-Clientversion, konkrete Quest/Gossip und Queue-Steuerung im Spiel prüfen |
| Wiki/Codex | YAML-/TOML-Struktur, lokale Links/Anker, Quellen und Bestandsaussagen prüfen; Client-Neuladen für reale Agentenerkennung |
| GitHub-Zuordnung | Lokale Workflowtests; ein späterer echter Actions-Lauf ist ein eigener Nachweis |

## Betrieb beenden und Daten erhalten

`docker compose stop` stoppt MySQL, `docker compose down` entfernt Container und Netz. Benannte Volumes bleiben ohne `-v` erhalten. `down -v`, Volume-Löschung und Pruning sind keine normalen Reparaturschritte. Datenbank, Voice-Map, Exporte und generiertes Audio bilden einen zusammengehörigen Bearbeitungsstand; Wiederherstellung ist nur mit passend gesicherten Beständen möglich. Ein praktisch geprüfter Restore ist bisher nicht dokumentiert.
