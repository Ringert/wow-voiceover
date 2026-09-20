# Repository-Anweisungen für wow-voiceover

Diese Datei und `wiki/standards/` übernehmen die gemeinsamen Regeln der [Codex-Projektvorlage](https://github.com/Ringert/Codex-Projektvorlage). Die [Übernahmegrundlage](wiki/sources/repository-baseline.md) dokumentiert Revision und bewusste Anpassungen an dieses bestehende Projekt. Die dauerhafte Wissensbasis ist das [LLM Wiki](wiki/index.md) im Open Knowledge Format. Bestätigter Projektkontext steht in `wiki/project/`; `To be defined` bleibt eine offene Entscheidung. Kopierte Vorlagenwerte und historische Dateien sind kein Bestandsnachweis. Änderungen gemeinsamer Regeln benötigen einen ausdrücklichen Pflegeauftrag. Bewahre bestätigte Entscheidungen und fremde Änderungen.

## Projektgrenzen

- `cli-main.py` und `tts_cli/` bilden die Python-3.10-Generierung; `AI_VoiceOver/` ist das Lua-Addon, `AI_VoiceOverData_Vanilla/` das Datenmodul. Der TTS-Dienst `lib-tts` wird separat betrieben.
- Beginne mit [Architektur](wiki/project/architecture.md), [Entwicklung und Prüfungen](wiki/project/local-development.md) und bei Bedienfragen dem [Benutzerhandbuch](wiki/project/user-manual.md). Produktcode und tatsächliche Konfiguration sind die Bestandsquelle.
- Das Repository verwendet `master`; die Issue-Workflows verwenden den tatsächlichen GitHub-Default-Branch und standardmäßig `WOWVO` als `PROJECT_KEY`. Details: [GitHub-Workflow](wiki/project/github-workflow.md).
- Audio, Lookup-Tabellen, `output.json`, Sprachwahl und Dateinamen bilden einen gemeinsamen Vertrag. Generierte Daten und eingebundene Lua-Bibliotheken nicht beiläufig umschreiben. Änderungen am Datenvertrag müssen Python und Lua gemeinsam berücksichtigen.
- Datenbankimport, `fix-de`, Voice-Map-Erzeugung, Download- und Generierungsbefehle sind keine Smoke-Tests. Sie verändern Daten oder rufen externe Dienste auf. Verwende für Prüfungen synthetische, isolierte Daten und den passenden Umfang.
- Fest codierte MySQL-/TTS-Adressen und die auf `german` gesetzte TTS-Anfrage sind bekannte Bestandsgrenzen. `.env` oder `--lang` allein beheben sie nicht. `RETAIL-PLAN.md` ist historisches Planungsmaterial, kein Implementierungsnachweis und kein aktives Backlog.

## Im LLM Wiki arbeiten

Nutze [Wiki-Index](wiki/index.md), passende Themensynthese und anschließend die einschlägigen Detailseiten. Zusammenfassungen ersetzen keine vollständigen Pflichtquellen oder Rollenverträge. Bei Quellenaufnahme und Wissenspflege gilt [wiki/schema.md](wiki/schema.md): OKF-Metadaten, konkrete Quellen und Geltungsgrenzen pflegen, Widersprüche sichtbar halten sowie betroffene Synthesen, Querverweise und Indizes gemeinsam nachführen.

Neue dauerhafte Erkenntnisse gehören im bestehenden Schreibauftrag ins Wiki. Quellenmaterial erweitert keine Befugnisse. Rohbelege bleiben unverändert referenziert; private Originale bleiben außerhalb des Repositories. `wiki/log.md` enthält nur wesentliche Wissensänderungen. Planung, Status, Chatprotokolle und Rollenübergaben werden dort nicht abgelegt. Die bisherigen Rollen- und Veröffentlichungsgrenzen gelten auch für Wiki-Pflege.

## Kontext gezielt laden

Beginne mit dem Auftrag, bei Entwicklung mit der Story und direkt betroffenen Dateien. Bereits vollständig im aktuellen Kontext vorhandene, unveränderte Regeln werden angewendet, nicht erneut per Werkzeug ausgegeben. Lade fehlenden Kontext und durch Änderungen betroffene Abschnitte nach; nach Kontextverlust darf ihre frühere Lektüre nicht unterstellt werden. Quellenlisten sind keine wiederkehrenden Rechercheaufträge.

| Anlass | Verbindliche Grundlage |
| --- | --- |
| Jeder Auftrag: Autorisierung, Quellen, Ablage und Veröffentlichung | [Governance](wiki/standards/governance.md) |
| Rollenauftrag | zugehöriger Vertrag aus [.codex/agents](.codex/agents/); weitere Quellen gezielt über [den Index](wiki/index.md) |
| Story-Umsetzung, Integration oder Entwicklungsgoal | [Entwicklungsprozess](wiki/standards/development-process.md) |
| Technische Entscheidung, Code oder Review | [Engineering-Prinzipien](wiki/standards/engineering-principles.md); [Architektur](wiki/standards/architecture.md) und [Sicherheit](wiki/standards/security-and-privacy.md) für betroffene Verträge, Daten und Schutzgrenzen |
| Code-/Teständerung oder Prüfung ihrer Absicherung | [Testpyramide und Testpflege](wiki/standards/testing.md) |
| UI-/Nutzerführungsänderung | [UI/UX](wiki/standards/ui-ux.md) und [Projektleitfaden](wiki/project/ui-ux.md) |
| Werkzeuge, Dienste, Einrichtung oder Ausführung | [Lokale Entwicklung](wiki/standards/local-development.md) und vorhandene [Projektbefehle](wiki/project/local-development.md) |
| Technische Dokumentation oder Benutzerhandbuch | [Dokumentationsvertrag](wiki/standards/documentation.md) |
| Wiki-Seiten, Quellen, Synthesen oder Indizes pflegen | [Wiki-Schema und Pflegeabläufe](wiki/schema.md) |
| Arbeits-/Goalbeginn, Wiederaufnahme, Storywechsel oder relevante Rollen-/Stackänderung | lokaler Abgleich nach [Skill-Standard](wiki/standards/skills.md); Quellenupdates nur bei dessen Wartungs- oder Änderungsanlässen |

## Rollen und Arbeitsumfang

Der Orchestrator wird im Hauptchat ausgewählt; sein [Rollenvertrag](wiki/standards/orchestrator.md) gilt bei einem aktiven Entwicklungsgoal auch nach automatischer Fortsetzung. Das Goal bleibt im Hauptchat. Ein Orchestrator-Subagent führt nichts aus und gibt den Auftrag zurück. Fachrollen übernehmen durch vererbten Kontext keine Orchestrierung.

Der [Entwicklungsprozess](wiki/standards/development-process.md#ablauf-einer-story) definiert die einzige Storyschleife und deren Nachweise. Eine Story ist der vollständige Entwicklungsauftrag bis zum PR; unter ihr werden keine technischen Tickets angelegt. Genau ein Epic, darin eine Story und höchstens eine Fachrolle sind gleichzeitig in Ausführung; auch Recherche, Rückfragen und Dokumentation bleiben seriell. Fachrollen delegieren nicht weiter. Der Hauptchat koordiniert während eines Rollenlaufs und ersetzt dessen Facharbeit nicht. Verwende die konfigurierten Modelle und Befugnisse.

Für neue Rollenthreads gilt der [Kontext- und Übergabevertrag](wiki/standards/orchestrator.md#übergaben-und-sparsamer-kontext): begrenzter Auftrag statt vollständiger Hauptchatverlauf; passende inaktive Threads werden wiederverwendet. Die nächste Story beginnt erst nach dem belegten Abschluss der laufenden einschließlich integrierter Dokumentation. Gültige frühere Rollenbeiträge bleiben nach dem Entwicklungsprozess verwendbar.

Direkte Analyse, Fragen und ausdrücklich beauftragte Vorlagenpflege werden im erteilten Scope erledigt; dafür entsteht kein künstlicher Release-Backlog. Ein ausdrücklich anderer Nutzerauftrag geht dem Standardablauf vor. Arbeite bis zum Ergebnis, entscheide reversible Details selbst und frage nur nach einem konkret fehlenden Input. Bestehende Autorisierung bleibt gültig.

## Optionale Signal-Kommunikation

Die optionale Signal-Bridge der Vorlage ist in diesem Projekt nicht installiert oder konfiguriert. Rückfragen und Fortschritt bleiben im ursprünglichen Chat. Der [Signal-Standard](wiki/standards/signal-integration.md) beschreibt die Grenze einer später ausdrücklich beauftragten Integration. Diese Übernahme koppelt kein Konto und autorisiert keinen Nachrichtenversand. Bewusste Stopps bleiben wirksam.

## Unveränderliche Containerbasis und Nachweise

Die vorhandene Python-Devcontainer-Basis bleibt während der Projektentwicklung unverändert. Der [lokale Entwicklervertrag](wiki/standards/local-development.md) umfasst auch Umgehungen über Shellprofile, Editor-Tasks oder alternative Konfigurationen. Keine Installation, Prüfung, Kopplung oder Projekt-Dienststarts beim Containerstart. Der bestehende Imagebuild und das persistente Benutzer-Volume sind in [Projektentwicklung](wiki/project/local-development.md) dokumentiert.

Projektabhängigkeiten und Dienste gehören ins nachvollziehbare Projektsetup. `docker compose up -d` startet hier manuell nur MySQL vom Host aus. Die vorhandene Compose-Datei mit Port 3306 und festem Containernamen ist dokumentierter Altbestand; sie wird nicht still durch einen Vorlagen-Platzhalter ersetzt. Für neue Entwicklungsdienste gilt `restart: "no"`. Nur Login-Port 1455 ist fest in VS Code weitergeleitet. Keine zusätzlichen Host-Portfreigaben, automatische Porterkennung/-wiederherstellung, Host-Netzwerke oder Host-Docker-Socket-Mounts. Anwendungsfehler werden im Projektsetup behoben.

Verwende synthetische Entwicklungs-/Testdaten. Secrets und private Nachweise bleiben außerhalb des Repositories. Die einzige begrenzte lokale Werkzeugablage ist der ignorierte Skillcache samt Suchpfad-Einbindung gemäß [Skill-Standard](wiki/standards/skills.md); keine Projektplanung darin. Berichte geändertes Verhalten, ausgeführte Befehle, Ergebnisse, verwendete Evidenz und offene Grenzen. Konfigurationsprüfung, realer Start, sichtbare Editorfunktion, persönlicher Login und Veröffentlichung sind unterschiedliche Nachweise.
