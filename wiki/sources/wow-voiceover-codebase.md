---
type: "Source Summary"
title: "Codebasis und Eingangszustand"
description: "Belegt den gelesenen Projektstand und die Grenzen der daraus abgeleiteten Dokumentation."
tags: ["wiki", "wow-voiceover"]
status: "stable"
scope: "wiki"
sources:
  - id: baseline
    resource: "https://github.com/Ringert/wow-voiceover/tree/9f6883e265dbf2e0088cfbf133ed2486138c819a"
  - id: cli
    resource: "../../cli-main.py"
  - id: container
    resource: "../../.devcontainer/README.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Codebasis und Eingangszustand

## Untersuchte Fassung

Untersucht wurde `Ringert/wow-voiceover` im lokalen Checkout. Ausgangscommit: [`9f6883e265dbf2e0088cfbf133ed2486138c819a`](https://github.com/Ringert/wow-voiceover/tree/9f6883e265dbf2e0088cfbf133ed2486138c819a) (`fix file naming`, 2. Februar 2026). GitHub meldete bei der Übernahme am 20. September 2026 `master` als Default-Branch.

Zum Eingangszustand gehörten lokale Änderungen an `README.md` und `requirements.txt` sowie die vorhandenen, noch nicht im Ausgangscommit enthaltenen `.devcontainer/`-Dateien. Diese Dateien wurden als lokale Quelle gelesen und bewahrt. Die aktuellen relativen Links im Wiki beziehen sich auf den Arbeitsstand mit diesen Dateien, nicht auf eine Behauptung, sie seien im genannten historischen Commit enthalten.

## Tatsächlich ausgewertete Quellen

| Quelle | Aufgenommenes Wissen |
| --- | --- |
| [cli-main.py](../../cli-main.py) | Modi, globale Argumente, Defaultverhalten und Reihenfolge |
| [tts_cli](../../tts_cli/) | SQL-Export, Stimmenzuordnung, Textvarianten, Synthesevertrag, Hashes, Lookups, Datenimport und Locale-Abbildung |
| [AI_VoiceOver](../../AI_VoiceOver/) | Addonereignisse, Queue, Optionen, Datenmodulvertrag, TOCs und Kompatibilitätsstruktur |
| [Vanilla-Modul](../../AI_VoiceOverData_Vanilla/Module.lua) und [TOC](../../AI_VoiceOverData_Vanilla/AI_VoiceOverData_Vanilla.toc) | Registrierung, erwartete Dateien und Audiopfade |
| [Compose](../../docker-compose.yml), [Env-Werte](../../tts_cli/env_vars.py), [Anforderungen](../../requirements.txt) | Tatsächliche Dienste, feste Adressen, Abhängigkeiten |
| [Devcontaineranleitung](../../.devcontainer/README.md) und [Konfiguration](../../.devcontainer/devcontainer.json) | Python-Arbeitsumgebung, Persistenz, Login-Weiterleitung und fehlende automatische Dienstintegration |
| [Releaseworkflow](../../.github/workflows/release-player.yaml), [README](../../README.md), [historischer Plan](../../RETAIL-PLAN.md) | Vorhandene Paketerstellung, ältere Anleitungen und Abgrenzung geplanter Fähigkeiten |

## Widersprüche und Grenzen

Die älteren README-Beispiele setzten `--lang` hinter den Unterbefehl und beschrieben `gen_lookup_tables` teilweise als Audiogenerierung. Der tatsächliche Parser und Aufrufpfad sind maßgeblich; Einstieg und Wiki wurden entsprechend korrigiert.

`.env.example` beschreibt MySQL-Werte, die `env_vars.py` nicht ausliest. Locale-Unterstützung im Parser stimmt nicht mit der fest deutschen HTTP-Synthese überein. Mehrere Client-TOCs und der Retail-Plan belegen keine heutige Retail-Funktion. Diese Unterschiede stehen bei [Entwicklung](../project/local-development.md), [Architektur](../project/architecture.md) und [Fachmodell](../project/domain-model.md).

Es wurden keine Datenbanken initialisiert, vollständigen Audiojobs ausgeführt, privaten Konten kopiert oder WoW-Clients gestartet. Die Dokumentation des TTS-Servers außerhalb dieses Checkouts wurde nicht als geprüfte Implementierung ausgegeben. Die Source Summary belegt Herkunft und Quellcodeabgleich; sie ist kein unabhängiges Produktreview oder Release-Zertifikat.
