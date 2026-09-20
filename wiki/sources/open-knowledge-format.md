---
type: Source Summary
title: Open Knowledge Format 0.2
description: Geprüfte Formatgrundlage für Wissensseiten, Quellenmetadaten, Indizes und Änderungslogs.
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
tags:
- source
- okf
- schema
status: stable
scope: wiki
sources:
- id: spec
  resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/62432a095456147ee71e70ac6e4dc0d2dea3ac30/okf/SPEC.md
  title: Open Knowledge Format (OKF), Version 0.2
source_observed_at: '2026-09-14T21:54:55Z'
source_revision: 62432a095456147ee71e70ac6e4dc0d2dea3ac30
source_sha256: 26aa5da029278939f914e578107242d9607d4f2dc5fe153272b82f9ed1030101
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# Open Knowledge Format 0.2

OKF beschreibt ein portables Markdown-Bundle. Typisierte Wissensseiten besitzen YAML-Metadaten; Quellen, Bearbeitung, Prüfung und Lebenszyklus lassen sich getrennt erfassen. Die reservierten Index- und Logdateien dienen Navigation und Änderungshistorie.[^spec]

## Festgelegte Anwendung

Das Bundle beginnt bei `wiki/`. Der [Hauptindex](../index.md) deklariert Version 0.2, der [Pflegevertrag](../schema.md#seitenformat) konkretisiert die lokale Typauswahl und Metadatenpflege. Relative Links erhalten die direkte Lesbarkeit im Repository. Fachliche Freigaben folgen der [Governance](../standards/governance.md).

## Fassung und Grenze

Die festgehaltene Revision wurde mit der am Abrufzeitpunkt über `main` ausgelieferten Spezifikation bytegleich abgeglichen. `source_sha256` bezeichnet den Raw-Dateiinhalt. Spätere Formatänderungen werden bewusst übernommen; eine veränderliche URL aktualisiert das Bundle nicht automatisch. Die Nutzung von OKF bestätigt keine fachliche Richtigkeit der aufgenommenen Inhalte.

[^spec]: [GoogleCloudPlatform/knowledge-catalog: OKF 0.2, feste Revision](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/62432a095456147ee71e70ac6e4dc0d2dea3ac30/okf/SPEC.md).
