---
type: "Concept"
title: "Arbeitsumgebung und Projektbetrieb"
description: "Verbindet vorhandenen Python-Container, getrennte Dienste und bewusste Werkzeugausführung."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: environment
    resource: "../standards/local-development.md"
  - id: project
    resource: "../project/local-development.md"
  - id: signal
    resource: "../standards/signal-integration.md"
  - id: adoption
    resource: "../sources/repository-baseline.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T08:35:43Z
---
# Arbeitsumgebung und Projektbetrieb

Die [lokale Entwicklungsregel](../standards/local-development.md) trennt feste Arbeitsbasis und Produktbetrieb. Hier ist die Arbeitsbasis der vorhandene Python-3.10-Devcontainer. Er enthält Projektbibliotheken und Entwicklungswerkzeuge, aber kein Docker-in-Docker. Synthese und Modellbetrieb finden ausschließlich im separaten TTS-Webservice statt; die Arbeitsumgebung benötigt dafür weder Modellbibliotheken noch GPU-Konfiguration. Die [Projektanleitung](../project/local-development.md) ist für konkrete Pfade und Befehle maßgeblich.

## Start und Zugriff

Das Öffnen des Containers startet weder MySQL noch TTS oder Audiogenerierung. `docker compose up -d` wird auf dem Host aus dem Checkout ausgeführt und startet ausschließlich MySQL. Der bestehende Port 3306 und feste Containername sind dokumentierter Altbestand. Neue Dienste folgen den gemeinsamen Port-/Restart-Grenzen.

Die TTS-Adresse ist über `.env` konfigurierbar; die MySQL-Adresse bleibt fest codiert. Deshalb ist die manuell gestartete Datenbank am Host nicht automatisch aus dem Arbeitscontainer erreichbar. Ein Konfigurationsfile oder installiertes Paket belegt keine funktionierende Ende-zu-Ende-Kette. Reale Verbindung und Generierung erhalten eigene Nachweise.

## Werkzeuge und Zustand

Nur Codex-Login-Port 1455 ist fest weitergeleitet. Home-Volume und MySQL-Volume halten unterschiedliche Zustände; Persistenz ist kein Backup. Persönliche Anmeldungen verbleiben außerhalb des Checkouts. Rebuild, Kontozugang und tatsächliche Editorfunktion sind getrennte Prüfgegenstände.

Der [Skill-Standard](../standards/skills.md) fordert konkrete Abdeckung statt vorsorglicher Installationen. Für Workflowtests wird bei Bedarf Node.js in der laufenden Umgebung genutzt; das macht Node nicht zum Produktstack. Produktprüfungen benötigen die jeweils passenden Python-/MySQL-/WoW-Komponenten.

Die [Signal-Integration](../standards/signal-integration.md) ist nicht eingerichtet. Der Chat bleibt der Kommunikationsweg. [Übernahmegrundlage](../sources/repository-baseline.md) erklärt, warum Container- und Signal-Infrastruktur der Vorlage nicht als Projektbestand kopiert wurden.
