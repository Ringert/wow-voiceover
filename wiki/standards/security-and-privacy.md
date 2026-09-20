---
type: Policy
title: Sicherheit und Datenschutz
description: Zugriff, Daten, Secrets, Testisolation und Wiederherstellung.
tags:
- shared
- security-and-privacy
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/security-and-privacy.md
  title: 'Vorlage vor der Wiki-Migration: standards/security-and-privacy.md'
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# Sicherheit und Datenschutz

Schutzmaßnahmen richten sich nach den tatsächlichen Daten, Akteuren und Operationen. Diese Regeln schaffen keine Pflicht, Konten, Uploads, Mandanten oder Telemetrie einzuführen. Konkrete Schutzwerte, Vertrauensbereiche und implementierte Kontrollen stehen in [Projektsicherheit](../project/security-and-privacy.md); geplante Kontrollen im technischen GitHub-Artefakt.

## Zugriff und Datenintegrität

- Standard für geschützte Operationen ist Verweigerung. Identität, Rolle und konkrete Objekt-/Kontextzuordnung werden bei jeder Operation auf der vertrauenswürdigen Seite geprüft. Versteckte UI-Elemente ersetzen keine Autorisierung.
- Listen, Suche, Zähler, Exporte, Dateien, Caches und Fehler verraten keine fremden oder internen Daten. Bei Kontextisolation prüfen Tests mindestens zwei getrennte Kontexte und die tatsächlich relevanten Rollen, einschließlich direkter IDs und abgeleiteter Datenwege.
- Registrierung, Einladung, Recovery und administrative Aktionen folgen dem fachlich entschiedenen Berechtigungsmodell. Eine Anmeldung verleiht nicht automatisch privilegierte Rechte. Loginfehler verraten keine vorhandenen Konten.
- Sessionfixation, CSRF, Replay und automatisierte Versuche werden entsprechend dem Threat Model begrenzt. Sperrung und Berechtigungsentzug beenden betroffene Zugriffe. Besonders wirksame administrative Aktionen erhalten passende zusätzliche Absicherung.
- Eingaben werden begrenzt und auf der vertrauenswürdigen Seite validiert, Ausgaben kontextgerecht kodiert, Datenzugriffe parametrisiert. Sicherheitsheader, Cookieattribute, Origin-Prüfung und Proxy-Vertrauen folgen dem realen Betriebsmodell.
- Speichern, Freigeben und Zustellen sind unterscheidbare Vorgänge. Konkurrenz und Wiederholung dürfen keine unbemerkten Überschreibungen, falschen Freigaben oder doppelten Geschäftsvorgänge erzeugen.
- Uploads erhalten begründete Größen-, Typ- und Inhaltskontrollen. Private Dateien liegen außerhalb öffentlich ausgelieferter Verzeichnisse; Downloads prüfen die aktuelle Berechtigung.

## Daten, Secrets und Testumgebung

Secrets, private Nachweise, Sessions und vertrauliche Inhalte erscheinen nicht in versionierten Dateien, öffentlichen Builds, URLs, Telemetrie oder unredigierten Logs. Konfigurationsfehler benennen Feld und Fehlerklasse, ohne sensible Werte auszugeben. Secrets liegen in geeigneten lokalen Speicherorten oder Secret-Verwaltung, getrennt von Quelltext und abhängig von den tatsächlichen Dateisystemrechten. Vorlagen dürfen sichere Variablennamen, aber keine echten Zugangsdaten enthalten.

Entwicklung und Tests verwenden synthetische Identitäten, fachliche Daten und Empfänger. Eine freigegebene redaktionelle Tatsache ist davon getrennt und unterliegt ihrer Quellen-/Verwendungsgrenze. Ein lokaler Mail- oder anderer Zustelladapter muss reale externe Zustellung verhindern, wenn diese nicht ausdrücklich beauftragt ist.

Testdaten, Entwicklungsdaten und Betriebsdaten sind getrennt. Destruktive Testvorbereitung muss das konkrete isolierte Ziel prüfen und darf nie still auf einen Entwicklungs- oder Produktionsbestand ausweichen. Eine belegbar notwendige Testabhängigkeit, die fehlt, wird als fehlender Nachweis gemeldet; Fehler werden nicht durch Skip, längere Timeouts oder schwächere Assertions verdeckt. Bereits vorhandene Daten und gültige Zugangsdaten bleiben bei wiederholtem Setup erhalten.

## Threat Model und Betriebsreife

Der Entwurf betrachtet relevante Missbrauchswege wie Identitätsdiebstahl, Rechteausweitung, Datenlecks, manipulierte Freigaben, schädliche Dateien, Spam, Secrets in Artefakten und Datenverlust. Jede notwendige Kontrolle hat eine benannte Grundlage und eine aussagekräftige Prüfung. Es gibt keine vollständige Kontrollmatrix allein der Vollständigkeit halber.

Vor realer Verarbeitung werden Datenkategorien, Zwecke, Empfänger, Berechtigungen, Dienstleister, Aufbewahrung, Export, Berichtigung, Löschung und Restrisiken geklärt. Nicht notwendige Tracker, Werbenetzwerke und Marketingcookies sind kein Default. Öffentliche Nutzungsanalyse und vertrauliche operative Telemetrie werden getrennt behandelt.

Migrationen, Sicherung und Wiederherstellung besitzen einen praktisch geprüften isolierten Weg. Persistenz, ein erfolgreiches Backupkommando oder ein grüner Build allein beweisen keine Wiederherstellbarkeit. Betriebs- und Veröffentlichungsgates folgen [Governance](governance.md) und [Betrieb](deployment.md).

## Persönlicher Werkzeugzustand

Der vollständige Benutzerzustand bleibt außerhalb der Repositoryquellen im dafür vorgesehenen Volume. Dazu gehören auch Verlaufsdateien, Indizes, Datenbanken, Erweiterungen und persönliche Einstellungen. Bei einem bewusst geplanten Eingriff werden tatsächliche Mountquellen und zusammengehörige Dateien erhalten. Sicherungen sind vertraulich. Der [lokale Entwicklervertrag](local-development.md#persistenter-zustand) beschreibt die Ablage; kein Start-Hook prüft, kopiert oder repariert sie.
