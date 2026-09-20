---
type: Policy
title: Architekturregeln
description: Verantwortungen, Vertrauensgrenzen, Datenintegrität und dokumentierter Bestand.
tags:
- shared
- architecture
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/architecture.md
  title: 'Vorlage vor der Wiki-Migration: standards/architecture.md'
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# Architekturregeln

Architektur folgt dem aktuellen fachlichen Bedarf und den [Engineering-Prinzipien](engineering-principles.md). Sie setzt keinen Anwendungsstil, kein Framework und keine Aufteilung in Dienste voraus. Bestätigte Kerntechnologien des Projekts sind einzuhalten; die Vorlage selbst legt keinen Produktstack fest.

## Verantwortung und Systemgrenzen

Jeder fachliche Bereich besitzt eine erkennbare Verantwortung, begrenzte Schnittstellen und eine maßgebliche Datenquelle. Domänenbegriffe werden im [Projektmodell](../project/domain-model.md) gepflegt. Fachliche Grenzen, UI-Ansichten, Prozesse und physisch getrennte Dienste sind unterschiedliche Entscheidungen. Ein zusätzlicher Dienst oder Datenspeicher braucht einen belegten Schutz-, Skalierungs- oder Betriebsbedarf.

Öffentliche, interne und anderen Identitäten zugeordnete Daten bleiben getrennt. Der vertrauenswürdige Anwendungskern entscheidet über geschützte Operationen; ein getrennter Bildschirm schafft keine Autorisierungsgrenze. Externe Systeme erhalten explizite Verträge und getrennte Konfiguration. Ist ein externes System führend, stellt eine lokale Kopie oder Referenz keinen Ersatz für dessen fachliche Verantwortung dar.

## Invarianten bei entsprechenden Fähigkeiten

- Geschützte Aktionen prüfen Identität, Berechtigung und konkretes Objekt auf der vertrauenswürdigen Seite; abgeleitete Listen, Suche, Exporte, Dateien und Caches halten dieselbe Grenze ein.
- Interne Entwürfe gelangen nicht durch Speichern in öffentliche oder für andere Personen freigegebene Ansichten. Eine Freigabe beschreibt Empfänger, Umfang und eine eindeutig gespeicherte Fassung.
- Gleichzeitige Änderungen dürfen keine unbemerkten Überschreibungen erzeugen. Fachliche Zustandsübergänge erhalten verständliche Vorbedingungen und Fehlerfolgen.
- Fachlicher Speichervorgang und nachgelagerte Zustellung haben unterscheidbare Ergebnisse. Bei unklarem Ausgang wird vor einer Wiederholung der Zustand abgeglichen; notwendige Idempotenz verhindert doppelte Verarbeitung.
- Archivierung, Löschung, Aufbewahrung, Freigabe und Zugangsentzug sind verschiedene Vorgänge. Ihre Folgen werden fachlich entschieden und nicht stillschweigend miteinander gekoppelt.
- Private Dateien werden vor ihrer Auslieferung frisch autorisiert. Browser- oder andere unvertrauenswürdige Clients importieren keine Datenbank-, Session- oder Secretmodule.
- Schema-/Migrationsrechte und normale Anwendungsrechte werden nach Bedarf getrennt. Reale Daten benötigen einen praktisch geprüften Migrations-, Sicherungs- und Wiederherstellungsweg.
- Liveness beschreibt Prozessfähigkeit; Readiness die für einen konkreten Dienst notwendige Betriebsbereitschaft. Eine unbenötigte externe Abhängigkeit soll keine unabhängige Fähigkeit blockieren.

## Entscheidung und dokumentierter Bestand

Der [Tech Lead](tech-lead.md) untersucht den realen Bestand und betroffene Abhängigkeiten und entscheidet die Lösung einschließlich Qualitätsleitplanken und Risiko-/Testzuordnung in GitHub. Die technische Ausarbeitung verbindet diese Entscheidung mit konkreten Einstiegshilfen und einem Implementierungsplan. Eine Entscheidung ist eine Umsetzungsvorgabe, noch kein Implementierungsnachweis. [Projektarchitektur](../project/architecture.md) beschreibt nur tatsächlich umgesetzte Grenzen, Komponenten, Schnittstellen, Datenflüsse und relevante Einschränkungen. Geplante Routen, Tabellen, Befehle oder Dateipfade werden dort nicht als vorhanden dargestellt.

Die Entwicklungsumgebung folgt immer der unveränderten [Containerbasis und dem manuellen Compose-Vertrag](local-development.md). Projekterfordernisse rechtfertigen keine Änderung der Dev-Container-Konfiguration.

Der Documentation Writer schreibt und pflegt die technische Bestandsdokumentation im Story-PR gemäß [Dokumentationsstandard](documentation.md); der Tech Lead bleibt für technische Entscheidungen verantwortlich. Grundkonzepte, Architekturentscheidungen und das Zusammenspiel wesentlicher Bausteine stehen im Mittelpunkt; Quellcodeverweise und gezielte Diagramme ergänzen die Erklärung. Die vollständige Kopie von Klassen, API-Feldern oder Planung ist keine Architekturübersicht.
