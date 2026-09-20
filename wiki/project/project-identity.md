---
type: "Project Context"
title: "Projektidentität"
description: "Repository, Produktname, Branchkonvention und belegte Verantwortungsgrenzen."
tags: ["project", "wow-voiceover"]
status: "draft"
scope: "project"
sources:
  - id: repository
    resource: "https://github.com/Ringert/wow-voiceover"
  - id: cli
    resource: "../../cli-main.py"
  - id: addon
    resource: "../../AI_VoiceOver/AI_VoiceOver_Vanilla.toc"
  - id: license
    resource: "../../LICENSE"
  - id: adoption
    resource: "../sources/repository-baseline.md"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Projektidentität

| Merkmal | Bestand und Geltungsgrenze |
| --- | --- |
| Projekt | `wow-voiceover`; Addon-Anzeigename **VoiceOver** |
| Repository | [Ringert/wow-voiceover](https://github.com/Ringert/wow-voiceover), bestehender Fork |
| Upstream-Herkunft | Die bisherige README und Release-Dateien verweisen auf `mrthinger/wow-voiceover`; diese Links sind keine Release-Nachweise dieses Forks. |
| Default-Branch | `master`, bei Übernahme über GitHub gelesen; die Workflows ermitteln ihn dynamisch. |
| Branchkürzel | `WOWVO`, lokaler Workflow-Default; `PROJECT_KEY` kann als Repository-Variable bewusst anders festgelegt werden. Branches: `issue/WOWVO-<story>`. |
| Produktbestand | Python-CLI zur Dialogvertonung, Lua-Player und Vanilla-Datenmodul; separates TTS-Backend. |
| Sprache | Wiki und gemeinsame Prozessregeln deutsch; bestehende README, Codebezeichner und Addon-Beschriftungen überwiegend englisch. CLI-Standardlocale `deDE`. |
| Code-Lizenz | Repository enthält [LICENSE](../../LICENSE) (Unlicense-Text); Abhängigkeiten und Audioquellen sind gesondert zu betrachten. |
| Verantwortung | Repository-Inhaber `Ringert`; konkrete fachliche, technische und Release-Verantwortliche: **To be defined**. Agentenrollen ersetzen keine bestätigten menschlichen Verantwortlichen. |

[Workflow](github-workflow.md) beschreibt die Arbeit im Fork. [Übernahmegrundlage](../sources/repository-baseline.md) hält die genaue Vorlagenrevision und die Anpassungen an den Bestand fest.
