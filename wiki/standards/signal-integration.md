---
type: "Policy"
title: "Optionale Signal-Anbindung"
description: "Grenze der nicht eingerichteten optionalen Kommunikationsintegration der Vorlage."
tags: ["shared", "wow-voiceover"]
status: "stable"
scope: "shared"
sources:
  - id: template
    resource: "https://github.com/Ringert/Codex-Projektvorlage/blob/b001e1b700d75aa0f31f6ced84381ba194b79582/wiki/standards/signal-integration.md"
  - id: config
    resource: "../../.codex/config.toml"
  - id: container
    resource: "../../.devcontainer/README.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Optionale Signal-Anbindung

Signal ist in **wow-voiceover nicht installiert oder konfiguriert**. Es gibt hier weder `tools/signal-bridge` noch einen Signal-MCP-Eintrag oder den projektlokalen Signal-Skill. Der bestehende Devcontainer enthält die dafür vorgesehene Bridge-Laufzeit nicht. Das Importieren der Rollen autorisiert keine Konto-Kopplung und keinen Nachrichtenversand.

## Kommunikation im aktuellen Projekt

Fortschritt, notwendige Rückfragen und Antworten bleiben im ursprünglichen Codex-Chat. Fehlendes Signal blockiert weder eine Story noch Dokumentationsarbeit. Es werden keine wiederholten Connectversuche, Reparaturtickets oder künstlichen Nutzerfreigaben erzeugt. Bewusste Stopps und die nativen Goal-Regeln bleiben maßgeblich.

## Werkzeugvertrag einer späteren Integration

Die genaue optionale Implementierung bleibt in der geprüften Vorlage referenziert: [Integrationsvertrag](https://github.com/Ringert/Codex-Projektvorlage/blob/b001e1b700d75aa0f31f6ced84381ba194b79582/wiki/standards/signal-integration.md), [Signal-Skill](https://github.com/Ringert/Codex-Projektvorlage/blob/b001e1b700d75aa0f31f6ced84381ba194b79582/.codex/skills/signal-communication/SKILL.md) und [Bridge-Schemas](https://github.com/Ringert/Codex-Projektvorlage/blob/b001e1b700d75aa0f31f6ced84381ba194b79582/tools/signal-bridge/src/mcp.mjs). Diese Quellen beschreiben ein anderes Setup; sie sind hier keine automatisch ausführbaren Handlungsanweisungen.

Ein späterer ausdrücklicher Integrationsauftrag muss Werkzeugcode, Laufzeiten, Skill, Codex-Konfiguration und Containerbasis gemeinsam prüfen. Keine Kopie persönlicher Konten oder privater Originale. Einrichtung bleibt bedarfsweise, ohne Containerstart-Hook, Hostport oder Host-Docker-Socket. Persönliche Kopplung, tatsächliche Zustellung und Antwortzuordnung brauchen jeweils eigene Nachweise; die Integration ersetzt keine native Freigabe. Autorisierung für Kommunikation wird nicht aus einer verfügbaren Werkzeugliste abgeleitet.
