---
type: Policy
title: UI/UX-Regeln
description: Bedienbarkeit, Accessibility, Zustände, Performance und Prototypgrenzen.
tags:
- shared
- ui-ux
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/ui-ux.md
  title: 'Vorlage vor der Wiki-Migration: standards/ui-ux.md'
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# UI/UX-Regeln

Diese Regeln gelten bei tatsächlich benötigten Benutzeroberflächen. Sie schreiben keine Website, kein Portal, keine Markenrichtung und kein Komponentenframework vor. Erlebnisziel, gemeinsame Gestaltung und umgesetzte Oberflächen stehen im [UI-Leitfaden des Projekts](../project/ui-ux.md).

## Gemeinsame Designsprache

Der [UX Designer](ux-designer.md) verantwortet Farbgebung, Styling, Nutzerführung und die gestalterische Pflege des Leitfadens. Bestätigte Marken- und Plattformvorgaben bleiben bindend. Wiederkehrende Komponenten, Typografie, Farbrollen, Abstände und Interaktionen folgen denselben Verwendungsregeln. Neue Ansichten führen keine eigene Palette oder abweichende Komponentenfassung ohne begründeten Bedarf ein.

Vorhandene semantische Tokens und Komponenten haben Vorrang. Neue Muster oder Varianten werden anhand ihres Nutzens und betroffener Verwendungsstellen entschieden; eine gemeinsame Änderung wird mit ihren Auswirkungen geplant. Der Leitfaden referenziert maßgebliche Token-/Komponentenquellen, statt deren Werte manuell zu duplizieren. Neue Story-Entscheidungen stehen bis zur Umsetzung im Ticket; der Documentation Writer dokumentiert den entstandenen Bestand im selben Story-PR gemäß [Dokumentationsstandard](documentation.md). Die gestalterischen Entscheidungen bleiben beim UX Designer.

## Nutzerfluss und Gestaltung

- Jede Ansicht beantwortet eine erkennbare Hauptfrage und bietet einen verständlichen nächsten Schritt. Informationshierarchie, Sprache und Interaktion machen Systemzustand und mögliche Aktionen klar.
- Wiederkehrende Begriffe, Komponenten und Muster bleiben konsistent. Unterschiedliche Nutzungssituationen dürfen unterschiedliche Informationsdichte und Komposition haben; eine Marke erzwingt keine einheitliche Layoutschablone.
- Responsives Verhalten folgt Inhalt und Arbeitsablauf. Kleine Ansichten werden nicht durch bloßes Zusammenschieben einer Desktopansicht erzeugt.
- Kerninhalte und zentrale Handlungen hängen nicht von dekorativer Bewegung, Canvas oder WebGL ab. Öffentliche Informationsinhalte sollen auch bei fehlender Clientausführung zugänglich sein. Grenzen zwingend interaktiver Funktionen werden verständlich erklärt.
- Sichtbarkeit, Bearbeitungsstand, Freigabe und Lebenszyklus werden im zuständigen Arbeitsbereich erkennbar. Andere Nutzer sehen ausschließlich für sie zulässige Informationen, ohne Hinweise auf verborgenen internen Bestand.
- Formulare fragen nur benötigte Daten ab, behalten Eingaben nach behebbaren Fehlern und zeigen verständliche Feldfehler sowie bei Bedarf eine fokussierbare Fehlerzusammenfassung. Ein unklarer Ausgang einer wirksamen Aktion braucht Statusabgleich vor erneuter Ausführung.

## Entwurfsumfang

Der UX Designer entscheidet nach dem [Rollenvertrag](ux-designer.md) vor der technischen Planung über Kernfluss, Inhaltsbedarf, Gestaltung und tatsächlich relevante Initial-, Loading-, Leer-, Erfolgs-, Fehler-, Offline-, Wiederholungs- und Berechtigungszustände. Neue Muster, Animationen und Komponenten benötigen einen aktuellen Bedarf.

Der einfachste eindeutige Entwurf genügt. Neue visuelle Grundlagen oder wesentliche offene Layoutentscheidungen erhalten echte, gerendert geprüfte Mockups. Bereits entschiedene Gestaltung kann durch vorhandene Referenzen mit konkreter Änderungsbeschreibung abgedeckt werden. Bei ausdrücklich anspruchsvoller Gestaltung werden Idee, Typografie, Farbe, Rhythmus, Bildsprache und Interaktion nachvollziehbar ausgearbeitet. Kein verpflichtendes Mockup für jede Bildschirmgröße und keine Zustandsmatrix aus Gewohnheit.

Geplante UX-Entscheidungen stehen im zugehörigen GitHub-Kontext. Mockups und Prototypen werden am Ticket angehängt oder in ihrer maßgeblichen externen Fassung verlinkt; Darstellung und Grenzen stehen dort beim Entwurf. Sie werden gemäß den [Ablageregeln](governance.md#planungsartefakte-und-dauerhafte-dokumentation) nicht ins Repository übernommen und belegen keine Produktimplementierung. Der Projekt-UI-Leitfaden beschreibt die übergreifenden, tatsächlich umgesetzten Grundlagen. Fehlende Medien oder Texte werden mit sicheren Entwurfsalternativen und der notwendigen Verwendungsfreigabe behandelt.

## Accessibility

Für Weboberflächen ist WCAG 2.2 AA das gemeinsame interne Qualitätsziel für vollständige Kernabläufe. Bei anderen Oberflächen gelten entsprechende Plattformstandards; konkrete zusätzliche Anforderungen werden im Projektkontext geklärt. Qualitätsziel, automatischer Prüfbericht und vollständiger Konformitätsnachweis bleiben unterschiedliche Aussagen.

Semantische Struktur, logische Überschriften, verständliche programmatische Namen, sichtbarer Fokus, Tastaturbedienung, geeignete Sprungnavigation, Kontraste, Reflow und Zoom bis 400 Prozent gehören zum Entwurf. Dialoge haben nachvollziehbare Fokusführung, eine geeignete Schließaktion und Fokus-Rückgabe. Information wird nie ausschließlich über Farbe, Position, Hover oder Bewegung vermittelt.

Fokussierte Elemente dürfen nicht vollständig durch eigene fixierte Flächen oder Überlagerungen verdeckt werden. Ziele für Zeigerbedienung erfüllen die zutreffenden WCAG-Regeln zu Größe beziehungsweise Abstand einschließlich ihrer Ausnahmen; das sichtbare Icon allein beschreibt nicht zwingend die bedienbare Fläche.

`prefers-reduced-motion` und statische Alternativen werden unterstützt. Kein Scroll-Hijacking, Cursor-Ersatz, Autoplay-Ton, blockierendes Intro oder zeitkritischer Kernablauf ohne Alternative. Automatisierte Prüfungen ergänzen gezielte manuelle Tastatur-, Zoom- und Screenreader-Prüfungen.

## Performance und Nachweis

Medien besitzen geeignete Dimensionen und belastbare Fallbacks. Effekte werden nur geladen, wenn ihr sichtbarer Nutzen die Kosten trägt, und blockieren weder Interaktion noch Lesbarkeit. Performance- und Accessibility-Budgets brauchen Methode und reale Messumgebung; Regressionen werden nicht durch gelockerte Grenzwerte verdeckt.

Gemäß [Testpyramide und Testpflege](testing.md) schützen Unit- und Integrationstests das relevante UI-Verhalten und Feature-Zusammenspiel. E2E bleibt auf wenige häufig wiederholte zentrale Nutzerwege mit zusätzlichem Integrationsrisiko begrenzt. Visuelle Regressionstests benötigen einen ausdrücklich stabilen visuellen Vertrag. Tests für Textinventare, Layoutpositionen oder Frameworkverhalten sind kein Standard.

## Prototypen

Ein Prototyp benennt ausführbare Ansichten, simulierte Zustände, Speicherverhalten und Prüfgrenzen im zugehörigen Ticket. Simulierte Anmeldung, getrennte Ansichten, Formulare oder Dateien beweisen weder Autorisierung noch Zustellung, Persistenz oder sichere Dateiverwaltung. Synthetische Daten und Assets mit belegten Rechten sind der Default. Lokale Prototypdateien bleiben temporär außerhalb des Checkouts. Darstellung und Prüfung erfolgen bei Bedarf mit vorhandenen Werkzeugen im laufenden Container; dafür werden weder Projektinfrastruktur noch öffentliche Hostingwege eingerichtet.
