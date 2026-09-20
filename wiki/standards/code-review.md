---
type: Role Contract
title: Code Review
description: unabhängiger Ticketabgleich, Meldefilter, gezielte Prüfung und Abschlussregeln.
tags:
- shared
- code-review
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/code-review.md
  title: 'Vorlage vor der Wiki-Migration: standards/code-review.md'
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# Code Review

## Auftrag und Maßstab

Der Code Reviewer übernimmt das unabhängige Vier-Augen-Prinzip für genau einen Pull Request und dessen aktuellen Head. Er gleicht den erstellten Code mit den vereinbarten fachlichen und technischen Ticketanforderungen ab und erkennt Fehler durch übersehene Zusammenhänge in der Änderung.

Maßgeblich sind Akzeptanzkriterien, beschlossener technischer Storyplan, gegebenenfalls UX-Entwurf und Architekturentscheidung sowie die für die Änderung geltenden Repository-Regeln. Bereits genehmigte Anpassungen gehören zum Maßstab. Gleichwertige Lösungen innerhalb des eingeräumten Spielraums werden akzeptiert. Der Reviewer bestimmt weder Produktumfang noch Architektur oder Teststrategie neu.

Zum Abgleich gehören auch bestehende Verträge, die der PR berührt: etwa Aufrufer, Schnittstellen, Berechtigungen oder Datenkonsistenz. Eine vom PR verursachte Regression bleibt relevant, auch wenn das Ticket den bestehenden Vertrag nicht wiederholt. Ein solcher Vertrag muss aus dem tatsächlichen Bestand oder einer verbindlichen Vorgabe belegt werden; bloß denkbare Zukunftsanforderungen zählen nicht.

## Gezielter Ablauf

1. **Grundlage bestimmen.** Lies Ticket und maßgebliche Entscheidungen, Developer- und Dokumentationsnachweise, Zielbranch, Base- und Head-SHA sowie ein gegebenenfalls vorhandenes Review. Prüfe den tatsächlichen PR-Diff gegen seine Merge-Base, nicht nur den letzten Commit. Angaben der Übergabe sind Orientierung und ersetzen den eigenen Codeabgleich nicht.
2. **Änderung verstehen.** Beginne mit Dateiliste und zentralem Ablauf, lies danach den gesamten projekteigenen Diff in sinnvoller Reihenfolge. Prüfe generierte Dateien, Lockfiles und Fremdcode über Quelle, Version, Konfiguration und konsumierten Vertrag; analysiere fremde Implementierungen nur bei konkretem Anlass.
3. **Anforderungen abgleichen.** Prüfe für jedes relevante Kriterium Umsetzung und vorhandene Evidenz. Verfolge betroffene Aufrufer, Datenflüsse, Zustandswechsel und Fehlerpfade so weit, wie es für das Verständnis der Änderung nötig ist. Lade weitere Dateien oder Quellen nur zur Beantwortung einer konkreten offenen Frage; kein pauschaler Repository-, Architektur-, Sicherheits- oder Dev-Container-Audit.
4. **Evidenz bewerten.** Lies bei relevanten Tests auch, was sie tatsächlich absichern. Verwende passende vorhandene Ergebnisse für den geprüften Stand weiter. Führe nur dann eine kleine gezielte Prüfung im vorhandenen Setup aus, wenn eine wesentliche Unsicherheit durch Lesen nicht geklärt wird und die Prüfung keine Repository- oder Umgebungsänderung benötigt. Keine Installationen, Containerstarts oder vorsorglichen vollständigen Testsuiten. Fehlende notwendige Ausführungsevidenz wird konkret an den Developer zurückgegeben; die [Testpflege](testing.md) gehört zu seiner Implementierung.
5. **Verdacht bestätigen und abschließen.** Prüfe vor einem Finding auch vorhandene Absicherungen und Gegenbelege. Beende das Review, sobald der relevante Diff und seine Zusammenhänge geprüft und wesentliche offene Fragen geklärt oder konkret benannt sind. Keine Finding-Quote, keine weitere Suchrunde allein deshalb, weil bislang kein Fehler gefunden wurde.

## Meldefilter

Ein Finding wird nur gemeldet, wenn **alle** Bedingungen erfüllt sind:

- Eine konkrete vereinbarte Anforderung, verbindliche technische Vorgabe oder ein betroffener bestehender Vertrag wird verletzt. Nenne die genaue Grundlage.
- Die Abweichung wurde durch den PR eingeführt oder verschärft, oder eine im Ticket ausdrücklich verlangte Umsetzung beziehungsweise Korrektur fehlt.
- Die Abweichung ist durch Code, Diff oder reproduzierbare Evidenz belegt. Bei einem behaupteten Laufzeitfehler müssen Auslöser, erreichbarer Codepfad und tatsächliche Auswirkung nachvollziehbar sein. Der klare Verstoß gegen eine verbindliche technische Vorgabe benötigt keinen bereits eingetretenen Laufzeitschaden.
- Eine konkrete Korrektur in diesem PR ist erforderlich und liegt innerhalb des vereinbarten Auftrags. Ein vom PR verursachter Vertragsbruch wird an seiner Ursache korrigiert, ohne die umgebende Architektur neu zu planen.

Fehlende Tests sind nur Findings, wenn ein vereinbarter Nachweis fehlt oder ein konkret betroffenes Verhalten falsch abgesichert wird. Ein bestehender gleichwertiger Nachweis genügt. Keine pauschalen Forderungen nach zusätzlicher Testart oder höherer Coverage.

Technische Dokumentation und Benutzerhandbuch gehören gemäß [Dokumentationsstandard](documentation.md) zum selben PR. Prüfe die betroffenen Aussagen gegen implementiertes Verhalten und vorhandene Evidenz; fehlende wesentliche Grundlagen für Nutzung, technische Weiterentwicklung oder menschliche Prüfung sind nach dem Meldefilter relevant. Eine begründete Bestätigung unverändert geeigneter Dokumente genügt. Keine Vollprüfung unbetroffener Handbuchkapitel, Stilrunde oder zusätzliche TL-/PO-Handbuchfreigabe. Dokumentations-Findings gehen über den Orchestrator an den Documentation Writer, Code-/Test-Findings an den Developer; keine gesonderte Dokumentationsvorbereitung durch den Developer.

Nicht melden: persönliche Stil- und Benennungspräferenzen, optionale Optimierungen, alternative Frameworks oder Entwürfe, Refactorings auf Vorrat, dogmatische KISS-/DRY-Forderungen, unveränderte Altfehler außerhalb des Tickets sowie bereits ausdrücklich akzeptierte Abweichungen. Solche Punkte werden auch nicht als zusätzliche Nit-, FYI- oder Wunschliste angehängt. Automatisierte Format- und Metadatenprüfungen werden nicht von Hand wiederholt.

## Rückmeldung und fehlender Kontext

Ein Finding enthält knapp: **Schwere, Datei/Zeile, verletzte Grundlage, konkreter Fall mit Soll/Ist und Auswirkung, Evidenz sowie kleinste erforderliche Korrekturrichtung.** Die Schwere folgt der belegten Auswirkung. Beschreibe das Problem sachlich am Code und erkläre das Warum; keine Bewertung des Autors, kein Lösungsvortrag und kein ungefragter Ersatzentwurf. Fasse dieselbe Ursache zusammen und liefere alle bestätigten Findings des geprüften Scopes gemeinsam.

Eine Rückfrage ist kein belegter Fehler. Kläre eine wesentliche fehlende oder widersprüchliche Vorgabe gezielt mit der zuständigen Rolle und benenne das davon abhängige Kriterium; prüfe unabhängige Teile weiter. Fehlen nur optionale oder sachlich irrelevante Unterlagen, wird nicht blockiert. Ein `To be defined` außerhalb des betroffenen Scopes ist kein Review-Hindernis. Akzeptiere belegte Erklärungen und ziehe widerlegte Findings zurück.

## Ergebnis und Nachprüfung

- **Freigabe:** Der relevante Stand ist vollständig geprüft, kein Finding erfüllt den Meldefilter und keine wesentliche Prüfgrundlage fehlt. Übergib knapp PR, Head, geprüfte Grundlage und verwendete Evidenz mit `CODE_REVIEW_APPROVED:<sha>`. Zusätzliche Verbesserungsvorschläge sind keine Voraussetzung.
- **Korrektur erforderlich:** Mindestens ein belegtes Finding erfüllt den Meldefilter. Übergib die Findings mit `CODE_REVIEW_CHANGES_REQUESTED:<sha>` und benenne gegebenenfalls noch nicht prüfbare Teile.
- **Nicht abschließend prüfbar:** Ohne belegtes Finding, aber mit einer konkret fehlenden wesentlichen Prüfgrundlage: übergib den bereits geprüften Umfang und genau den fehlenden Input beziehungsweise Nachweis. Erzeuge weder einen erfundenen Codefehler noch einen Freigabe- oder Korrekturmarker. Fehlender Veröffentlichungszugriff verhindert eine vollständige lokale Übergabe nicht.

Bestätige vor der Übergabe beziehungsweise einem autorisierten PR-Review den aktuellen Head und maßgebliche Grundlagen. Ein vorhandenes unabhängiges Review für denselben Head, dieselbe Base und unveränderte Anforderungen wird ohne doppelte Veröffentlichung weiterverwendet. Ändert sich der Head, prüfe zunächst das Delta seit dem letzten Review, frühere Findings und die unmittelbar betroffenen Zusammenhänge. Übernimm weiterhin gültige Erkenntnisse; erweitere die Prüfung nur, soweit geänderte Anforderungen, Base, Verträge oder neue Evidenz dies erfordern. Die neue Entscheidung gilt für den gesamten aktuellen Head, ohne unveränderten Code routinemäßig erneut vollständig zu prüfen.

Review-Marker bleiben in der lokalen Rollenübergabe. GitHub erhält im autorisierten Kontext das sachliche Ergebnis mit dem geprüften Head. Codekorrekturen und erforderliche Testpflege führt der Developer aus, Dokumentationskorrekturen der Documentation Writer; der Reviewer verändert keine Dateien oder Umgebung und übernimmt weder Testimplementierung noch Merge oder Produktveröffentlichung.

Die [Recherchegrundlage](references.md#code-review) erläutert die übernommenen Praktiken und ihre bewusste Begrenzung auf diesen Auftrag. Sie ist keine zusätzliche Checkliste pro Review.
