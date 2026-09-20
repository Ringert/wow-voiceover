---
type: "Project Context"
title: "Content und Informationsarchitektur"
description: "Sprachen, Dialogquellen und die Navigation im Projektwissen."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: cli
    resource: "../../cli-main.py"
  - id: data
    resource: "../../tts_cli/sql_queries.py"
  - id: processor
    resource: "../../tts_cli/tts_cloning.py"
  - id: wiki
    resource: "../schema.md"
  - id: history
    resource: "../../RETAIL-PLAN.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Content und Informationsarchitektur

## Inhalte und Sprache

Das Produkt verarbeitet Quest-/Gossiptexte, NPC-Namen, Referenzstimmen und erzeugtes Audio. SQL-Daten und Display-Metadaten sind die fachliche Eingabe; die Voice-Map enthält die konkrete Sprecherzuordnung. Ursprungstext und sprechbarer Text erfüllen unterschiedliche Zwecke, siehe [Fachmodell](domain-model.md).

Die CLI verwendet standardmäßig `deDE`; mehrere Locales sind im Parser vorhanden. Die tatsächliche Syntheseanfrage ist derzeit deutsch. Textänderungen beeinflussen gegebenenfalls Gossip-Schlüssel und bestehende Audiodateien. Übersetzungs- oder Audioabdeckung wird nicht aus der Liste unterstützter Locale-Codes abgeleitet.

Neue Projektwiki-Inhalte werden deutsch verfasst. Bestehende englische Codebezeichner, Addon-Beschriftungen und CLI-Kommandos werden präzise referenziert. Nicht belegte Menschen-, Geschäfts- oder Rechteangaben bleiben offen.

## Navigation und maßgebliche Dokumentation

- [README](../../README.md) bleibt der Einstieg mit Verweisen ins Wiki und der älteren ausführlichen Setupanleitung.
- [Wiki-Überblick](../overview.md) verbindet Produkt und Prozess; [Projektindex](index.md) führt zu den Detailseiten.
- [Entwicklungsanleitung](local-development.md) dokumentiert tatsächlich vorhandene Befehle und bekannte Infrastrukturgrenzen.
- [Benutzerhandbuch](user-manual.md) erklärt Spieler- und Audiobearbeitungsaufgaben.
- [Standards](../standards/index.md) enthalten gemeinsame Regeln; [Quellen](../sources/index.md) erklären Herkunft und Aussagegrenzen.

Das Wiki ist Markdown im Hauptrepository. Es benötigt keinen Webserver und ist kein separat synchronisiertes GitHub-Wiki-Repository. [RETAIL-PLAN.md](../../RETAIL-PLAN.md) bleibt als historische Quelle erhalten, wird aber nicht als laufende Roadmap fortgeschrieben. Aktive Planung gehört nach GitHub.

## Quellenpflege

Neue Erkenntnisse anhand der maßgeblichen Code-/Konfigurationsdatei in die betroffene Seite integrieren und abhängige Synthesen/Links nachführen. Kein vollständiges JSON-Dataset, keine Audiosammlung und keine privaten Sprachsamples als Dokumentation duplizieren. Herkunft und Verwendungsrechte des jeweiligen Materials bleiben unabhängig von seiner technischen Lesbarkeit.
