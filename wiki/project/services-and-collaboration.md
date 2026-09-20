---
type: "Project Context"
title: "Leistungen und Zusammenarbeit"
description: "Zusammenarbeit am Addon und an der Audiogenerierung ohne erfundene Betriebszusagen."
tags: ["project", "wow-voiceover"]
status: "draft"
scope: "project"
sources:
  - id: readme
    resource: "../../README.md"
  - id: process
    resource: "../standards/development-process.md"
  - id: domain
    resource: "domain-model.md"
  - id: signal
    resource: "../standards/signal-integration.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Leistungen und Zusammenarbeit

Das Repository bietet Quellcode für den VoiceOver-Player, ein Vanilla-Datenmodul und Werkzeuge zur Daten-/Audiobearbeitung. `lib-tts` stellt außerhalb dieses Repositories die Synthese bereit. Ein gehostetes Kundenangebot, Supportvertrag oder SLA ist im untersuchten Bestand nicht belegt.

## Beiträge und Übergaben

Beiträge im Fork laufen über [GitHub-Issues und PRs](github-workflow.md). Eine Story bündelt Bedarf, Akzeptanz, technischen Plan, Code, passende Prüfungen und Dokumentation. Der Orchestrator und die Fachrollen unterstützen diesen Ablauf nach ihren [Rollenverträgen](../standards/index.md); sie sind keine zusätzlichen Produktnutzerrollen.

Ein Audiobeitrag braucht passende Quell-/Referenzdaten, Voice-Map, Dialogidentität, erzeugte Datei und aktualisierte Lookup-/Dauerndaten. Eine Datei ohne diese Zuordnung ist kein vollständig nutzbares Datenpaket. Prüfberichte benennen konkrete Client-/Werkzeugversionen und unterscheiden Codelektüre, Simulation, echte Generierung und Ingame-Wiedergabe.

Die bestehende README enthält externe Community-Verweise. Ihre heutige Zuständigkeit und Verfügbarkeit sind nicht verifiziert. Der ursprüngliche Codex-Chat bleibt der Kommunikationsweg während dieser Arbeit; Signal ist nicht eingerichtet.

Fachliche/technische Ansprechpartner, konkrete Releaseverantwortung und etwaige verbindliche Zusagen: **To be defined**. Aus dem Vorlagenimport entstehen keine Nachrichten an Dritte, Serviceverträge oder öffentlichen Releases.
