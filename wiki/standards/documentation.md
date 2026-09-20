---
type: Role Contract
title: Dokumentation und Documentation Writer
description: Rollenvertrag für technische Dokumentation und Benutzerhandbuch, Bestandsnachweise und regelmäßige Verbesserung.
tags:
- shared
- documentation
status: stable
scope: shared
sources:
- id: template-adoption
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/b001e1b700d75aa0f31f6ced84381ba194b79582/wiki/standards/documentation.md
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/documentation.md
  title: 'Vorlage vor der Wiki-Migration: standards/documentation.md'
- id: wiki-pattern
  resource: ../sources/llm-wiki.md
- id: wiki-format
  resource: ../sources/open-knowledge-format.md
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Dokumentation und Documentation Writer

Dokumentation wird im [LLM Wiki](../index.md) gepflegt. Sie erklärt das tatsächliche Produkt und ermöglicht seine Übergabe an menschliche Entwickler und Tester. Technische Dokumentation und Benutzerhandbuch sind verbindliche Ergebnisse; der Umfang folgt dem betroffenen Verhalten und Leserbedarf. Es gelten die [Ablageregeln](governance.md#planungsartefakte-und-dauerhafte-dokumentation), keine Planungs- oder Ticketchronik im Checkout.

## Verantwortung und Zeitpunkt

Der Agent [documentation_writer](../../.codex/agents/documentation-writer.toml) erstellt und pflegt beide Bereiche. Der Tech Lead verantwortet technische Entscheidungen und Konzepte, der Product Owner fachliche Regeln und Nutzeraufgaben, der UX Designer die Designsprache. Der Writer verwendet deren bestätigte Entscheidungen, ohne sie neu festzulegen. Eine konkrete Unklarheit geht seriell über den Orchestrator an die zuständige Rolle; eine zusätzliche routinemäßige TL-/PO-Freigabe ist nicht vorgesehen.

Der Writer arbeitet nach der Developer-Übergabe auf demselben Story-Branch im bereits erstellten Story-PR, vor dessen abschließendem unabhängigen Review und Merge. Der [Entwicklungsprozess](development-process.md#ablauf-einer-story) regelt Integration und Nachweise. Es gibt keinen zusätzlichen Dokumentations-PR für diese Story und keine nachgelagerte zweite Rollenrunde. Code und wesentliche Dokumentation werden gemeinsam integriert. Eine technische Änderung ohne Einfluss auf Anwender braucht keine künstliche Handbuchänderung; der geprüfte Bedarf wird für beide Bereiche getrennt bestätigt.

Der Developer liefert Code, Tests, normale PR-Beschreibung und Prüfevidenz. Der Writer ermittelt daraus, aus tatsächlichen Abläufen, akzeptierten Ticketentscheidungen und vorhandenen Dokumenten selbst den Pflegebedarf. Eine zusätzliche Dokumentationsplanung oder vorbereitende Dokumentationsübergabe durch den Developer ist nicht erforderlich. Erkannte Produktfehler gehen mit Evidenz an den Orchestrator; weder Code noch Akzeptanz werden im Dokumentationsauftrag nebenbei geändert.

## Maßgeblicher Bestand und Schreibumfang

Grundlage sind der aktuelle implementierte Story-Stand, betroffene Verträge, Tests und belegte Prüfergebnisse einschließlich akzeptierter Planabweichungen. Geplante Fähigkeiten, frühere Ticketentwürfe und Mockups beweisen keine Umsetzung. Die Beschreibung im PR gilt für dessen Code-Stand; erst der bestätigte gemeinsame Merge belegt den Bestand auf `master`. Ein Merge belegt keine öffentliche Bereitstellung: Verfügbarkeitsaussagen brauchen den tatsächlichen Release-/Betriebsstand. Wesentliche Voraussetzungen und Einschränkungen bleiben sichtbar, ungeklärte Projektwerte `To be defined`.

Schreibe ausschließlich betroffene Bestandsseiten unter `wiki/project/`, daraus unmittelbar abgeleitete Zusammenfassungen unter `wiki/concepts/` beziehungsweise `wiki/overview.md`, nötige Quellenzusammenfassungen unter `wiki/sources/`, betroffene Indizes und Einstiegslinks in README sowie nützliche Dokumentationsbilder oder Diagrammquellen. Pflege OKF-Metadaten, Quellen, Querverweise und wesentliche Wissensänderungen in `wiki/log.md` nach dem [Wiki-Vertrag](../schema.md). Dieser Umfang erlaubt keine Änderung allgemeiner Regeln oder des Wiki-Schemas. Der technische Einstieg ist [Projektarchitektur](../project/architecture.md), der fachliche [Benutzerhandbuch](../project/user-manual.md). Bei tatsächlichem Umfang können Kapitel und Bilder unter `wiki/project/user-manual/` ergänzt werden; weitere Markdown-Wissensseiten folgen ebenfalls OKF. Gemeinsame Fachbegriffe werden im vorhandenen Projektmodell konsistent gehalten; der UI-Leitfaden folgt den entschiedenen und implementierten UX-Vorgaben.

Der Auftrag erlaubt nötige Dokumentationscommits und Pushes auf dem bestehenden Story-Branch. Er erlaubt keine Änderung von Produktcode, Tests, Infrastruktur oder allgemeinen Standards, keine eigene Produktentscheidung, keinen zusätzlichen Branch/PR und keinen Merge. Bewahre fremde Änderungen. Eine Handbuchlücke wird nicht durch eine heimliche Produktänderung behoben. Bei fehlendem Schreibzugriff übergib vollständige vorbereitete Inhalte und die konkrete Grenze an den Orchestrator, ohne Speicherung zu behaupten. Eine ausdrücklich separat beauftragte Dokumentationspflege folgt dem dafür erteilten Scope.

## Technische Dokumentation

Schreibe für Entwickler, technische Betreiber und Tester ohne vorausgesetztes Projektwissen. Erweitere vorhandene Einstiege; vertiefe nur, was Verständnis, sichere Änderung, Prüfung oder Betrieb unterstützt:

- **Überblick:** Zweck, Systemkontext, Bausteine, Verantwortungen und externe Abhängigkeiten. Eine C4-Kontext- oder Bausteinsicht ist bei zusätzlichem Erklärungswert geeignet.
- **Grundkonzepte:** tatsächlich eingesetzte übergreifende Regeln und Patterns, etwa Datenhaltung, Identität, Berechtigungen, Fehlerbehandlung oder Nebenläufigkeit. Erkläre Wie und Warum an maßgeblichen Quellstellen; keine vollständige arc42-Checkliste oder Klasseninventare.
- **Zusammenspiel:** wesentliche Schnittstellen, Datenflüsse, Zustandsübergänge und Vertrauensgrenzen. Nutze ein Sequenz-, Zustands- oder UML-Diagramm, wenn es einen schwierigen Zusammenhang besser erklärt.
- **Entscheidungen und Einstieg:** Gründe, relevante Nachteile und Grenzen der umgesetzten Lösung, Quellpfade und Vertragsdefinitionen. Verlinke bestätigte Entscheidungen und API-/Schemaspezifikationen, statt Historie oder Felder zu kopieren.
- **Entwicklung, Prüfung und Betrieb:** tatsächliche Einrichtung, Start, verfügbare Prüfwege, synthetische Testdaten beziehungsweise Rollen, Diagnose, Migration, Wiederherstellung und Betriebsgrenzen, soweit betroffen. Menschen müssen die relevanten Prüfungen mit den vorhandenen Projektbefehlen nachvollziehen können; dokumentiere Voraussetzungen, erwartete Ergebnisse und bekannte Grenzen. Keine erfundenen Befehle oder unbestätigten Erfolgsbehauptungen.

Wähle Text, Tabelle oder Diagramm nach der Leserfrage. Diagramme benennen Zweck, Geltungsbereich, Bausteine und Beziehungen, erklären verwendete Symbole und vermischen keine Abstraktionsebenen ohne Erklärung. Wartbare eingebettete Quellen genügen, wenn sie den Zusammenhang darstellen; keine Pflicht zu sämtlichen C4-Ebenen, einem bestimmten Werkzeug oder zusätzlichen Exportdateien.

## Benutzerhandbuch

Das Handbuch hilft Anwendern und menschlichen Testern, das Produkt zu verstehen und echte Aufgaben nachzuvollziehen. Verwende Nutzerbegriffe und reale zugängliche Beschriftungen der Oberfläche. Gliedere nach Leserbedarf und nutze nur benötigte Formen:

- **Verstehen:** Zweck, Zielgruppen, grundlegende Begriffe und Zusammenhänge vorhandener Features. Interna sind nur relevant, wenn sie eine Nutzungsentscheidung beeinflussen.
- **Einsteigen:** ein kurzer durchgängiger erster Nutzerweg mit echten Voraussetzungen, Berechtigungen und erkennbarem Ergebnis, ohne vorausgesetztes Projektwissen.
- **Aufgaben erledigen:** nach Nutzerzielen benannte Anleitungen mit Ausgangslage, geordneten Schritten und erwartetem Ergebnis. Bedeutende Varianten, Unterbrechungen und Fehlerwege ergänzen, optionale Schritte kennzeichnen.
- **Nachschlagen und Hilfe:** relevante Einstellungen, Rollen und Begriffe sowie bekannte Problemsymptome, sichere Abhilfe und tatsächlich vorhandene Hilfewege. Gemeinsame Erklärungen verlinken.

Verwende kurze aktive Sätze, aussagekräftige Überschriften und konsistente Begriffe. Benenne Aktionen anhand ihrer zugänglichen Namen, nicht allein durch Farbe oder Position. Erläutere eine entscheidungsrelevante Folge vor dem Schritt. Beschreibe nur vorhandene Rücknahme- und Wiederholungsmöglichkeiten. Das Handbuch ist keine Liste aller Schaltflächen und keine umbenannte Entwickleranleitung. Produktbehauptungen, Supportkanäle und Freigaben werden nicht erfunden.

Screenshots des realen Produkts benötigen einen konkreten Erklärungsnutzen, synthetische Daten, passende Rechte, verständliche Beschriftung und eine textlich nutzbare Anleitung. Prüfe ihre Aktualität bei geänderten Ansichten. Mockups, Bildserien auf Vorrat und automatische Bildschirmkataloge sind keine Bestandsdokumentation.

## Umfang und wiederkehrende Pflege

Jede Aussage besitzt eine maßgebliche Quelle. Verlinke gemeinsamen Kontext und Verträge, statt sie abzuschreiben. Das Wiki verdichtet Zusammenhänge in Synthesen; die vollständige Regel beziehungsweise Bestandsaussage bleibt in ihrer Detailseite. Ändert sich diese Quelle, prüfe unmittelbar abhängige Zusammenfassungen, Metadaten und Indizes im selben Auftrag. Teile bestehende Abschnitte erst bei tatsächlichem Umfang nach Leseraufgaben auf. Bilder ersetzen keine Anleitung; eine zweite Darstellung eines einfachen Zusammenhangs ist entbehrlich. Keine zusätzlichen Generatoren, Hostingwege, Portfreigaben oder automatischen Containerstart-Schritte für Dokumentation.

Die folgenden Anlässe bestimmen die Pflege; es gibt keinen Hintergrundjob und keinen vollständigen Bestandsaudit nach jeder Kleinigkeit:

- **Mit jeder inhaltlichen Story vor dem abschließenden Review:** betroffene technische und fachliche Abschnitte samt direkt abhängigen Verweisen und Abläufen prüfen und nachführen. Codekorrekturen danach erfordern nur den betroffenen Dokumentationsabgleich.
- **Zum Feature-Epic-Abschluss:** Zusammenspiel der Konzepte und vollständigen Nutzerweg einschließlich Einstieg, Begriffen und Querverweisen prüfen, möglichst im PR der letzten Story. Geeignete Nachweise weiterverwenden.
- **Bei konkreten Hinweisen:** wiederkehrende Supportfragen, Onboardingprobleme, geänderte Begriffe, entfernte Funktionen oder Widersprüche gezielt korrigieren. Nach längerer Projektpause die für den nächsten Auftrag benötigten Einstiege abgleichen.

Prüfe Richtigkeit, Verständlichkeit, Auffindbarkeit und Nutzen. Schließe konkrete Lücken, fasse Duplikate zusammen und entferne obsolete Aussagen, Bilder, Kapitel und verwaiste Links. Geeignete Texte werden nicht aus Stilvorliebe umgeschrieben. Größere unabhängige Lücken gehen als konkreter Pflegebedarf an den Orchestrator beziehungsweise Product Owner; sie werden weder ignoriert noch verdeckt in das Feature aufgenommen. Erforderliche Grundlagen für die Übergabe dieser Story bleiben Teil ihres Abschlusses.

## Nachweis und Abschluss

Prüfe geänderte Aussagen gegen Code, Verträge und tatsächliche Bedienung. Verwende passende aktuelle Evidenz weiter. Fehlt für eine neue oder unklare wesentliche Anleitung ein Nachweis, führe sie gezielt mit synthetischen Daten aus, soweit Zugriff und Auftrag dies erlauben. Behaupte keine beobachtete Bedienung bei reinem Codelesen. Prüfe geänderte Links, Quellpfade und die Lesbarkeit benötigter Darstellungen mit vorhandenen Werkzeugen. Eine reine Textkorrektur verlangt weder vollständige Produkttests noch neue Wortlauttests; für Code-/Konfigurationseinfluss gilt der [Merge-Vertrag](development-process.md#merge-nachweise).

Übergib geprüften Code-Stand, aktuellen PR-Head, verantwortete Dateien, verwendete Evidenz und offene Grenzen. Bestätige technische Dokumentation und Handbuch jeweils mit `DOCS_UPDATED` oder begründetem `DOCS_REVIEWED_NO_CHANGE`. Ein Marker allein belegt weder Speicherung noch Merge. GitHub enthält den sachlichen Änderungs- und Prüfnachweis, keine internen Rollenmarker. Fehlende wesentliche Grundlagen werden benannt, nicht erfunden. Der Orchestrator verifiziert die gemeinsame Integration. Die [Recherchegrundlage](references.md#technische-dokumentation-und-benutzerhandbuch) ist keine neue Checkliste pro Story.
