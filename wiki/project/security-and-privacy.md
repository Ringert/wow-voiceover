---
type: "Project Context"
title: "Projektsicherheit und Datenschutz"
description: "Konkrete Daten, Systemgrenzen und bekannte Schutzlücken der lokalen Generierung."
tags: ["project", "wow-voiceover"]
status: "draft"
scope: "project"
sources:
  - id: env
    resource: "../../tts_cli/env_vars.py"
  - id: compose
    resource: "../../docker-compose.yml"
  - id: import
    resource: "../../tts_cli/init_db.py"
  - id: tts
    resource: "../../tts_cli/tts_cloning.py"
  - id: ignore
    resource: "../../.gitignore"
  - id: container
    resource: "../../.devcontainer/README.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:35:08Z
---
# Projektsicherheit und Datenschutz

## Daten und Vertrauensgrenzen

| Bereich | Daten und Grenze |
| --- | --- |
| Generierung | Quest-/Gossiptexte, NPC-Metadaten, Voice-Map und Referenzaudio; TTS erhält Text und Referenzkennung |
| Externe Quellen | Datenbankdump über GitHub, optionale Audio-Downloads über Hilfsskripte; Netzwerkantworten sind externe Eingaben |
| Lokale Dienste | MySQL-Datenbank und separater TTS-Server; der CLI-Code konfiguriert keine Authentisierung für TTS |
| WoW | Addon verarbeitet Spielereignisse und speichert Profile/Charakterzustände in `VoiceOverDB` |
| Werkzeuge | Codex-/GitHub-Anmeldungen im privaten Home-Volume, außerhalb des Repositorys |

## Bestehende Kontrollen und Grenzen

`.env`, generierte Ordner, virtuelle Umgebungen, lokale Skillnachweise und lokale Skill-Suchpfade sind ignoriert. Ignorierregeln entfernen keine bereits versionierten Dateien. Die vorhandenen großen JSON-Exporte sind Projektbestand; sie sind keine synthetischen Testfixtures.

MySQL ist im bestehenden Compose-Setup am Host auf `3306:3306` veröffentlicht, verwendet den Rootbenutzer und ein bekanntes Entwicklungskennwort. Das ist kein gehärtetes Betriebssetup. Änderungen an Reichweite, Zugangsdaten oder Umgebung gehören in eine konkrete Infrastrukturarbeit; die Vorlagenübernahme ändert weder Konten noch Netzwerkzustand.

`load_dotenv` lädt `.env`, die MySQL-Werte werden jedoch fest im Code gesetzt. TTS verwendet standardmäßig HTTP auf `localhost:8000`; Protokoll, Host und Port sind über `.env` konfigurierbar, einschließlich HTTPS. Der Client setzt keinen Auth-Header. Download und Synthese überschreiten eine eigene Prozessgrenze; Betrieb und Schutzmaßnahmen des externen Dienstes sind hier nicht nachgewiesen.

`init-db` lädt einen veränderlichen Dump, entpackt ein ZIP und importiert SQL. Einige zusätzliche SQL-Importfehler werden im vorhandenen Code abgefangen, ohne den gesamten Vorgang scheitern zu lassen. Die abschließende Erfolgsmeldung allein belegt daher keine vollständige Datenintegrität. Import und Textkorrektur sind keine allgemeinen Tests und dürfen nicht gegen fremde oder produktive Daten laufen.

## Umgang mit Änderungen und Nachweisen

Für Tests synthetische, begrenzte Dialogdaten und isolierte Datenbanken verwenden. Keine persönlichen Sprachaufnahmen, Zugangsdaten oder Home-Verzeichnisse als Fixtures, Issue-Anhänge oder öffentliche Logs übernehmen. Externe Kommunikation und Veröffentlichung brauchen den passenden Auftrag; aus der bloßen Installation von Werkzeugen entstehen keine zusätzlichen Befugnisse.

Hashing, Dateinamen und Lookup-Schlüssel sind Integritätsverträge des Produkts; MD5-basierte Gossip-Dateischlüssel bieten keinen kryptografischen Schutz. Fehler bei Zuordnung oder Wiederherstellung können falsche Stimmen bzw. fehlende Wiedergabe verursachen.

Rechte an Spieltexten, Referenzstimmen, Modellen und Audiodaten sind getrennt von der Code-Lizenz zu prüfen. Konkrete Aufbewahrungsfristen, Release-Verantwortung, Restore-Nachweis und Rechtefreigaben für neue Datenveröffentlichungen: **To be defined**. Diese Seite ist eine Bestandsaufnahme, keine rechtliche Bewertung oder Betriebsfreigabe.
