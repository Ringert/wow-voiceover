---
type: Concept
title: Qualität durch Code-, Test- und Wissenspflege
description: Verbindet risikogerechte Tests, verständliche technische Entscheidungen und aktuelle Dokumentation im selben Lieferumfang.
tags: [quality, testing, maintenance]
status: stable
scope: shared
sources:
  - id: engineering
    resource: ../standards/engineering-principles.md
  - id: testing
    resource: ../standards/testing.md
  - id: documentation
    resource: ../standards/documentation.md
  - id: review
    resource: ../standards/code-review.md
generated:
  by: codex/gpt-6
  at: 2026-09-14T21:56:25Z
---
# Qualität durch Code-, Test- und Wissenspflege

Die [Engineering-Prinzipien](../standards/engineering-principles.md) verlangen eine einfache vollständige Lösung für den aktuellen Bedarf. Zuständigkeiten, Schnittstellen und maßgebliche Informationsquellen bleiben erkennbar. Abstraktionen und zusätzliche Infrastruktur benötigen konkreten Nutzen. Ein Qualitätsziel schreibt kein neues Werkzeug vor.

## Absichern, was sich ändern kann

Der Tech Lead ordnet reale Änderungsrisiken geeigneten Nachweisen zu. Der Developer pflegt die dazugehörigen Tests im selben Implementierungsauftrag. Die [Testpyramide](../standards/testing.md) bevorzugt viele schnelle Unit-Tests, gezielte Integrationstests und sehr wenige E2E-Tests für zentrale Nutzerwege mit zusätzlicher Aussage. Entscheidend ist die niedrigste Ebene, die das Risiko erkennt.

Vorhandene Tests bleiben erhalten, wenn ihr Schutz passt. Sie werden bei echten Lücken ergänzt und bei entfallenem oder gleichwertig günstiger abgesichertem Verhalten sinnvoll entfernt. Zeit, Zufall, Daten und externe Antworten werden für reproduzierbare Tests kontrolliert. Ein Fehler wird geklärt; wiederholtes Ausführen bis zum Erfolg ersetzt keine Korrektur.

## Wissen ist Teil der Lieferung

Der [Dokumentationsvertrag](../standards/documentation.md) verbindet zwei Leserbedarfe: technische Zusammenhänge für Entwickler, Betreiber und Tester sowie reale Nutzeraufgaben im Handbuch. Der Writer pflegt den tatsächlichen Bestand im Story-PR anhand bestätigter Entscheidungen. Ein fehlender Einfluss auf einen Bereich kann begründet ohne Textänderung bestätigt werden.

Das [unabhängige Review](../standards/code-review.md) prüft den aktuellen gesamten PR gegen vereinbarte Anforderungen und betroffene Verträge. Substanzielle Dokumentationslücken gehören in denselben Reviewauftrag. Format-, Link- und Quellenabgleich sichern Wiki-Änderungen; Wortlauttests liefern dafür keinen zusätzlichen Schutz.

## Pflege ohne zusätzliche Prozessrunde

Geänderte Funktionen und Konzepte werden mit ihrer Story dokumentiert. Beim Epic-Abschluss wird der vollständige Zusammenhang möglichst im letzten Story-PR geprüft. Konkrete Widersprüche oder wiederkehrende Verständnisprobleme lösen gezielte Pflege aus. Geeignete bestehende Evidenz wird weiterverwendet.

Im [LLM Wiki](../schema.md) umfasst diese Pflege auch direkt betroffene Zusammenfassungen, Querverweise und Quellen. Die [Nachweissynthese](evidence-and-publication.md) hält Prüfungen, Bestandsaussagen und Veröffentlichung auseinander. Tests, Lint und Quellenaufnahme erzeugen keinen automatischen Containerstart oder neuen Auslieferungsweg.
