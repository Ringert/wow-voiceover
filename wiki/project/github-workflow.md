---
type: "Playbook"
title: "GitHub-Workflow"
description: "Konkrete Einrichtung des übernommenen Storyprozesses im bestehenden master-Repository."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: process
    resource: "../standards/development-process.md"
  - id: config
    resource: "../../.codex/config.toml"
  - id: branch
    resource: "../../.github/workflows/link-issue-branch.yml"
  - id: pr
    resource: "../../.github/workflows/link-issue-pr.yml"
  - id: official-agents
    resource: "https://learn.chatgpt.com/docs/agent-configuration/subagents"
  - id: official-config
    resource: "https://learn.chatgpt.com/docs/config-file/config-reference"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# GitHub-Workflow

## Rollen und Arbeitsumfang

Die [sieben Agentenkonfigurationen](../../.codex/agents/) übernehmen Modelle, Reasoning und Befugnisse der Vorlage. Der Orchestrator arbeitet bei ausdrücklich beauftragten Entwicklungsgoals im Hauptchat; höchstens eine Fachrolle arbeitet gleichzeitig. Die sechs offenen Rollenthreads dienen der Wiederverwendung von Kontext, nicht sechs parallelen Aufträgen. Direkte Analyse, Dokumentations- und Vorlagenpflege bleiben im erteilten Scope.

Codex lädt projektlokale Rollen aus `.codex/agents/*.toml` und Einstellungen aus `.codex/config.toml` im vertrauten Projekt. Nach Übernahme die Codex-Sitzung bzw. den Client neu laden und die Rollenauswahl tatsächlich prüfen. Valides TOML allein belegt weder Erkennung noch Modellzugang. Die Konfiguration startet kein Goal und enthält keine Signal-MCP-Verbindung. Grundlage: [offizielle Rollendokumentation](https://learn.chatgpt.com/docs/agent-configuration/subagents) und [Konfigurationsreferenz](https://learn.chatgpt.com/docs/config-file/config-reference), abgerufen am 20. September 2026.

## GitHub-Struktur

| Element | Festlegung |
| --- | --- |
| Repository | `Ringert/wow-voiceover` |
| Integrationsbranch | Tatsächlicher Default-Branch, derzeit `master`; keine Umbenennung auf `main` nötig |
| Projektkürzel | `WOWVO` als Workflow-Fallback; optional bewusste Repository-Variable `PROJECT_KEY` |
| Storybranch | `issue/WOWVO-<issue-number>` bei Standardkürzel |
| Hierarchie | Release-Milestone; top-level Epic; Story als direktes natives Sub-Issue im selben Milestone |
| Labels | `type:roadmap`, `type:epic`, `type:story`, `implementation-ready` |
| Story-PR | Genau ein PR gegen den Default-Branch; `Closes #<story>` und `Refs #<parent-epic>` |
| Abschluss | Code, passende Tests und Dokumentation im selben PR, unabhängiges Review des aktuellen Heads, anschließend belegte Integration |

Die vollständigen Rollen- und Nachweisregeln stehen im [Entwicklungsprozess](../standards/development-process.md). Ein Issue als Text im PR ist noch kein Nachweis der nativen Development-Verknüpfung.

## Übernommene Automatisierung

[link-issue-branch.yml](../../.github/workflows/link-issue-branch.yml) reagiert auf `implementation-ready` oder einen manuellen Aufruf mit Storynummer. Es prüft offene Story, direkten Parent, gemeinsamen Milestone und bereits vorhandene Verknüpfungen. Es erstellt den Branch über `createLinkedBranch` am tatsächlichen Default-Branch und prüft die native Zuordnung. Ein bereits existierender unverbundener Branch wird als Fehler gemeldet. Rechte: `contents: write`, `issues: write`.

[link-issue-pr.yml](../../.github/workflows/link-issue-pr.yml) prüft PRs aus demselben Repository bei Öffnen, Wiederöffnen, Bearbeiten, neuem Head und Reviewbereitschaft. Es prüft Branchkürzel, genau eine Story-Schließreferenz, genau ein Parent-Epic, Zielbranch, gemeinsamen Milestone und native PR-Verknüpfung. Ein zweiter zugeordneter PR wird abgelehnt. Der Workflow hat nur Leserechte und führt keinen ausgecheckten PR-Code aus. Externe Fork-PRs werden von dieser Zuordnungsprüfung nicht erfasst.

Die [PR-Vorlage](../../.github/pull_request_template.md) enthält Ergebnis, relevante Prüfevidenz und beide Dokumentationsbereiche. Interne Rollenmarker gehören nicht in den PR-Text. Die Workflows erstellen weder Backlog noch Produktbuilds, Tests, Releases oder automatische Merges. Der bestehende Tag-Releaseworkflow bleibt separat.

## Einrichten und verwenden

1. Die Workflowdateien auf den Default-Branch übernehmen, damit insbesondere Issue- und manuelle Trigger verfügbar werden; Actions müssen im Repository zulässig sein.
2. Die vier oben genannten Labels anlegen bzw. vorhandene passende Labels verwenden. Bei gewolltem anderem Kürzel `PROJECT_KEY` unter **Settings → Secrets and variables → Actions → Variables** setzen, bevor Storybranches entstehen. Ohne Variable funktioniert `WOWVO`.
3. Milestone und fachliches Epic anlegen, Story als **natives Sub-Issue** zuordnen und beide in denselben Milestone legen. Links oder Checklisten allein ersetzen die Parent-Beziehung nicht.
4. Nach fachlicher und technischer Ausarbeitung `implementation-ready` setzen. Workflow-Ergebnis und Development-Verknüpfung prüfen, dann den erzeugten Branch verwenden.
5. Den Story-PR samt Dokumentation mit den beiden Referenzzeilen gegen `master` öffnen. Aktuelle Prüfung und unabhängiges Review abwarten; Branchschutz bleibt maßgeblich.

Die lokale Vorlagenübernahme ist keine Bestätigung bereits angelegter Labels, Repository-Variablen, Branchschutzregeln oder erfolgreich ausgeführter Actions. Sie benennt auch keine vorhandenen Issues als freigegeben. Ein direkt beauftragter Pflege-PR außerhalb des Storyschemas benötigt eine bewusste Einordnung: Der strenge Zuordnungsworkflow lehnt beliebige Branches im selben Repository ab. Keine Dummy-Story oder falsche Schließreferenz eintragen, um eine Prüfung zu umgehen.

## Prüfen und Vorlagenupdates übernehmen

```bash
node --test tools/github-workflows/test/*.test.mjs
```

Die Tests verwenden synthetische API-Antworten. Sie prüfen auch `master`, andere Default-Branchnamen, fehlende Default-Branches und bestehende Zuordnungen; sie erzeugen keine echten Issues, Branches oder PRs.

Für ein Vorlagenupdate die [festgehaltene Revision](../sources/repository-baseline.md) mit der gewünschten neuen Fassung vergleichen. Projektwiki, `master`-/`WOWVO`-Anpassung, bestehende Devcontainer-Basis und bewusste Nichtintegration von Signal erhalten. Geänderte Regeln samt Herkunft pflegen und Workflowtests erneut ausführen; kein blindes Überschreiben des Projektkontexts.
