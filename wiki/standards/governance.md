---
type: Policy
title: Governance und Freigaben
description: Quellenstatus, Dokumentationsgrenzen, reale Daten und Veröffentlichungsfreigabe.
tags:
- shared
- governance
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/governance.md
  title: 'Vorlage vor der Wiki-Migration: standards/governance.md'
- id: wiki-pattern
  resource: ../sources/llm-wiki.md
- id: wiki-format
  resource: ../sources/open-knowledge-format.md
generated:
  by: codex/gpt-6
  at: '2026-09-14T22:11:03Z'
---
# Governance und Freigaben

## Allgemeine Regeln, Projektkontext und Planung

`wiki/standards/` und `AGENTS.md` enthalten die gemeinsamen Regeln aller Projekte. [Wiki-Schema und Pflegevertrag](../schema.md) regeln die Wissensbasis; auch sie werden nur im ausdrücklichen Pflegeauftrag geändert. `wiki/project/` enthält ausschließlich den langlebigen Kontext eines konkreten Projekts. Unbekannte Werte bleiben **To be defined**; sie werden weder durch plausible Geschäftsangaben noch durch Behauptungen über implementierte Fähigkeiten ersetzt. Eine nicht benötigte Kategorie darf mit begründetem „Nicht zutreffend“ geklärt werden.

Neue Projektnamen, Rollenmodelle, Stackvorgaben, Domains und Betriebsziele dürfen gemeinsame Regeln nicht verändern. Bestätigte Projektentscheidungen werden mit ihrer Quelle und Geltungsgrenze dokumentiert. Ein Neubeginn oder eine technische Umstrukturierung widerruft eine vorhandene Tatsachen- oder Inhaltsfreigabe nicht automatisch.

GitHub ist die einzige Quelle für Roadmap, Release-Scope, Lieferphasen, Milestones, Prioritäten, Reihenfolge, Abhängigkeiten, Status und Ticketchronik. Das LLM Wiki erklärt dauerhafte Produktziele, tatsächlichen Bestand und Bedienung. Seine Synthesen verknüpfen maßgebliche Detailseiten; Quellenzusammenfassungen belegen Herkunft und Geltungsgrenzen. GitHub-Artefakte enthalten keine Agentenanweisungen, Goals oder Chatprotokolle.

## Planungsartefakte und dauerhafte Dokumentation

Die Codebasis enthält benötigten Produktcode, Tests, Projektkonfiguration und dauerhaft nützliches Wiki-Wissen. Das [Wiki-Log](../log.md) darf wesentliche Änderungen dieses Wissens mit Seitenbezug festhalten, aber keine Arbeitsnotizen, Suchchronik, Rollenübergaben oder Projektstatus. Planungsdateien, Arbeitsnotizen, Mockups, Wireframes, Gestaltungsprototypen und ihre Quellen oder Exporte werden nicht ins Repository oder in einen Story-Branch übernommen. Das gilt für alle Rollen und auch für Ablagen unter `wiki/`; ein ignorierter Projektordner ist kein Ersatz für diese Trennung.

Die [Skill-Regel](skills.md) erlaubt ausdrücklich den lokalen, von Git ignorierten Werkzeugcache `.codex/skills-check.json` und die nötigen lokalen Suchpfad-Verweise unter `.agents/skills/`. Der Cache enthält ausschließlich Skill-Auswahl, Quellen, Installations- und Aktualitätsnachweise; er wird nicht in neue Projekte übernommen und enthält keine Roadmap-, Goal-, Story- oder Rollenübergabestatus. Die tatsächlich verwendeten gemeinsamen Skill-Dateien unter `.codex/skills/` sind versionierte Projektwerkzeuge. Diese begrenzte Ausnahme erlaubt keine weiteren Arbeits- oder Planungsablagen im Checkout.

Entwürfe und technische Planungszeichnungen wie UML, Ablauf- oder Sequenzdiagramme gehören zum zugehörigen GitHub-Ticket: direkt in dessen Beschreibung, als Anhang oder als eindeutig referenzierte Fassung in einer für das Projekt vorgesehenen externen Ablage. Lokal benötigte Arbeitsdateien entstehen in einem aufgabenbezogenen temporären Verzeichnis außerhalb des Checkouts. Ohne passende Uploadmöglichkeit werden die vorbereiteten Dateien und ihr genauer Ablageort übergeben; ein lokaler Pfad wird nicht als veröffentlichter Anhang ausgegeben und die Codebasis dient nicht als Ausweichablage. Eigene temporäre Dateien werden nach gesicherter Ablage beziehungsweise abgeschlossener Nutzung aufgeräumt; noch benötigte einzige Kopien und fremde Dateien bleiben erhalten.

UML und andere Zeichnungen dürfen Teil der Repository-Dokumentation sein, wenn sie den tatsächlich umgesetzten Architektur-, Fach- oder Betriebsbestand erklären und über das Ticket hinaus einen konkreten Nutzen haben. Halte sie mit dem Bestand aktuell und vermeide doppelte Quelldateien oder Exporte ohne Nutzen. Dauerhafte Gestaltungsregeln werden mit ihrer Implementierung im Projekt-UI-Leitfaden dokumentiert; Mockups werden dadurch nicht zu Bestandsdokumentation. Tatsächlich verwendete Produktassets bleiben reguläre Projektdateien. Die Abgrenzung richtet sich nach dem Zweck, nicht nach dem Dateiformat.

Verantwortung, Inhalt, regelmäßige Pflege und Prüfung von technischer Dokumentation und Benutzerhandbuch sind im [Dokumentationsstandard](documentation.md) gebündelt. Beide gehören zum gemeinsamen Storyabschluss; Planungsdateien werden dafür nicht übernommen.

## Eigenständiger Entscheidungsspielraum

Innerhalb des beauftragten Ziels und bestätigter Grenzen dürfen zuständige Rollen reversible Details zu Text, Informationsstruktur, Interaktion und Technik selbst entscheiden. Sichere synthetische Entwürfe und neutrale Platzhalter erlauben Fortschritt, während externe Tatsachen offen sind. Es ist keine persönliche Geschmacksfreigabe für jeden Satz oder Designwert erforderlich.

Identität, vertrauliche Daten, Rechtsbewertungen, Kennzahlen, Zertifizierungen, Kunden- oder Medienrechte sowie verbindliche Geschäftsbedingungen werden nicht erfunden. Benötigt eine konkrete Aktion eine noch fehlende externe Entscheidung, bleibt diese Aktion offen; unabhängige Entwicklung geht weiter. Bereits erteilte, passende Autorisierung wird nicht erneut angefordert.

## Inhalts- und Quellenstatus

| Status | Verwendung |
| --- | --- |
| Arbeitsentwurf | Nicht öffentliches Entwurfsartefakt; vor Veröffentlichung prüfen |
| Quellenbasiert | Tatsachenbezug ist belegt; zulässiger Zweck und Zielkanal bleiben durch die Quelle begrenzt |
| Freigegeben | Inhalt, Quelle, Rechte und konkreter Verwendungszweck sind bestätigt |
| Gesperrt | Keine Übernahme in öffentliche Artefakte, Demos, Metadaten oder Testfixtures |

Eine bestätigte Tatsache verleiht keine Rechte an begleitenden Logos, Bildern, Screenshots oder Zitaten. Anonymisierung ersetzt weder Tatsachenbeleg noch Medienrechte. Private Originalbelege bleiben außerhalb des Repositories; im Projektkontext stehen nur geeignete Evidenzreferenzen. Interne Prüfmarker und Freigabehinweise gehören nicht in Produktoberflächen oder öffentliche Builds.

## Technische Qualität und Veröffentlichung

Eine Fassung kann in einer nicht öffentlichen Umgebung mit synthetischen Daten fachlich und technisch abgenommen werden. Ein erfolgreicher Build, Merge oder lokaler Compose-Start erteilt keine Veröffentlichungs- oder Betriebsfreigabe. Öffentliche Bereitstellung, produktive Datenverarbeitung und reale externe Kommunikation werden nur im passend autorisierten Auftrag ausgelöst.

Vor einer Veröffentlichung werden die für das reale Produkt zutreffenden Punkte überprüft:

- verantwortliche Identität, Geschäftsbezeichnung, Domains und Kontaktwege;
- Pflichtinformationen, Datenschutz und gegebenenfalls Vertrags-/Verbraucherinformationen für die tatsächliche Rechtsordnung und Betriebsform;
- veröffentlichte Behauptungen, Leistungszusagen, Medienrechte und relevante Lizenzen;
- tatsächlich verwendete Hosting-, Kommunikations-, Datei-, Identitäts-, Logging- und Analysedienste;
- Kernabläufe mit finalen Inhalten, Accessibility, Sicherheit sowie angemessene Backup-, Restore- und Rollback-Evidenz;
- bei öffentlichen Webprodukten erreichbare Kontaktwege, TLS, zutreffende Metadaten, Canonical Host und bewusst gesteuerte Indexierung;
- Ausschluss privater oder interner Inhalte und unbeabsichtigt veröffentlichter synthetischer Daten.

Fehlende notwendige Bestätigungen sperren die davon abhängige Veröffentlichung oder reale Verarbeitung. Sie sind kein Grund, bereits korrekte technische Arbeit zurückzubauen. Rechts- und Betriebsvoraussetzungen werden für das konkrete Projekt aus aktuellen Primärquellen geklärt; keine Übernahme fremder Unternehmens-, Steuer- oder Rechtsannahmen.

## Erfolgsmessung

Erfolgskriterien folgen dem konkreten Nutzer-/Geschäftsergebnis. Messwerte erhalten erst verbindliche Ziele, wenn Methode, Umgebung und Verantwortlichkeit feststehen. Technische Kriterien betreffen die tatsächlich erforderlichen Kernpfade, Bedienbarkeit, Performance, Schutzgrenzen und Wiederherstellbarkeit. Invasive Analyse oder reine Reichweitenzahlen werden nicht zur Vervollständigung einer Checkliste eingeführt.
