---
type: "Reference"
title: "Projektreferenzen"
description: "Maßgebliche Quellen des Projektwissens mit ihren Aussagegrenzen."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: baseline
    resource: "../sources/wow-voiceover-codebase.md"
  - id: template
    resource: "../sources/repository-baseline.md"
  - id: schema
    resource: "../schema.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Projektreferenzen

| Quelle | Verwendung | Geltungsgrenze |
| --- | --- | --- |
| [Codebasis und Eingangszustand](../sources/wow-voiceover-codebase.md) | Ausgangsrevision und lokale Konfiguration | Codelektüre ist kein Dienst-/Ingame-Test |
| [Vorlagenübernahme](../sources/repository-baseline.md) | Rollen, Standards, Wiki und GitHub-Automatisierung | Vorlagenwerkzeuge belegen keinen Produktbestand |
| [CLI](../../cli-main.py), [Processor](../../tts_cli/tts_cloning.py), [SQL](../../tts_cli/sql_queries.py) | Tatsächliche Argumente, Datenfluss und Seiteneffekte | Serviceimplementierung liegt außerhalb dieses Repositories |
| [Addon](../../AI_VoiceOver/VoiceOver.lua), [Datenmodule](../../AI_VoiceOver/DataModules.lua) | Spielereignisse, Dateiauflösung und Wiedergabe | Keine Aussage über ungeprüfte aktuelle Clientversionen |
| [Devcontainer](../../.devcontainer/README.md), [Compose](../../docker-compose.yml) | Reproduzierbares lokales Setup und bekannte Netzwerkgrenzen | Konfiguration bestätigt keine persönliche Anmeldung oder laufenden Dienste |
| [Releaseworkflow](../../.github/workflows/release-player.yaml) | Vorhandener Tag-/Draft-Releasepfad | Feste Upstream-Links sind keine Releases des Forks |
| [RETAIL-PLAN.md](../../RETAIL-PLAN.md) | Historische Produktideen | Kein aktuelles Backlog und kein implementierter Zustand |
| [LICENSE](../../LICENSE) | Vorhandener Code-Lizenztext | Keine pauschale Lizenz für Spieltexte, Stimmen, Modelle und Drittbibliotheken |

Externe Ziele wie `lib-tts`, VMaNGOS, allvoice.ai und Community-Verweise sind aus dem Quellcode bekannt. Ihr aktueller Dienst-/Support-/Rechtestand wurde bei dieser Übernahme nicht vollständig untersucht. Bei einer davon abhängigen Änderung wird die passende aktuelle Primärquelle gezielt gelesen; die Quellenliste ist kein wiederkehrender Komplett-Rechercheauftrag.

Die [Wiki-Pflegeregeln](../schema.md) regeln Quellenstand, Metadaten, Querverweise und Widersprüche. Für konkrete Codeänderungen die betroffenen Quellen neu abgleichen; keine Datenbank- oder TTS-Befehle nur zur Erzeugung eines Dokumentationsprüfmarkers ausführen.
