---
type: "Source Summary"
title: "Übernahme der Codex-Projektvorlage"
description: "Fixiert die gelesene Vorlage und die bewussten Anpassungen an das vorhandene Projekt."
tags: ["wiki", "wow-voiceover"]
status: "stable"
scope: "wiki"
sources:
  - id: template
    resource: "https://github.com/Ringert/Codex-Projektvorlage/tree/b001e1b700d75aa0f31f6ced84381ba194b79582"
  - id: project
    resource: "wow-voiceover-codebase.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Übernahme der Codex-Projektvorlage

## Herkunft und Fassung

Die Quelle ist [Ringert/Codex-Projektvorlage](https://github.com/Ringert/Codex-Projektvorlage), gelesen am **20. September 2026** über einen separaten Git-Checkout. Übernommener Stand: [`b001e1b700d75aa0f31f6ced84381ba194b79582`](https://github.com/Ringert/Codex-Projektvorlage/tree/b001e1b700d75aa0f31f6ced84381ba194b79582). Die Originale bleiben über diese feste Revision abrufbar. Ein später geänderter Vorlagen-HEAD ändert die hiesigen Regeln nicht automatisch.

Die gemeinsame Wiki-Struktur folgt den von der Vorlage mitgelieferten [LLM-Wiki-](llm-wiki.md) und [OKF-Quellen](open-knowledge-format.md). Deren ältere Quellen- und Prüfvermerke beschreiben die Vorlagenarbeit; sie behaupten keine erneute unabhängige Prüfung dieses Projekts. Historische Quellenlinks auf `c183c509.../documentation/` in unveränderten Standards bleiben Herkunftsbelege der ursprünglichen Wiki-Migration.

## Übernahme und Anpassung

| Vorlagenbereich | Verwendung in wow-voiceover |
| --- | --- |
| `AGENTS.md` | Ladematrix, Wissenspflege, serieller Rollenprozess und Nachweisregeln; ergänzt um konkrete Python-/Lua-Grenzen |
| `.codex/agents/*.toml` | Sieben Rollen mit unveränderten Modellen, Reasoning und Schreibgrenzen |
| `.codex/config.toml` | Goal-/Agenteneinstellungen und sechs wiederverwendbare Fachrollenthreads; kein nicht verfügbarer Signal-MCP-Server |
| `wiki/standards/` | Rollen, Governance, Engineering, Tests, Dokumentation und weitere gemeinsame Regeln; Branch-, Arbeitsumgebungs- und Signalannahmen ausdrücklich angepasst |
| `wiki/schema.md`, `wiki/concepts/`, Indizes | OKF-Format, Ingest/Query/Lint und zusammenhängende Wissenspflege; Synthesen auf das konkrete Projekt bezogen |
| `wiki/project/` | Offene Vorlagenfelder durch quellengestützte Projektseiten ersetzt; tatsächlich ungeklärte Verantwortungs-/Betriebsfragen bleiben markiert |
| PR-Vorlage und Issue-Workflows | Ein Story-PR mit Code, Tests und Dokumentation; Default-Branch dynamisch statt fest `main`, Fallbackkürzel `WOWVO` |
| Workflowtests | Vorhandene PR-Tests übernommen und an Branchkonvention angepasst; Branch-Erzeugung und Default-Branch-Verhalten gezielt abgesichert |
| Devcontainer / Compose | Bestehende Python-Basis und MySQL-Datei erhalten; kein Debian-/DinD-Austausch, kein neutraler `app`-Platzhalter |
| Signal-Werkzeug / Skill | Nicht installiert und nicht aktiviert; optionale Quelle im [Signal-Standard](../standards/signal-integration.md) referenziert |
| Persönlicher Zustand / Skillcache | Keine Kopie aus der Vorlage oder anderen Projekten |

Die bestehende README behält ihren Inhalt und den vorhandenen Devcontainer-Einstieg; Wiki-Verweise und belegte CLI-Korrekturen ergänzen sie. Produktcode, JSON-/Audiodaten, bestehender Releasejob, Abhängigkeiten und persönliche Konten werden durch diese Übernahme nicht geändert.

## Projektquelle und Aussagegrenzen

[Codebasis und Eingangszustand](wow-voiceover-codebase.md) erklärt den getrennten Projektbeleg. Ein kopierter Standard, valides TOML oder ein bestandener lokaler Test belegt keine tatsächlich sichtbare Agentenauswahl, erfolgreich ausgeführte GitHub-Automatik, funktionierende TTS-Verbindung oder Ingame-Kompatibilität. Die Übernahme erzeugt keine Releases, Nachrichten, Roadmap oder vorgetäuschte Bestandsfreigabe.

Die [GitHub-Seite](../project/github-workflow.md) beschreibt Einrichtung und Updateverfahren. Gemeinsame Regeln und konkreter Projektbestand bleiben getrennt; Projektseiten nicht beim nächsten Vorlagenupdate überschreiben.
