---
type: "Policy"
title: "Lokale Entwicklung"
description: "Feste Arbeitsbasis, manueller Dienststart und nachvollziehbare Werkzeug- und Datenhaltung."
tags: ["shared", "wow-voiceover"]
status: "stable"
scope: "shared"
sources:
  - id: template
    resource: "https://github.com/Ringert/Codex-Projektvorlage/blob/b001e1b700d75aa0f31f6ced84381ba194b79582/wiki/standards/local-development.md"
  - id: project
    resource: "../project/local-development.md"
  - id: container
    resource: "../../.devcontainer/devcontainer.json"
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Lokale Entwicklung

## Feste Containerbasis

Die Vorlage trennt Arbeitscontainer und Produktdienste. Für dieses bestehende Projekt bleibt der bereits vorhandene Python-Devcontainer die feste Basis. Sein tatsächlicher Aufbau ist in [Projektentwicklung](../project/local-development.md) und der [Containeranleitung](../../.devcontainer/README.md) beschrieben. Die Debian-/Docker-in-Docker-Basis der Vorlage wird nicht als vorhandene Infrastruktur behauptet oder darüberkopiert.

**`.devcontainer/` bleibt während normaler Projektentwicklung unverändert.** Änderungen daran benötigen einen ausdrücklich passenden Einrichtungs-/Pflegeauftrag. Keine Umgehung über alternative Containerdateien, Shellprofile, Editor-Tasks oder Lifecycle-Hooks. Der normale Containerstart installiert und prüft nichts, koppelt kein Konto und startet weder Anwendung, Datenbank, Generierung noch Kommunikationsdienste. Vorhandene Abhängigkeiten werden im Imagebuild reproduzierbar bereitgestellt.

## Vertrag für das Projektsetup

Produktabhängigkeiten gehören in nachvollziehbare Manifeste und das beauftragte Projektsetup. Keine zufällig installierte persönliche Umgebung als Projektvoraussetzung darstellen. Die tatsächlichen Befehle und Grenzen stehen in [Projektentwicklung](../project/local-development.md); ein nicht vorhandener Compose-Dienst wird nicht als nutzbarer Einstieg dokumentiert.

`docker compose up -d` ist ein **manueller** Dienststart. Hier startet die vorhandene Root-Datei `docker-compose.yml` nur MySQL vom Host; TTS bleibt ein separater Dienst. Eine Migration auf ein vollständiges inneres Compose-Netz erfordert eine konkrete Entscheidung zu Laufzeit, Erreichbarkeit und bestehenden Daten. Die bestehende Datei nicht durch eine konkurrierende `compose.yaml` verdecken.

Für neue oder bewusst überarbeitete Entwicklungsdienste gelten die übernommenen Standards:

- `restart: "no"`, keine automatische Anwendung beim Container-/Daemonstart.
- Benannte Projektvolumes für Daten; keine globalen Ressourcennamen oder festen `container_name` ohne belegten Altbestandsbedarf.
- Interne Servicenamen und Ports für Dienstkommunikation. Bereitschaftsprüfungen nur für echte Abhängigkeiten; Tests bleiben eigene Befehle.
- Keine zusätzlichen `ports`, Host-Netzwerke, Host-Docker-Socket-Mounts oder automatisch generierten Host-Overrides.
- Schreibende Werkzeuge müssen brauchbare Dateirechte im Checkout erhalten.
- Datenbestand, Import- und Fehlerverhalten bei einer Änderung ausdrücklich berücksichtigen; keine ungeprüften destruktiven Initialisierungen.

Die vorhandene MySQL-Hostbindung und der Containername sind [dokumentierter Altbestand](../project/local-development.md#dienste-und-konfiguration), keine Empfehlung für neue Dienste. Ein Anwendungsfehler wird an seiner tatsächlichen Konfigurations-/Codegrenze behoben, nicht durch einen versteckten Containerstart-Hook.

## Zusätzliche Werkzeuge und Codex

Werkzeuge dürfen im laufenden Container bei konkretem Bedarf manuell installiert werden. Erforderliche Prüfwerkzeuge und ihre Versionen werden im Änderungsnachweis benannt. Ein Rebuild kann manuell installierte Systempakete entfernen; daraus entsteht kein Auftrag zur heimlichen Änderung der Containerbasis. Sprachabhängigkeiten bleiben im Projektmanifest beziehungsweise in einer ausdrücklich vorgesehenen Werkzeugumgebung.

Die GitHub CLI und die Codex-VS-Code-Erweiterung sind im bestehenden Setup vorgesehen. Persönliche Anmeldung und Projektvertrauen werden nicht aus Dateivorhandensein abgeleitet. Die [Projektkonfiguration](../../.codex/config.toml) und [Agentenrollen](../../.codex/agents/) benötigen eine passende Codex-Laufzeit und tatsächlich bestätigte Erkennung. Der [GitHub-Leitfaden](../project/github-workflow.md) nennt die Aktivierung und Prüfgrenzen.

Zusätzliche Skills folgen [skills.md](skills.md): konkrete Fähigkeitslücke, geprüfte Quelle, vollständige Installation und tatsächliche Erkennung. Projektlokale Skills, ignorierter Prüfstatus und Suchpfad-Verweise bleiben getrennt. Ohne Lücke keine Skillinstallation auf Vorrat. Signal ist nach [signal-integration.md](signal-integration.md) hier nicht eingerichtet.

## Ports und Hostzugriff

Nur Login-Port **1455** ist fest in VS Code weitergeleitet. Automatische Porterkennung und Wiederherstellung bleiben deaktiviert. Manuelle Hoststarts und gewünschte temporäre Weiterleitungen erfolgen bewusst; Agenten erzeugen keine zusätzliche dauerhafte Portkonfiguration. Host- und Container-`localhost` bezeichnen unterschiedliche Netzwerkräume.

## Persistenter Zustand

Quelltext ist der eingebundene Checkout. Das bestehende projektspezifische Home-Volume enthält Codex-, GitHub- und VS-Code-Zustand; Datenbankdateien liegen im benannten Compose-Volume. Der tatsächliche Mountpfad und Volumename sind vor einer Migration zu prüfen. Andere Checkout-Pfade oder ein anderer Docker-Daemon können andere Volumes verwenden.

Persistenz ist kein Backup. Vor gezielten Datenmigrationen passende zusammengehörige Daten außerhalb des Repositorys sichern. Keine privaten Home-Dateien übernehmen und keinen vorhandenen Benutzerzustand überschreiben. `docker compose down -v`, Volume-Löschung und Pruning sind keine normalen Start- oder Diagnosebefehle.

## Nachweise und Diagnose

Konfiguration, erfolgreicher Imagebuild, tatsächlicher Dienststart, sichtbare Editorfunktion, persönlicher Login und Produktprüfung sind unterschiedliche Nachweise. Benenne ausgeführte Befehle und Ergebnisse sowie konkrete offene Grenzen. Nutze Dienstlogs, tatsächliche Mounts und Netzwerkadressen zur Diagnose. Kein Bereitschaftstest darf einen Datenbankimport oder eine vollständige Audiogenerierung verstecken.
