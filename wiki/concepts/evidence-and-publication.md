---
type: Concept
title: Aussagen, Nachweise und Freigaben
description: Ordnet Quellenstatus, implementierten Bestand, Prüfungen und Veröffentlichung nach ihrer tatsächlichen Aussagekraft.
tags: [evidence, governance, publication]
status: stable
scope: shared
sources:
  - id: governance
    resource: ../standards/governance.md
  - id: documentation
    resource: ../standards/documentation.md
  - id: deployment
    resource: ../standards/deployment.md
  - id: security
    resource: ../standards/security-and-privacy.md
generated:
  by: codex/gpt-6
  at: 2026-09-14T21:56:25Z
---
# Aussagen, Nachweise und Freigaben

Eine Aussage wird mit Quelle, betrachteter Fassung und Geltungsgrenze gepflegt. Die [Governance](../standards/governance.md#inhalts--und-quellenstatus) unterscheidet Arbeitsentwurf, quellenbasierten Inhalt, Freigabe und gesperrten Inhalt. Eine Tatsachenfreigabe erlaubt nicht automatisch die Verwendung begleitender Bilder oder Logos. Private Originalnachweise bleiben außerhalb des Repositories.

| Vorliegender Nachweis | Tragfähige Aussage | Zusätzlich zu klären, falls benötigt |
| --- | --- | --- |
| Bestätigte fachliche oder technische Entscheidung | Vorgabe für die Umsetzung | Tatsächliche Implementierung und Prüfung |
| Mockup oder Simulation | Entwurf beziehungsweise ausdrücklich simuliertes Verhalten | Echte UI, Persistenz, Autorisierung und andere reale Grenzen |
| Erfolgreicher Test oder Build | Ergebnis des benannten Prüfwegs am geprüften Stand | Nicht geprüfte Integrationen, menschliche Bedienung und Betrieb |
| Gemeinsamer Merge | Integration des nachgewiesenen Standes | Tatsächliche Auslieferung und Verfügbarkeit |
| Erfolgreicher Compose-Start | Lokaler Start im betrachteten Setup | Öffentliche Bereitstellung und reale Datenverarbeitung |
| Wiki-Metadaten oder ein bestandener Formatcheck | Einordnung beziehungsweise strukturelle Korrektheit | Fachliche Bestätigung anhand der Quellen |

Das [Benutzerhandbuch](../project/user-manual.md) und die [Projektarchitektur](../project/architecture.md) beschreiben tatsächlichen Bestand. Geplante Fähigkeiten bleiben in GitHub; unbekannte Werte bleiben `To be defined`. Eine neu erzeugte Zusammenfassung hebt diese Grenze nicht auf.

## Auswirkungen auf die Arbeit

Zuständige Rollen entscheiden reversible Details im autorisierten Scope selbst. Fehlende nicht erfindbare Tatsachen halten nur die konkret davon abhängige Aktion auf. Bestehende Autorisierung bleibt gültig. Eine Veröffentlichung oder Verarbeitung realer Daten folgt den tatsächlich benötigten [Publikationsbedingungen](../standards/governance.md#technische-qualität-und-veröffentlichung) und dem [Betriebsvertrag](../standards/deployment.md).

[Sicherheits- und Datenregeln](../standards/security-and-privacy.md) gelten auch für Quellen, Beispiele und Logs. Entwicklung und Tests verwenden synthetische Daten. Bei widersprüchlichen Belegen erhält die betroffene Wiki-Seite beide Quellen und eine sichtbare offene Aussage gemäß [Pflegevertrag](../schema.md#quellen-aufnehmen--ingest); eine plausible Synthese ersetzt keine Klärung.
