---
type: "Project Context"
title: "Produktvision"
description: "Nutzen, Zielgruppen und Produktgrenzen des vorhandenen VoiceOver-Projekts."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: readme
    resource: "../../README.md"
  - id: events
    resource: "../../AI_VoiceOver/VoiceOver.lua"
  - id: tts
    resource: "../../tts_cli/tts_cloning.py"
  - id: history
    resource: "../../RETAIL-PLAN.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T08:45:40Z
---
# Produktvision

VoiceOver macht vorhandene WoW-Quest- und NPC-Dialoge als vorproduzierte Sprachausgabe hörbar. Die Python-Werkzeuge erzeugen Audiodateien und Zuordnungstabellen; das Addon spielt passende Dateien bei Spielereignissen ab. Der laufende WoW-Client benötigt dafür keine Verbindung zum TTS-Dienst.

## Zielgruppen und Nutzen

- **Spieler** hören Questannahme, Questabschluss und NPC-Gossip über das Addon und steuern die Wiedergabe.
- **Audio-/Datenbearbeiter** ordnen NPCs Referenzstimmen zu, erzeugen Dialogaudio und regenerieren gezielt betroffene Dateien.
- **Entwickler und Tester** pflegen die gemeinsame Python-/Lua-Schnittstelle, Client-Kompatibilität und die Generierungsumgebung.

## Grenzen des aktuellen Produkts

Der aktive Generierungspfad nutzt Vanilla-/VMaNGOS-Daten und den externen `lib-tts`-Dienst. Der Code hat mehrere Client-TOCs und Kompatibilitätsschichten; daraus folgt keine bestätigte Unterstützung aller heutigen WoW-Versionen. [RETAIL-PLAN.md](../../RETAIL-PLAN.md) beschreibt historische Ideen für Crowdsourcing und Retail-Portierung. Es belegt weder einen implementierten Uploaddienst noch ein aktuelles Releaseziel.

Die Locale-Auswahl existiert, die Syntheseanfrage verwendet jedoch fest `language: de`. Eine vollständig funktionierende Mehrsprachigkeit ist deshalb kein belegter Bestand. Das Projekt enthält keinen eigenen Webauftritt, Nutzerkonto-Service oder produktiven TTS-Host.

## Beobachtbare Qualität

Geeignete Akzeptanz richtet sich nach der Änderung: richtiger Dialog zur richtigen Quest bzw. zum NPC, konsistente Dateinamen und Tabellen, verständliches Audio, steuerbare Warteschlange und nachvollziehbare Regenerierung. Die [Prüfwege](local-development.md#prüfungen) unterscheiden Syntaxprüfung, simulierte Workflowprüfung, reale Dienstintegration und Ingame-Test. Verbindliche Kennzahlen oder eine neue Roadmap werden aus diesen Zielen nicht abgeleitet.
