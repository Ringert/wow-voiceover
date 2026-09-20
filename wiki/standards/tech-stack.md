---
type: Policy
title: Stackentscheidungen
description: Auswahl, bestätigte Kerntechnologien, Quellen, Versionen und Wartbarkeit.
tags:
- shared
- tech-stack
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/tech-stack.md
  title: 'Vorlage vor der Wiki-Migration: standards/tech-stack.md'
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# Stackentscheidungen

Die Vorlage legt keine Programmiersprache, kein Frontendframework und keine Datenbank fest. Bestätigte Kerntechnologien eines abgeleiteten Projekts stehen in [Projekt-Tech-Stack](../project/tech-stack.md) und werden nicht stillschweigend neu zur Wahl gestellt. Versionen, Integrationen und unterstützende Komponenten werden innerhalb dieser Grenze bedarfsgerecht entschieden.

## Auswahlregeln

- Wähle die kleinste wartbare Werkzeugkombination, die den belegten Bedarf und seine Schutzgrenzen abdeckt. Bestehende Frameworkfähigkeiten und etablierte Werkzeuge haben Vorrang vor eigenem Infrastrukturcode.
- Prüfe unterstützte Versionen, Kompatibilität, Lizenzen, Sicherheitslage und Betriebsanforderungen anhand aktueller offizieller Quellen mit Abrufdatum. Eine historische Paketliste oder Referenzsammlung begründet keine Technologiewahl.
- Verwende aktiv gepflegte Bibliotheken für sicherheitskritische Funktionen, Sessions und Kryptografie. Keine Eigenimplementierung ohne ausdrückliche, fachlich belastbare Notwendigkeit.
- Verwende genau ein maßgebliches Locking-Verfahren je installierbarer Einheit. Exakte Paketauflösungen gehören in Lockdateien, Image- und Runtime-Versionen in die verantworteten Projektkonfigurationen. Versionslisten in Fließtext dürfen keine zweite manuell synchronisierte Wahrheit schaffen.
- Halte Transaktionen, Migrationen, Berechtigungen, Datenisolation und Fehlerdiagnose verständlich. Ein kleines Team muss Updates und den tatsächlichen Betriebsweg warten können.
- Build und lokale Tests benötigen standardmäßig keine persönlichen Produktivkonten. Notwendige Integrationskonten werden als konkrete Abhängigkeit getrennt beschrieben, nicht stillschweigend vorausgesetzt.
- Prüfe Runtime- und Abhängigkeitsänderungen in der tatsächlich verwendeten Containerumgebung. Eine Installation allein belegt keine Kompatibilität. Auditbefunde werden nach realem Einsatz bewertet; nicht durch pauschale Ausnahmen oder erzwungene Major-Overrides kaschieren.
- Bei öffentlich indexierbaren Webinhalten muss die Renderingentscheidung Inhalt, Auffindbarkeit und Performance tragen. Geschützte Daten bleiben aus gemeinsam genutzten Rendering-Caches ausgeschlossen.

## Ablage und Ausführung

Jede bestätigte Stackentscheidung und relevante Änderung ihrer Versionen löst den gezielten [Skill-Abgleich](skills.md) aus. Belege die Abdeckung bestätigter Technologien durch vorhandene geeignete Regeln/Werkzeuge oder tatsächlich benötigte zusätzliche Skills. Recherchiere und installiere fehlende Skills vor davon abhängiger Umsetzung. Ein bisher offener Stack wird nicht allein durch Rollenabdeckung oder einen neuen Statustext vollständig.

Die Entscheidung bis zur Implementierung gehört in das technische GitHub-Artefakt. Tatsächlich eingesetzte Werkzeuge und ihre maßgeblichen Konfigurationsdateien werden danach im Projektkontext dokumentiert. Die Linux-/Docker-Basis ist davon unabhängig: Sprachlaufzeiten, Buildwerkzeuge und benötigte Dienste werden in Projektimages bereitgestellt. Zusätzliche persönliche Werkzeuge installiert man bei Bedarf im laufenden Dev Container. `.devcontainer/` bleibt unverändert.
