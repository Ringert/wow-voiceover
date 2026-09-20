---
type: "Project Context"
title: "UI-Leitfaden des Projekts"
description: "Vorhandene WoW-Bedienelemente und Regeln für Änderungen an Addon und CLI."
tags: ["project", "wow-voiceover"]
status: "stable"
scope: "project"
sources:
  - id: options
    resource: "../../AI_VoiceOver/Options.lua"
  - id: queue
    resource: "../../AI_VoiceOver/SoundQueueUI.lua"
  - id: overlay
    resource: "../../AI_VoiceOver/QuestOverlayUI.lua"
  - id: cli
    resource: "../../cli-main.py"
  - id: zone
    resource: "../../tts_cli/zone_selector.py"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# UI-Leitfaden des Projekts

## Bestehende Oberflächen

Die sichtbare Produktoberfläche ist das WoW-Addon, keine Website. [Options.lua](../../AI_VoiceOver/Options.lua) definiert AceConfig-Optionen mit englischen Beschriftungen. [SoundQueueUI.lua](../../AI_VoiceOver/SoundQueueUI.lua) zeigt die Warteschlange und NPC-Porträts; [QuestOverlayUI.lua](../../AI_VoiceOver/QuestOverlayUI.lua) ergänzt die Questdarstellung. Der Minimapbutton ist über LibDataBroker/LibDBIcon eingebunden.

Vorhandene Nutzerkonzepte sind Play/Pause, Überspringen, Queue leeren, Audiooptionen, Datenmodule und Profile. Standardbelegung und Einstellungsfolgen stehen im [Benutzerhandbuch](user-manual.md#im-spiel-hören-und-steuern). Layout und Verhalten hängen auch vom Client ab; Legacy-Möglichkeiten nicht mit modernen APIs gleichsetzen.

## Gestaltungsregeln für Änderungen

- Bestehende WoW-/AceConfig-Muster und verständliche Beschriftungen weiterverwenden. Keine Web-Tokens oder ein zweites Designsystem aus der Vorlage erfinden.
- Queuezustand, Pause und fehlende Audiodaten nachvollziehbar darstellen. Neue Fehlerfälle anhand des tatsächlichen Spielablaufs prüfen.
- Skalierung, Verschiebbarkeit, Sichtbarkeit und Profile berücksichtigen; keine ungeprüften Resets gespeicherter Einstellungen.
- Eine UI-relevante Story erhält die nötige UX-Grundlage vor der Implementierung. Ein Mockup ersetzt keine Sichtprüfung der implementierten WoW-Oberfläche.
- Bedienbarkeit und Lesbarkeit im konkreten Client prüfen. Eine belegte vollständige Accessibility-Konformität liegt nicht vor.

## CLI und Hilfswerkzeuge

Die Haupt-CLI nutzt `argparse` und Konsolenausgaben. `interactive` startet im aktuellen Code eine Batchverarbeitung aller abgefragten Dialoge. Der Name allein darf in Hilfetexten nicht als Auswahl-/Bestätigungsdialog beschrieben werden. Änderungen an Befehlen müssen Seiteneffekte, globale Optionsposition und Ausgabeort verständlich machen.

`zone_selector.py` enthält eine Matplotlib-Zonenauswahl, ist aber kein Nachweis eines aktiven Auswahlpfads von `cli-main.py interactive`. Playwright dient einem Download-Hilfswerkzeug; seine Installation macht aus dem Produkt keine Webanwendung.
