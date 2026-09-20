---
type: Policy
title: Entwicklungsprozess und Rollen
description: Planungshierarchie, Orchestrator und sechs Fachrollen, vollständiger Storyauftrag, serielle Übergaben und ein
  PR für Code, Tests und Dokumentation.
tags:
- shared
- development-process
status: stable
scope: shared
sources:
- id: template-adoption
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/b001e1b700d75aa0f31f6ced84381ba194b79582/wiki/standards/development-process.md
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/development-process.md
  title: 'Vorlage vor der Wiki-Migration: standards/development-process.md'
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Entwicklungsprozess und Rollen

GitHub ist die einzige Quelle für Roadmap, Release-Zuordnung, Priorität, Abhängigkeiten, Status und Ticketchronik. Dieser Vertrag definiert die Storyschleife. Autorisierung, externe Freigaben und die Grenze zwischen Planung und Bestandsdokumentation stehen in [Governance](governance.md).

## Planungshierarchie

| Ebene | GitHub-Repräsentation | Zweck |
| --- | --- | --- |
| Release | Milestone | Gemeinsames messbares Release-Ziel |
| Roadmap | Top-level Issue mit `type:roadmap` | Geordneter Überblick; kein Parent der Epics |
| Epic | Top-level Issue mit `type:epic` und Milestone | Zusammengehöriges Feature mit Nutzerergebnis und Gesamtakzeptanz |
| Story | Natives direktes Sub-Issue eines Epics mit `type:story` und demselben Milestone | Eigenständig wertvoller, reviewbarer Entwicklungsauftrag einschließlich technischem Plan, Code, Tests und Dokumentation |

Unter einer Story werden keine weiteren Tickets angelegt. Technische Arbeitsschritte und ihre Nachweise stehen im technischen Abschnitt derselben Story; es gibt weder einen weiteren Issue-Typ noch Branches, PRs oder Rollenübergaben pro Schritt. Vorhandene technische Alttickets werden nicht automatisch gelöscht oder geschlossen; ausführungsrelevante Vorgaben werden bei einer Wiederaufnahme in der maßgeblichen Story zusammengeführt, ohne den genehmigten Umfang zu verändern.

Ein Epic wird Story für Story umgesetzt. Der Product Owner verantwortet fachlichen Zuschnitt, Priorisierung und tatsächliche Dependencies nach seinem [Ticketvertrag](product-owner.md#fachliche-ticketinhalte). Eine Dependency besteht nur, wenn ein konkretes Vorgängerergebnis zur sinnvollen Erstellung oder Abnahme fehlt; Priorität und Arbeitsreservierung sind keine Dependencies. Epics bleiben top-level, die Roadmap verlinkt sie. Der [Orchestrator](orchestrator.md) steuert Auswahl, Reservierung und nötige Wechsel innerhalb des beauftragten Ziels.

## Inhalte und Zuständigkeiten

GitHub-Artefakte sind werkzeug- und akteursneutral: Sie beschreiben nicht, ob ein Mensch, eine KI oder ein bestimmtes Werkzeug die Arbeit ausführt. Sie enthalten Bedarf, Ergebnis, Scope/Nicht-Ziele, relevante Regeln, überprüfbare Akzeptanz, Priorität, Status und sachliche Voraussetzungen. Die technische Story-Ausarbeitung darf Einstiegspunkte, Lösungen, Testauftrag und Befehle enthalten. Goals, Prompts, Agentenanweisungen, Chatprotokolle und interne Übergabemarker gehören nicht in Titel, Beschreibungen, Kommentare, Labels, Milestones oder Projects.

| Rolle | Verantwortet | Maßgeblicher Vertrag |
| --- | --- | --- |
| Orchestrator | Goal-Scope, serielle Koordination, GitHub-Zuordnung, Integration und belegter Abschluss | [Orchestrator](orchestrator.md) |
| Product Owner | Produktnutzen, Epic-/Story-Scope, Akzeptanz, Prioritäten, Dependencies und fachliche Vorgaben für das Handbuch | [Product Owner](product-owner.md) |
| UX Designer | Designsprache, Nutzerführung, notwendige geprüfte Entwürfe und UX-Ticketergänzung | [UX Designer](ux-designer.md) |
| Tech Lead | technische Entscheidung, Bestandsanalyse, ausführbarer Storyplan, Risiken/Nachweise und technische Dokumentationsvorgaben | [Tech Lead](tech-lead.md) |
| Software Developer | vollständige Story-Implementierung, lokales Refactoring, Testpflege, Story-PR und Codekorrekturen | [Software Developer](software-developer.md) |
| Documentation Writer | technische Bestandsdokumentation und Benutzerhandbuch für menschliche Entwickler, Tester und Anwender | [Dokumentation](documentation.md) |
| Code Reviewer | unabhängiger Abgleich des vollständigen PRs mit Anforderungen und betroffenen bestehenden Verträgen | [Code Review](code-review.md) |

Modelle und Reasoning stehen ausschließlich in den [Agentenkonfigurationen](../../.codex/agents/). Fachrollen arbeiten seriell und delegieren nicht weiter. Notwendige fachliche, gestalterische oder technische Rückfragen laufen gezielt über den Orchestrator, ohne zusätzliche obligatorische Beratungs- oder Freigaberunde. Reversible Details entscheidet die zuständige Rolle in ihrem Spielraum; lokale Developer-Entscheidungen sind in dessen Vertrag abgegrenzt.

## Ablauf einer Story

1. **Fachliche Grundlage:** Der Product Owner erstellt oder refinert die ausgewählte Story im Featurekontext. Nutzen, Scope, nummerierte beobachtbare Akzeptanz, UI-Relevanz und reale Voraussetzungen müssen entscheidbar sein. Spätere Stories werden nur so weit ausgearbeitet, wie ihre Priorisierung es erfordert.
2. **Gestaltung:** Bei UI-Relevanz liefert der UX Designer die nötige Gestaltungsgrundlage nach seinem [Ticketvertrag](ux-designer.md#ux-inhalte-im-ticket). Bestehende eindeutige Gestaltung wird verwendet; neue visuelle Grundlagen oder wesentliche offene Layoutentscheidungen brauchen tatsächlich gerenderte, geprüfte Mockups.
3. **Technischer Plan:** Der Tech Lead untersucht reale Codepfade und Auswirkungen und ergänzt die Story nach seinem [Ticketvertrag](tech-lead.md#technischer-ticketvertrag). Der Plan enthält Entscheidung, Gründe, verbindliche Grenzen, Einstiegshilfen, geordnete Schritte, relevante Patterns/Refactorings, echte Voraussetzungen und risikogerechte Nachweise. Es werden keine technischen Sub-Issues erstellt.
4. **Umsetzung bis zum PR:** Nach vorliegenden und gespeicherten Grundlagen setzt der Orchestrator `implementation-ready` und bereitet den nativ verknüpften Story-Branch aus `master` vor. Der Developer erhält die gesamte Story als zusammenhängenden Auftrag. Er erledigt ihre Schritte seriell, pflegt Code und Tests gemeinsam, prüft den gesamten Story-Diff und erstellt beziehungsweise aktualisiert genau einen Story-PR gegen `master`. Erst dann meldet er sich mit `DEV_HANDOFF`, veröffentlichtem Head und Prüfevidenz beim Orchestrator zurück; Dokumentation und unabhängiges Review stehen noch aus. Eine echte notwendige Entscheidung darf diesen Auftrag gezielt unterbrechen.
5. **Dokumentation im selben PR:** Der Documentation Writer ergänzt technische Dokumentation und Benutzerhandbuch anhand des tatsächlichen geprüften Codes, vorhandener Entscheidungen und Nachweise im bestehenden Story-Branch/PR. Es gibt keinen nachgelagerten Dokumentations-PR. Er übergibt aktualisierte Dokumente und Nachweise oder ein begründetes Nicht-Erfordernis nach dem [Dokumentationsvertrag](documentation.md). TL und PO bleiben inhaltliche Entscheidungsinstanzen; ihre erneute Beauftragung erfolgt nur bei einer konkreten offenen Frage.
6. **Unabhängiges Review:** Der Code Reviewer prüft den vollständigen PR mit Code, Tests und betroffener Dokumentation für den aktuellen Head. Belegte Findings gehen gesammelt über den Orchestrator an den Developer für Code/Tests beziehungsweise den Documentation Writer für Dokumente. Keine zusätzliche allgemeine Produkt-, Architektur- oder UX-Abnahmerunde.
7. **Gezielte Korrektur:** Korrekturen erfolgen im selben Branch/PR. Die betroffenen Rollen aktualisieren Nachweise; Verhaltensänderungen werden gegebenenfalls in der Dokumentation nachgeführt. Der Reviewer prüft das Delta, frühere Findings und betroffene Zusammenhänge und bestätigt den neuen Gesamtstand. Geeignete unveränderte Erkenntnisse bleiben verwendbar.
8. **Integration und Abschluss:** Der Orchestrator prüft die [Merge-Nachweise](#merge-nachweise), merged und bestätigt die tatsächliche Aufnahme von Code und Dokumentation auf `master`. Erst bei erfüllter Story-Akzeptanz und vollständigem Dokumentationsabschluss folgt die nächste Story. Ein geöffneter PR oder automatisch geschlossenes Issue allein beweist keinen Erfolg.

Jede erforderliche Phase benötigt einen tatsächlichen Beitrag ihrer zuständigen Rolle. Ein bereits vorhandener Beitrag erfüllt die Phase ohne erneuten Rollenaufruf, wenn Auftrag/Anforderungen, maßgebliche Entscheidungen, relevante Codebasis und Abhängigkeiten ihn weiterhin tragen. Die Zuordnung von Beitrag, geprüftem Stand und Evidenz muss vorliegen; ein Label oder bloßer Fertigmarker genügt nicht. Bei geänderter Grundlage wird nur der betroffene Anteil erneut beauftragt. Wiederaufnahme beginnt am ersten offenen oder ungültig gewordenen Schritt, nicht automatisch am Anfang.

## Übergabevertrag

Jede Übergabe nennt Artefakt/Story, verantwortete Dateien, geprüften Stand, konkretes Ergebnis, verwendete Evidenz und offene Grenzen. Codebezogene Übergaben nennen Branch, Base/Head und PR-Link. Gültige Ergebnisse werden referenziert, statt volle Chatprotokolle, Tickettexte oder Prüfberichte zu kopieren. Der [Orchestrator-Kontextvertrag](orchestrator.md#übergaben-und-sparsamer-kontext) bestimmt Thread-Wiederverwendung und Kontextumfang.

| Marker, ausschließlich lokal | Bedeutung |
| --- | --- |
| `PO_REFINED` / `PO_REVIEWED_NO_CHANGE` | abgeschlossener fachlicher Auftrag mit benanntem Umfang: Backlogbereich, Epic oder Story; erst eine entscheidbare Story geht weiter |
| `UX_DESIGN_READY` / `UX_NOT_REQUIRED` | nutzbare, erforderlichenfalls visuell geprüfte Gestaltungsgrundlage oder belegte fehlende UI-/UX-Relevanz |
| `TECH_PLAN_READY` | technisch ausführbare Story-Ausarbeitung; keine bloße Beratung oder ungeklärte Grundentscheidung |
| `DEV_HANDOFF` | vollständige Implementierung mit PR/Head und erforderlicher Prüfevidenz beziehungsweise gezielte Rückgabe bei echter Entscheidungsgrenze; keine eigene Review-Freigabe |
| `DOCS_UPDATED` / `DOCS_REVIEWED_NO_CHANGE` | technische Dokumentation und Benutzerhandbuch geprüft; pro Bereich Änderung oder begründeter unveränderter Stand, Quellstand und Evidenz |
| `CODE_REVIEW_APPROVED:<sha>` / `CODE_REVIEW_CHANGES_REQUESTED:<sha>` | unabhängige Freigabe beziehungsweise belegte Findings für den benannten Head |

Ein UX-Entwurf belegt weder implementierte UI noch vollständige Accessibility-Konformität. Fachliche/technische Marker allein ersetzen keine gespeicherten GitHub-Grundlagen für `implementation-ready`. Ein Dokumentationsmarker belegt noch keine Integration. Wesentliche offene Prüfgrundlagen werden konkret zurückgegeben, ohne erfundene Fehler- oder Erfolgsmarker.

Fehlt einer Rolle geeigneter GitHub-Schreibzugriff, übergibt sie vollständige veröffentlichungsfertige Inhalte und konkrete Zuordnungen beziehungsweise vorbereitete Anhänge. Der Orchestrator speichert sie im bestehenden autorisierten Kontext und verifiziert das Ergebnis. Vorbereitete Inhalte und lokale Pfade werden nicht als veröffentlichte Artefakte ausgegeben.

## Merge-Nachweise

Unmittelbar vor dem Merge müssen aktueller PR-Head, unabhängige Review-Freigabe, erforderliche GitHub-Prüfungen und erfolgreiche Developer-Prüfevidenz denselben Gesamtstand tragen. Technische Dokumentation und Benutzerhandbuch müssen nach dem [Dokumentationsvertrag](documentation.md#nachweis-und-abschluss) für diesen Stand geeignet sein. Bestehende Branchschutzregeln bleiben verbindlich.

Ein neuer Head verlangt keine mechanische Wiederholung aller Prüfungen. Bei einem reinen Dokumentationsdelta können Developer-Ergebnisse für den letzten geprüften Code-Head weitergelten: Code-Head und neuer Head werden benannt, das Delta wird geprüft, und Code-, Konfigurations-, Build- und Testverträge müssen unverändert bleiben. Dies benötigt keinen weiteren Developer-Aufruf allein wegen neuer Dokumentationscommits. Ändert sich eine dieser Grundlagen oder ist ihre Wirkung unklar, liefert der Developer die konkret betroffenen Nachweise nach. Das unabhängige Review bestätigt immer den aktuellen vollständigen Head.

Developer und Reviewer verwenden [Testing](testing.md), vorhandene [Projektbefehle](../project/local-development.md) und passende Evidenz. Ausgeführte Befehle/Ergebnisse, übernommene Nachweise, Codeabgleich und reale Bedienprüfung werden unterschieden. Qualitätsnachweise autorisieren keine Veröffentlichung; externe Gates folgen [Governance](governance.md).

## Native GitHub-Zuordnung

Ein Story-Branch heißt `issue/<PROJECT_KEY>-<story>` und zielt mit genau einem PR auf `master`. `link-issue-branch.yml` reagiert auf `implementation-ready` beziehungsweise einen manuellen Aufruf mit Storynummer. Er prüft die Story direkt unter einem top-level Epic im selben Milestone, erstellt den Branch mit `createLinkedBranch` und prüft die native Development-Zuordnung. Ein vorhandener nicht zugeordneter Branch ist ein Fehler. Rechte: `contents: write`, `issues: write`.

`link-issue-pr.yml` prüft bei `opened`, `reopened`, `edited`, `synchronize` und `ready_for_review` PRs aus demselben Repository. Der PR schließt genau seine Story mit `Closes #<story>`, nennt genau ein Parent-Epic mit `Refs #<epic>`, hat die passende native Story-Zuordnung und keinen zweiten verknüpften PR für dieselbe Story. Technische Untertickets und `Implements`-Zeilen werden nicht verwendet. Dokumente sind Teil des einen Story-PRs; die [PR-Vorlage](../../.github/pull_request_template.md) enthält dessen Nachweise. Rechte des PR-Workflows: ausschließlich `contents: read`, `issues: read`, `pull-requests: read`.

Beide Workflows verwalten GitHub-Metadaten. Sie führen keine Produktbuilds, Produkttests oder Auslieferung aus; deren Anforderungen bleiben unabhängig davon bestehen. Die Vorlage konfiguriert keinen automatischen Merge. Ein eingeschränkter GitHub-Zugriff ist eine konkrete externe Grenze; lokale Ergebnisse bleiben bearbeitbar.

## GitHub-Einrichtung

Dieses Repository verwendet derzeit `master` als Default-Branch. Die übernommenen Workflows ermitteln den tatsächlichen Default-Branch über GitHub; eine Umbenennung ist nicht erforderlich. Für den Storyprozess braucht das Repository aktivierte Actions sowie `type:roadmap`, `type:epic`, `type:story` und `implementation-ready`. Milestones, Priorisierung und native Sub-Issues/Dependencies werden im tatsächlichen Backlog gepflegt. Kopieren der Vorlage erzeugt keine Tickets oder anderen externen Änderungen.

Beide Workflows verwenden das Repository des Ereignisses und die Repository-Variable `PROJECT_KEY` unter **Settings → Secrets and variables → Actions → Variables**; ohne Variable gilt hier `WOWVO`. Das Kürzel besteht aus Großbuchstaben und Ziffern und beginnt mit einem Buchstaben. Lege es vor dem ersten Story-Branch fest; ändere es bei bestehenden Branches nicht beiläufig. Die Zuordnung steht in [Projektidentität](../project/project-identity.md). Workflow- oder Containeränderungen sind für ein eigenes Kürzel nicht nötig.

## Zielabschluss und wiederkehrende Pflege

Ein Storyziel endet nach deren vollständigem Abschluss. Ein Epic endet, wenn alle erforderlichen Storybeiträge integriert, seine Akzeptanz am Zusammenspiel erfüllt und die Dokumentation aktuell sind. Ein Milestone endet nach seinen vollständigen Epics und erfüllter integrierter Release-Akzeptanz. Einzelne Story-/Epicziele lösen keinen zusätzlichen Releaseabschluss aus; eine eigene integrierte Abnahme erhält nur bei entsprechendem Umfang ein Epic. Es werden keine erfüllten Kriterien aus bloß geschlossenen Issues abgeleitet.

Die [regelmäßige Dokumentationspflege](documentation.md#umfang-und-wiederkehrende-pflege) wird mit der betroffenen Story und zum Epic-Abschluss möglichst mit dessen letzter Story integriert. Ein Merge löst keine zweite Dokumentationsrunde aus. Größere eigenständige Pflege erfolgt im ausdrücklich beauftragten Kontext beziehungsweise einer eigenen fachlich begründeten Story mit einem PR, nicht als zusätzlicher PR zur bereits abgeschlossenen Story.

Skill-Einrichtung und Wartung folgen ausschließlich [skills.md](skills.md); eine spätere Signal-Anbindung dem [Signal-Standard](signal-integration.md). Sie erzeugen weder zusätzliche Fachphasen noch künstliche Backlogelemente. Für alle Arbeiten gelten die feste [Containerbasis](local-development.md), gezieltes Kontextladen und die unveränderten nativen Goal-Grenzen.
