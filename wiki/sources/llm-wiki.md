---
type: Source Summary
title: LLM Wiki nach Andrej Karpathy
description: Konzeptquelle für dauerhaft verdichtetes, verknüpftes und durch ein LLM gepflegtes Wissen.
resource: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
tags:
- source
- wiki
status: stable
scope: wiki
sources:
- id: karpathy
  resource: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  title: LLM Wiki
  author: human:karpathy
source_observed_at: '2026-09-14T21:53:38Z'
source_sha256: dc3efe98ae62f23dd08acad13aba2e95287beb20b6bec2f4af0423557fe37401
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# LLM Wiki nach Andrej Karpathy

Karpathy beschreibt eine Wissensbasis, in der ein LLM Quellen zu dauerhaftem, verknüpftem Wissen verarbeitet. Unveränderte Originale, gepflegte Wiki-Seiten und ein Struktur-/Arbeitsvertrag haben eigene Aufgaben. Quellenaufnahme, belegte Antworten und Konsistenzprüfung entwickeln das Wiki weiter; Index und Log unterstützen Orientierung und Pflege.[^karpathy]

## Anwendung in diesem Repository

Der [lokale Pflegevertrag](../schema.md) setzt das Muster mit vollständigen Regeln, Projektwissen, [Themensynthesen](../concepts/index.md) und Quellenzusammenfassungen um. Die [Ausgangstexte](repository-baseline.md) bleiben durch Git adressierbar. Der Nutzer kuratiert Auftrag und Quellen; die zuständigen Rollen pflegen daraus belegtes Wissen. Schreibrechte folgen weiterhin den Rollenverträgen.

Das Konzept legt kein verbindliches Dateischema fest. Dafür gilt die vom Nutzer gewählte [OKF-Spezifikation](open-knowledge-format.md). Zusätzliche Suchdienste oder Obsidian sind für dieses Repository nicht eingerichtet.

## Fassung und Grenze

`source_observed_at` bezeichnet den Abruf dieser veränderlichen Gist-Fassung; `source_sha256` den SHA-256 des UTF-8-Texts vom Raw-Endpunkt. Ein Fingerprint belegt den gelesenen Inhalt, garantiert aber nicht dessen spätere Abrufbarkeit. Bei einer konzeptionellen Änderung die dann aktuelle Quelle gezielt abgleichen. Diese Zusammenfassung behauptet weder eine Produktimplementierung noch eine unabhängige Inhaltsprüfung.

[^karpathy]: [Andrej Karpathy: LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
