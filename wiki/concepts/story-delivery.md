---
type: Concept
title: Eine Story vollständig abschließen
description: Verbindet fachliche Klärung, Rollenbeiträge, gemeinsamen PR und belastbaren Integrationsnachweis.
tags: [delivery, roles, documentation]
status: stable
scope: shared
sources:
  - id: process
    resource: ../standards/development-process.md
  - id: orchestration
    resource: ../standards/orchestrator.md
  - id: documentation
    resource: ../standards/documentation.md
generated:
  by: codex/gpt-6
  at: 2026-09-14T21:56:25Z
---
# Eine Story vollständig abschließen

Der [Entwicklungsprozess](../standards/development-process.md#ablauf-einer-story) bündelt alle Beiträge in einer Story und genau einem PR. Technische Schritte stehen im Storytext. Ein Epic und darin eine Story sind gleichzeitig in Umsetzung; auch lesende Facharbeit bleibt seriell. Der [Orchestrator](../standards/orchestrator.md) koordiniert im Hauptchat und ersetzt keine Fachrolle.

| Beitrag | Verantwortliche Rolle | Ergebnis für den nächsten Schritt |
| --- | --- | --- |
| Fachlichkeit | [Product Owner](../standards/product-owner.md) | Nutzen, Scope, Akzeptanz, UI-Relevanz und tatsächliche Voraussetzungen |
| Gestaltung bei UI-Relevanz | [UX Designer](../standards/ux-designer.md) | Entschiedene Nutzerführung und geeignete, erforderlichenfalls visuell geprüfte Entwürfe |
| Technik | [Tech Lead](../standards/tech-lead.md) | Lösung am realen Bestand, begründete Grenzen, ausführbarer Plan und notwendige Nachweise |
| Umsetzung | [Software Developer](../standards/software-developer.md) | Vollständiger Code, sinnvolle Testpflege, Prüfevidenz und erstellter Story-PR |
| Wissenspflege | [Documentation Writer](../standards/documentation.md) | Technische Bestandsdokumentation und Benutzerhandbuch im selben PR |
| Unabhängige Prüfung | [Code Reviewer](../standards/code-review.md) | Anforderungsabgleich für den aktuellen vollständigen PR-Head |
| Integration | [Orchestrator](../standards/orchestrator.md) | Belegter gemeinsamer Merge und Abschluss des tatsächlich beauftragten Scopes |

Geeignete frühere Beiträge bleiben verwendbar, solange ihre Grundlagen passen. Eine Wiederaufnahme beginnt am ersten offenen oder ungültigen Ergebnis. Fachliche, gestalterische und technische Entscheidungen bleiben bei ihren zuständigen Rollen; lokale Implementierungsdetails liegen beim Developer.

## Wann ist der Beitrag integriert?

Ein erstellter PR belegt keine unabhängige Freigabe; ein Rollenmarker belegt keinen Merge. Vor Integration müssen aktueller Head, Review, erforderliche Checks und Developer-Evidenz denselben Gesamtstand tragen. Technische Dokumentation und Handbuch werden jeweils geprüft. Bei einem reinen Dokumentationsdelta kann unveränderte Codeevidenz gemäß [Merge-Vertrag](../standards/development-process.md#merge-nachweise) weitergelten.

Die Epic-Akzeptanz betrachtet zusätzlich das Zusammenspiel seiner Stories. Ein Storyziel umfasst keine Geschwister, ein Epicziel keinen vollständigen Release. [Nachweise und Veröffentlichung](evidence-and-publication.md) erklären die anschließenden Aussagegrenzen. Dauerhaftes Ergebniswissen fließt nach dem [Wiki-Pflegevertrag](../schema.md) zurück; Planung und Lieferstatus bleiben in GitHub.
