---
type: Policy
title: Auslieferung und Betrieb
description: Anforderungen an tatsächlich unterstützte Betriebswege.
tags:
- shared
- deployment
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/deployment.md
  title: 'Vorlage vor der Wiki-Migration: standards/deployment.md'
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# Auslieferung und Betrieb

## Bedarf und tatsächliche Fähigkeit

CI, externe Vorschau, Hosting, Deployment und Produktivbetrieb werden nur für einen gegenwärtigen Bedarf und nach einer bewussten Architekturentscheidung eingeführt. Produktqualität verlangt passende Nachweise, aber nicht automatisch eine solche Infrastruktur.

Der lokale Entwicklerweg bleibt der [manuell gestartete Compose-Betrieb](local-development.md). Er begründet keinen öffentlichen Betrieb. Für das konkrete Projekt beschreibt [Projektbetrieb](../project/deployment.md) ausschließlich tatsächlich implementierte und geprüfte Auslieferungswege; geplante Infrastruktur bleibt in GitHub.

Eine Auslieferungsfähigkeit gilt erst als unterstützt, wenn sie aktuell entschieden, implementiert, mit ungefährlicher Konfiguration reproduzierbar geprüft und mit realen Einstiegspunkten dokumentiert ist. Ein erfolgreicher Build oder kopierte Altdateien allein reichen nicht aus.

## Auslieferungsvertrag

Jeder tatsächlich unterstützte Weg dokumentiert die zutreffenden Punkte:

- Zielumgebung, erzeugtes Artefakt und reproduzierbaren Auslieferungsbefehl;
- Konfiguration, Secrets und deren sichere Validierung;
- getrennte Identitäten, Datenbanken, Dateien und Empfänger verschiedener Umgebungen;
- Migrationen, Reihenfolge, Fehlerverhalten und sicheren Rückfallweg;
- passende Bereitschaftskriterien und eindeutiges Verhalten bei einer fehlgeschlagenen Freigabe;
- für Webdienste insbesondere TLS, Header, Cache-, Origin-, Robots- und Canonical-Regeln des realen Betriebsmodells.

## Betriebsvertrag

Ein Betrieb mit realen Daten dokumentiert zusätzlich Gesundheitszustand, redigierte Logs, relevante Metriken und Alarmwege, minimal berechtigte Zugänge und Secret-Wechsel, Datensicherung und Aufbewahrung sowie eine praktisch geprüfte isolierte Wiederherstellung. Wichtige Funktionen und Migrationen besitzen einen Diagnose- und Rückfallweg. Verantwortung und Grenzen externer Dienste sind benannt.

Freigaben, Migrationen, Sicherung und Rückfall beziehen sich auf konkrete Artefakte und Datenbestände. Ein technischer Fehler darf nicht durch automatische Neuanlage, Reset oder Überlagerung eines unbekannten Bestands umgangen werden.

## Veröffentlichungsgrenze

Ein technisch erfolgreicher Auslieferungsweg veröffentlicht nicht eigenmächtig. Öffentliche Domainumschaltung, Indexierung, reale Dienstkonten und produktive Datenverarbeitung folgen dem tatsächlich autorisierten Auftrag und [Governance](governance.md). Deploymentkonfiguration darf die gemeinsame Dev-Container-Konfiguration und deren Portregeln nicht erweitern.
