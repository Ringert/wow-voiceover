---
type: "Project Context"
title: "Projektauslieferung und Betrieb"
description: "Vorhandene Addon-Pakete, Datenartefakte und Grenzen des Release- und Dienstbetriebs."
tags: ["project", "wow-voiceover"]
status: "draft"
scope: "project"
sources:
  - id: release
    resource: "../../.github/workflows/release-player.yaml"
  - id: template
    resource: "../../.github/release-template.md"
  - id: module
    resource: "../../AI_VoiceOverData_Vanilla/AI_VoiceOverData_Vanilla.toc"
  - id: compose
    resource: "../../docker-compose.yml"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Projektauslieferung und Betrieb

## Artefakte und Laufzeit

Das Produkt wird als WoW-Addon samt getrenntem Datenmodul installiert. Es gibt in diesem Repository keinen zu deployenden Webserver. MySQL und `lib-tts` werden für die Audioerzeugung gebraucht, nicht zur Wiedergabe im Spiel. Generierte Audiodaten und Lookup-Tabellen müssen passend zum Player und zum vorgesehenen Inhalt ausgeliefert werden.

| Artefakt | Vorhandener Auslieferungsweg |
| --- | --- |
| `AI_VoiceOver` | Player mit Lua-Dateien, TOCs und eingebundenen Bibliotheken |
| `AI_VoiceOverData_Vanilla` | Modul und Metadaten im Repository; `generated/` muss durch vorhandene passende Datenpakete oder bewusste Generierung ergänzt werden |
| `release/*.zip` | Temporäre Player-ZIPs des Tag-Workflows; keine automatisch erzeugten Voiceover-Audios |
| MySQL-Volume | Lokaler Generierungsbestand; nicht Teil eines Addon-Releases |

## Bestehender Releaseworkflow

[release-player.yaml](../../.github/workflows/release-player.yaml) reagiert auf Tags `v*.*.*`. Es ersetzt die TOC-Platzhalterversion `0.0.0`, kopiert vier Playerverzeichnisse, wählt die jeweiligen generischen TOCs und packt ZIPs für 1.12, 2.4.3, 3.3.5 und die als `WoW_BlizzClassic` bezeichnete Variante. Für Letztere verwendet der bestehende Workflow den Mainline-TOC. Diese Benennung ist kein Nachweis aktueller Clientkompatibilität.

Das Ergebnis wird als **Draft Release** angelegt. Der Workflow führt keine Produkt- oder Audiogenerierungstests aus und paketiert das Vanilla-Audio nicht selbst. Die Release-Notizen enthalten weiterhin feste `mrthinger/wow-voiceover`-Links, einschließlich eines alten separaten Datenpakets. Vor einem tatsächlichen Release dieses Forks sind Ziel-URLs, Versionen und passende Datenartefakte konkret zu prüfen; die Vorlagenübernahme ändert oder veröffentlicht diesen Releaseweg nicht.

Die neuen Issue-/PR-Workflows sind Verwaltungsprüfungen und verändern den Releaseworkflow nicht. Ein Tag kann den vorhandenen Releasejob starten und wird daher nicht als allgemeiner Entwicklungsschritt erzeugt.

## Betriebs- und Prüfnachweise

Addon-Lua, Client-API und passende Audio-/Lookupdaten müssen in der vorgesehenen Clientversion gemeinsam geprüft werden. Eine Syntaxprüfung auf Linux reicht dafür nicht. Für die Generierung sind reale MySQL- und TTS-Erreichbarkeit sowie eine passende Referenzstimme erforderlich. Aktueller Service-Host, Modellbetrieb, Monitoring und Release-Verantwortung: **To be defined**.

## Sicherung und Wiederherstellung

Voice-Map, zugrunde liegende JSON-Exporte, erzeugte MP3s und Lua-Lookups zusammen sichern. Den MySQL-Datenbestand separat sichern; ein Docker-Volume ist kein Backup. Den persönlichen Devcontainer-Zustand vertraulich außerhalb des Checkouts halten. `docker compose down` ohne `-v` bewahrt das Datenvolume, eine Volume-Löschung nicht.

Ein Restoreverfahren und ein getesteter Release-Rollback sind bislang nicht belegt. Kein Datenbankimport, keine Neuverteilung der Stimmen und keine Löschung zur bloßen Überprüfung ausführen. Ein technisch erzeugtes Draft Release ist nach [Governance](../standards/governance.md) von einer öffentlichen Veröffentlichung zu unterscheiden.
