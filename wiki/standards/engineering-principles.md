---
type: Policy
title: Engineering-Prinzipien
description: KISS, Modularisierung, DRY, Lokalität, Information Hiding und risikogerechte Nachweise.
tags:
- shared
- engineering-principles
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/engineering-principles.md
  title: 'Vorlage vor der Wiki-Migration: standards/engineering-principles.md'
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# Engineering-Prinzipien

Diese Prinzipien helfen bei technischen Entscheidungen. Sie sind keine mechanische Checkliste: Regeln können einander widersprechen, und die passende Gewichtung hängt von Problem, Änderungswahrscheinlichkeit, Risiko und Projektgröße ab. Eine Abweichung ist erlaubt, wenn ihre Konsequenzen verstanden und die Entscheidung nachvollziehbar ist.

## Entscheidungsprinzipien

### KISS und gegenwärtiger Bedarf

Wähle die einfachste verständliche Lösung, die das aktuelle Problem und seine realen Risiken vollständig trägt. Baue keine Erweiterungspunkte, Infrastruktur oder Varianten auf Vorrat. Einfach bedeutet nicht provisorisch: notwendige Fehler-, Sicherheits- und Datenintegritätsgrenzen gehören zur vollständigen Lösung.

### Qualität, Nachweis und Infrastruktur

Trenne die geforderte Produkteigenschaft, den dafür geeigneten Nachweis und die Infrastruktur, die diesen Nachweis ausführt. Ein Qualitätsanspruch begründet für sich keine CI, gehostete Vorschau, Hosting-, Deployment- oder Delivery-Infrastruktur. Solche Fähigkeiten benötigen einen konkreten gegenwärtigen Bedarf, eine bewusste Architekturentscheidung und eine reale Implementierung.

Qualitätsgates verlangen reproduzierbare Prüfungen und eindeutige Evidenz zum geprüften Stand. Der gemeinsame lokale Entwicklerweg steht in [Lokale Entwicklung](local-development.md), konkrete Projektbefehle in [Projektspezifische Entwicklung](../project/local-development.md); tatsächlich vorhandene Auslieferungs- und Betriebswege stehen in [Projektbetrieb](../project/deployment.md). Änderungsnachweise und Pull Requests kopieren diese globalen Verträge nicht, sondern dokumentieren nur den konkreten Nachweis. Keine Produktprüfung und kein Projektstart wird an den Dev-Container-Start gekoppelt.

### Zerlegung und Modularisierung

Teile komplexe Probleme an fachlich stabilen Grenzen. Ein Modul besitzt eine klar abgegrenzte Verantwortung und eine kleine definierte Schnittstelle. Innerhalb eines Moduls ist hohe Kohäsion erwünscht; zwischen Modulen geringe Kopplung. Abhängigkeiten bleiben gerichtet und azyklisch.

### Abstraktion und DRY

Abstraktion hebt gemeinsames Wissen hervor. Sie lohnt sich, wenn mehrere reale Fälle dieselbe fachliche Regel teilen oder vorhandene Komplexität dadurch sinkt. Ähnlich aussehende Codezeilen allein sind kein Abstraktionsgrund.

DRY bedeutet, dass jedes Wissen eine eindeutige maßgebliche Repräsentation besitzt. Manuell synchronisierte Kopien werden vermieden. DRY verlangt weder einen Generator für statische Inhalte noch eine gemeinsame Abstraktion für zufällig ähnliche Details.

### Lokalität und Information Hiding

Informationen, die zusammen geändert und nur gemeinsam verwendet werden, liegen beieinander. Statischer View-Content gehört standardmäßig zur View oder zum typisierten Feature-Code. Ein separates Contentmodell benötigt einen unabhängigen Redaktions-, Freigabe-, Übersetzungs- oder Wiederverwendungszyklus.

Module zeigen nur die Schnittstelle, die ihre Nutzer brauchen. Veränderliche, komplexe oder sensible Details werden gekapselt, damit ihre Änderung keine unnötigen Ripple Effects erzeugt.

### Komposition und Domänenmodell

Modelle verwenden Begriffe und Verantwortungen der Problemdomäne. Objekte und Komponenten erledigen ihre eigene Aufgabe, statt als passive Datenbehälter von zentralen Manager-Konstrukten gesteuert zu werden. Komposition und Delegation sind der Default; Vererbung braucht eine echte stabile Ist-ein-Beziehung.

### Standards und Werkzeuge

Konventionen von Sprache, Framework und Repository werden einheitlich angewendet. Compiler, Linter, Test Runner und etablierte Plugins haben Vorrang vor eigenen Prüfprogrammen. Ein eigenes Tool ist nur gerechtfertigt, wenn eine konkrete, nicht anderweitig abdeckbare Lücke besteht und Nutzen, Verantwortlichkeit sowie Entfernungskriterium dokumentiert sind.

Tools unterstützen eine Methode; ihre Existenz beweist keine Qualität. Ebenso ist ein Test kein Wert an sich, sondern eine kostengünstige Absicherung eines benannten Risikos.

### Integrierte Dokumentation

Software besteht aus ausführbarem Verhalten und der Dokumentation, die ihre Nutzung und Weiterentwicklung ermöglicht. Der [Documentation Writer](documentation.md) führt technische Dokumentation und Benutzerhandbuch im Story-PR und pflegt sie regelmäßig anhand der von TL und PO verantworteten Entscheidungen. Der Developer nutzt die Dokumentation als Verständnisgrundlage für seine Implementierung. Dokumentation erklärt Einstieg, Zusammenhänge und Bedienung, ohne Code oder Ticketverlauf abzuschreiben.

### Planungs- und Dokumentationsgrenze

Die [Governance](governance.md#allgemeine-regeln-projektkontext-und-planung) ist die maßgebliche Quelle für allgemeine Regeln, dauerhaften Projektkontext und GitHub-Planung. Ihre [Artefaktgrenzen](governance.md#planungsartefakte-und-dauerhafte-dokumentation) gelten auch für technische Zeichnungen, Mockups und temporäre Dateien.

## Verantwortung im Prozess

Entscheidungsbefugnisse und Rollenfolge stehen im [Entwicklungsprozess](development-process.md#inhalte-und-zuständigkeiten) und den dort verlinkten Rollenverträgen. Lokale Implementierungsdetails und Testpflege liegen beim Developer innerhalb des bestätigten Plans; das unabhängige Review prüft gegen den vereinbarten Maßstab.

## Grundlagen

- [Softwareentwicklungs-Prinzipien: Eine Übersicht](https://www.christian-rehn.de/2011/05/14/softwareentwicklungs-prinzipien-eine-ubersicht/)
- [Allgemeine Prinzipien bei der Entwicklung von Softwaresystemen](http://spolwig.de/is/softwareprojekte/prinzipien.htm)
