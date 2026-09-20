---
type: "Concept"
title: "wow-voiceover im Zusammenhang"
description: "Verbindet Produktarchitektur, Rollenprozess und die belegte Entwicklungsumgebung."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: architecture
    resource: "project/architecture.md"
  - id: environment
    resource: "project/local-development.md"
  - id: process
    resource: "standards/development-process.md"
  - id: adoption
    resource: "sources/repository-baseline.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# wow-voiceover im Zusammenhang

**wow-voiceover** erzeugt vertonte WoW-Dialoge und spielt sie als Addon ab. Die [Python-Generierung](project/architecture.md) liest MySQL-/VMaNGOS-Daten, ordnet NPC-Stimmen zu und ruft den getrennten TTS-Dienst auf. Das Vanilla-Datenmodul verbindet erzeugte Audiodateien und Lua-Lookups mit dem Player. Das [Benutzerhandbuch](project/user-manual.md) erklärt Einstieg und Bedienung.

## Von einer Änderung zum dokumentierten Bestand

Der aus der Vorlage übernommene Orchestrator koordiniert ausdrücklich beauftragte Entwicklungsgoals im Hauptchat. Sechs Fachrollen liefern ihre Beiträge seriell: Product Owner, UX Designer, Tech Lead, Software Developer, Documentation Writer und Code Reviewer. Eine Story enthält Plan, Code, Tests und Dokumentation in einem PR. [Storyabschluss](concepts/story-delivery.md) erklärt das Zusammenspiel; [Entwicklungsprozess](standards/development-process.md) und [GitHub-Einrichtung](project/github-workflow.md) sind die maßgeblichen Detailseiten.

Direkte Analyse und ausdrücklich beauftragte Vorlagen-/Wikipflege bleiben direkte Aufträge. Es entstehen daraus keine künstlichen Tickets oder automatischen Goals.

## Tatsächliche Arbeitsumgebung

Der vorhandene Python-3.10-Devcontainer und sein Benutzer-Volume bleiben Grundlage. Er enthält kein Docker-in-Docker und startet weder MySQL noch TTS. MySQL wird über die bestehende Compose-Datei am Host gestartet; der TTS-Server wird separat betrieben. Feste Dienstadressen verhindern derzeit eine allein durch `.env` konfigurierbare Verbindung aus dem Container. [Projektentwicklung](project/local-development.md) beschreibt Befehle, Seiteneffekte und Prüfgrenzen.

Die optionale Signal-Bridge der Vorlage ist nicht integriert. [Umgebungssynthese](concepts/development-environment.md) und [Übernahmegrundlage](sources/repository-baseline.md) erklären diese bewusste Anpassung an den Bestand.

## Wissen und Evidenz

[Standards](standards/index.md) definieren Verfahren. [Projektseiten](project/index.md) dokumentieren Code, Konfiguration und Bedienung. GitHub enthält aktives Backlog, Release-Zuordnung und Status. Ein historischer Plan, vorhandene Client-TOCs oder ein erfolgreicher Syntaxcheck belegen keine funktionierende Retail-Unterstützung oder End-to-End-Generierung.

Neue Erkenntnisse werden nach dem [Wiki-Schema](schema.md) in Detailseiten, Quellen und abhängigen Synthesen fortgeschrieben. [Nachweise und Freigaben](concepts/evidence-and-publication.md) sowie [Qualität und Pflege](concepts/quality-and-maintenance.md) verbinden diese Regeln mit dem täglichen Änderungsprozess.
