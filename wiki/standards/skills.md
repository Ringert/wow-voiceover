---
type: Policy
title: Projektspezifische Skills
description: belegte Rollen-/Stackabdeckung, gezielte Installation unter `.codex`, lokaler Prüfstatus und Quellenprüfung alle
  sieben Tage oder bei Änderungen.
tags:
- shared
- skills
status: stable
scope: shared
sources:
- id: template-adoption
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/b001e1b700d75aa0f31f6ced84381ba194b79582/wiki/standards/skills.md
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/skills.md
  title: 'Vorlage vor der Wiki-Migration: standards/skills.md'
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Projektspezifische Skills

Prüfe die benötigten Fähigkeiten für die vorhandenen Rollen und den bestätigten Projektstack. Vorhandene Rollenverträge und Werkzeuge dürfen einen Bedarf nachweislich abdecken; zusätzliche Skills werden für konkrete Lücken ausgewählt, vollständig unter `.codex/skills/` installiert und in der verwendeten Codex-Laufzeit erkannt. Eine Empfehlungsliste ersetzt keine erforderliche Installation, eine Mindestzahl installierter Skills keinen Abdeckungsnachweis. Die Vorlage nimmt keinen Produktstack und keinen erfolgreichen Prüfstatus vorweg.

## Zuständigkeit und Auslöser

Der Hauptchat koordiniert Abgleich, Installation und lokalen Status. Im Goal übernimmt der Tech Lead erforderliche Auswahl- und Kompatibilitätsentscheidungen seriell; der Orchestrator setzt die begründete Auswahl um. Bei direktem Einrichtungsauftrag arbeitet der Hauptchat im erteilten Scope. Fachrollen melden konkrete Lücken und installieren nicht unabhängig voneinander. Keine künstlichen Release-Tickets, zusätzlichen Implementierungs-PRs oder parallelen Rollenaufträge.

| Anlass | Erforderliche Aktion |
| --- | --- |
| Erster Projektauftrag, Beginn einer Sitzung oder eines Goals, Wiederaufnahme einschließlich automatischer Fortsetzung, nächste Story | lokaler Abgleich von Cache, Projektbindung, relevanten Eingangsänderungen, installierten Dateien und Suchpfaden; bei gültigem Nachweis keine erneute Recherche oder Netzabfrage |
| Letzte erfolgreiche Quellenprüfung mindestens sieben Tage alt oder kein gültiger Quellennachweis | betroffene Originalquellen aktuell prüfen; unveränderte Auswahl und Downloads weiterverwenden |
| Bestätigte Änderung an Rollen, Rollenverträgen, Stack, relevanten Versionen, Skillbedarf oder Laufzeit/Suchpfaden | betroffene Abdeckung und Kompatibilität sofort neu prüfen; betroffene Skillquellen unabhängig von der Frist abgleichen |
| Konkreter Sicherheits- oder Kompatibilitätshinweis | betroffenen Nachweis sofort neu bewerten und Quelle prüfen; sicherheitsrelevante nötige Korrektur nicht bis zum Wochenabgleich verschieben |
| Einzelner Werkzeugaufruf oder Rollenübergabe ohne diese Änderungen | kein zusätzlicher Skill-Abgleich |

Zusammenfallende Anlässe im selben Hauptchat-Turn werden einmal behandelt. „Sofort“ bedeutet vor der davon abhängigen Aktion im laufenden Arbeitskontext, keinen Hintergrunddienst. Einrichtung und Prüfung erfolgen ausschließlich bei Bedarf im gestarteten Container, niemals über Containerstart, Lifecycle-Hooks, Shellprofile oder Editor-Tasks; `.devcontainer/` bleibt unverändert.

## Bedarf und Auswahl

1. Ermittle tatsächlich vorhandene Rollen aus `.codex/agents/*.toml` und ihren Verträgen, einschließlich Koordination, Produkt, UX, Technik, Entwicklung, Review und Dokumentation. Skills ändern weder Modelle noch Befugnisse oder den seriellen Prozess.
2. Ermittle den bestätigten Stack aus [Projekt-Tech-Stack](../project/tech-stack.md), Manifesten, Lockdateien und verbindlichen Auftrags-/GitHub-Entscheidungen. Unterscheide bestätigte Auswahl von installiertem Bestand. Containerbasis und kopierte Vorlagenwerkzeuge sind kein Produktstack. `To be defined`, `TBD`, leere, widersprüchliche oder teilweise geklärte Angaben bleiben offen; nicht benötigte Komponenten brauchen eine begründete Geltungsgrenze.
3. Bewerte Rollen- und Stackbedarf getrennt. Jede relevante Fähigkeit erhält `native` mit konkretem ausreichendem Rollenvertrag/Werkzeug und Evidenz, `skill` mit tatsächlicher geeigneter Skill-Zuordnung oder begründet `not_required`. Diese Einstufung betrifft Fähigkeiten, nicht pauschal ganze Technologien. Ein generischer Rollenskill belegt ohne passenden Inhalt keine Stackabdeckung. Eine erfolglose Suche oder unbekannter Stack rechtfertigt weder `native` noch `not_required`.
4. Recherchiere für tatsächliche Lücken aktuell geeignete Skills in Originalquellen. Bevorzuge gepflegte offizielle beziehungsweise kuratierte Angebote; geeignete Community-Skills bleiben möglich. Verzeichnisse und Rankings dienen nur zum Auffinden. Prüfe konkrete `SKILL.md`-Inhalte und benötigte Ressourcen auf Aufgabenpassung, Technologie/Version, Pflegezustand, Herkunft, Nutzungsrechte, Abhängigkeiten und Vereinbarkeit mit Projektregeln. Wähle die kleinste ausreichende Kombination ohne konkurrierende Duplikate; ein Skill darf mehrere belegte Bedarfe abdecken.
5. Halte Auswahlgründe, Quellen/Quellpfade, Fassungen, Abrufdatum, Abdeckung, relevante Ablehnungen und Lücken im lokalen Cache fest. Gibt es keinen geeigneten Skill für einen tatsächlich ungedeckten Bedarf, bleibt dieser offen. Keine Installation eines unpassenden Ersatzes für einen Erfolgsmarker.

Bei offenem Stack bearbeite bereits entscheidbare Rollen- und bestätigte Stackbedarfe. Nach Festlegung der fehlenden Komponenten werden deren Prüfung und nötige Installation vor abhängiger Umsetzung nachgeholt. Unverändert offene Fragen lösen keine identische Vollrecherche bei jeder Fortsetzung aus.

## Installation und Verfügbarkeit

Die Vorlage enthält einen optionalen Signal-Skill; er wird hier mangels Bridge und Kommunikationsauftrag nicht installiert. Maßgeblich ist die [Integrationsgrenze](signal-integration.md). Die vorhandenen Rollenverträge, Python-Werkzeuge, GitHub CLI und gezielte Quellcodeprüfung tragen den aktuellen Dokumentations- und Workflowauftrag. Weitere Skills werden erst für einen konkret ungedeckten Bedarf ausgewählt; es wird keine erfolgreiche spätere Modell-, Addon- oder Diensteprüfung vorweggenommen.

Installiere jeden ausgewählten zusätzlichen Skill vollständig mit benötigten Skripten, Referenzen, Assets und Lizenzhinweisen aus der geprüften Quelle. Verwende vorhandene Installer, etwa `skill-installer` mit explizitem `--dest <repository>/.codex/skills` und dokumentiertem `--ref`. Das globale Standardziel ist nicht das Projektziel. Downloadlink, leeres Verzeichnis oder alleinige `SKILL.md` trotz benötigter Ressourcen genügen nicht. Identisch vorhandene Skills werden wiederverwendet.

Prüfe heruntergeladene Anweisungen und Skripte vor Verwendung. Keine Erweiterung von Rollenbefugnissen, kein Überschreiben bestätigter Entscheidungen und keine Umgehung der Containergrenzen. Zusätzliche Laufzeiten, Dienste oder Konten benötigen tatsächlichen Bedarf und bestehende Autorisierung. Download autorisiert keine externe Kommunikation oder Veröffentlichung.

Maßgebliche Projekt-Skills liegen versioniert unter `.codex/skills/`. Globale oder mit Codex gebündelte Hilfsskills müssen nicht vorsorglich kopiert werden. Ihre belegte Verfügbarkeit und Eignung kann vorhandene Werkzeugabdeckung tragen, ist aber kein Nachweis einer ausdrücklich benötigten projektlokalen Installation.

Prüfe den Suchpfad der verwendeten Codex-Version. Die [offizielle Dokumentation](https://learn.chatgpt.com/docs/build-skills#where-to-save-skills) beschreibt `.agents/skills` und verlinkte Skill-Verzeichnisse. Falls `.codex/skills` nicht direkt erkannt wird, lege bei Bedarf lokal `.agents/skills/<skill-name>` als relativen Link auf `../../.codex/skills/<skill-name>` an. Die Dateien bleiben in `.codex/skills`; die Einbindung wird nicht versioniert. Überschreibe keine fremden gleichnamigen Skills oder Suchpfade und vermeide doppelte Einträge.

Verifiziere nach Installation, relevanter Änderung oder Laufzeit-/Suchpfadwechsel vollständige Dateien, gültige Metadaten mit `name` und `description`, benötigte Ressourcen und tatsächliche Erkennung durch Codex beziehungsweise dessen Skill-Liste. Konfiguration oder Symlink allein genügt nicht. Lade Codex bei Bedarf neu; bis zur Erkennung bleibt dieser Nachweis offen. Speichere geprüfte Revision und reproduzierbaren Fingerprint des gesamten Skill-Verzeichnisses. Unveränderte Dateien bei derselben Laufzeit und Einbindung erlauben die Weiterverwendung dieses Nachweises.

## Lokaler Prüfstatus

Nutze genau `.codex/skills-check.json`, von Git ignoriert und nicht als erfolgreicher Vorlagenstand kopiert. Er enthält nur Werkzeugauswahl und Prüfstatus, keine Planung, Rollenübergaben, Zugangsdaten oder privaten Nachweise. Zeitpunkte stehen in UTC mit Zeitzone.

| Feld | Inhalt |
| --- | --- |
| `schemaVersion` | `2`; alte oder unbekannte Formate werden anhand realer Quellen neu bewertet, ihre früheren Erfolgswerte nicht übernommen |
| `status` | `not_checked`, `pending_stack`, `incomplete` oder `complete` gemäß unten |
| `project` | geprüfte Repository-Identität ohne Zugangsdaten und aufgelöster Checkout-Pfad |
| `inputs` | Quellen/Fingerprints der Rollen samt Verträgen, bestätigten Stackentscheidungen, relevanten Versionsdateien, dieses Standards sowie Laufzeit und Einbindung |
| `roles`, `stack` | getrennte Abdeckung je Fähigkeit mit `native`, `skill` oder `not_required`, Begründung/Evidenz und offenen Anforderungen; Stackzustand `unknown`, `partial` oder `defined` mit Komponenten, Versionen und Quellen |
| `research` | Kandidaten, Originalquellen, Fassungen/Abrufdaten, Auswahlgründe, relevante Ablehnungen und verbleibende Recherche |
| `skills` | je ausgewähltem Skill Quelle/Quellpfad, beobachteter Branch oder Releasekanal, genaue installierte Revision, Inhaltsfingerprint, Installations-/Suchpfad und tatsächlicher Erkennungsnachweis |
| `updates` | Status `not_checked`, `current`, `available` oder `failed`; je Quelle letzte geprüfte Revision, `lastAttemptAt`, `lastSuccessAt`, `validUntil`, gegebenenfalls ETag, Fehler und `nextRetryAt` |
| `checkedAt`, `lastCompleteAt`, `pending` | letzter lokaler Abgleich, letzter belegter Gesamterfolg und konkrete Lücken samt nächstem nötigem Schritt |

`not_checked` gilt ohne verwertbaren lokalen Abgleich, auch bei fremdem oder beschädigtem Cache. `pending_stack` gilt bei unbekanntem oder teilweise geklärtem Stack; nutzbare Einzelnachweise bleiben erhalten. `incomplete` gilt bei definiertem Stack mit noch fehlender Abdeckung, erforderlicher Installation, Erkennung, Kompatibilität oder fälliger Quellenprüfung.

`complete` bedeutet **Bedarf vollständig abgedeckt**, nicht „für jede Rolle einen externen Skill installiert“. Es setzt gleichzeitig passende aktuelle Eingangsgrundlagen, separat belegte Rollen- und Stackabdeckung, `stack.state: defined`, keine entscheidungsrelevante Lücke, vollständig installierte und erkannte ausgewählte Skills sowie gültige Quellenprüfungen ohne offene erforderliche Aktualisierung voraus. Weder eine leere ungeklärte Stackliste noch alleinige Rollenabdeckung genügt. Ein tatsächlich nicht benötigter Technologiebereich muss ausdrücklich begründet sein.

## Gültigkeit und Updates

Beim lokalen Abgleich vergleiche Projektbindung, Eingangs- und Skillfingerprints sowie Einbindung. Entwerte nur betroffene Nachweise bei Änderungen, fehlenden Dateien oder abgelaufener Quellenfrist; ein unveränderter lokaler Abgleich setzt einen gültigen Erfolg nicht vorsorglich zurück. Ein Cache aus anderem Checkout oder inkompatiblem Format wird anhand realer Quellen neu aufgebaut. Keine Erfolgsannahme nach Abbruch oder Kontextverlust.

Eine erfolgreiche Originalquellenprüfung gilt höchstens sieben Tage ab `lastSuccessAt` (`validUntil`); relevante Änderungen oder konkrete Sicherheits-/Kompatibilitätshinweise beenden ihre Gültigkeit früher. Ein lokaler Abgleich aktualisiert `checkedAt`, verlängert aber niemals diese Quellenfrist. Bei fälliger Prüfung vergleiche den aktuellen Stand des gespeicherten Branches/Releasekanals mit der installierten Revision. Der erneute Abruf nur eines unveränderlichen alten Commits genügt nicht. Verwende sparsame Release-, Commit- oder ETag-Abfragen; ohne Änderung kein Komplettdownload. Bei vorlageneigenen versionierten Skills ist der tatsächliche Stand dieses Repositorys die Quelle; lokale Änderungen müssen im Fingerprint und geprüften Stand erkennbar bleiben.

Prüfe verfügbare Updates zunächst temporär außerhalb des Checkouts auf Eignung, Kompatibilität und neue Abhängigkeiten. Installiere passende Updates im autorisierten Umfang und verifiziere Dateien und Erkennung erneut. Bewahre lokale Anpassungen und den bisherigen nutzbaren Stand bei Fehlern; kein blindes Löschen oder Überschreiben. Normale Updates werden an einer vorgesehenen Arbeitsgrenze integriert; eine begonnene Story wechselt ihre Regeln nicht beiläufig. Erforderliche Sicherheits-/Kompatibilitätskorrekturen werden vor betroffener Weiterarbeit behandelt.

Bei Netzfehlern oder Konflikten bleiben nutzbare Fassungen erhalten, der betroffene Aktualitätsnachweis offen und `lastSuccessAt` unverändert. Halte nur den tatsächlichen Versuch mit Fehler fest. Ein unveränderter vorübergehender Abfragefehler wird frühestens nach 24 Stunden erneut versucht (`nextRetryAt`); eine konkret geänderte Voraussetzung oder ein Sicherheits-/Kompatibilitätsanlass erlaubt die frühere gezielte Prüfung. Kein Netzversuch bei jeder automatischen Fortsetzung. Abgelaufene oder fehlgeschlagene Nachweise werden währenddessen nicht als aktuell ausgegeben.

Schreibe Einzelnachweise und abgeleiteten Status gemeinsam über eine temporäre Datei und anschließendes Ersetzen. Nur der koordinierende Hauptchat schreibt; überlappende Sitzungen stimmen die Zuständigkeit ab und lesen keinen laufenden Schreibvorgang als Erfolg. Frühere gültige Evidenz bleibt erhalten, historische Erfolge sind als solche kenntlich.

Melde Auswahländerungen, tatsächliche Installationen/Updates, Fassungen, Status und konkrete Grenzen knapp im Originalchat; ein unveränderter erfolgreicher lokaler Abgleich benötigt keinen ausführlichen Wiederholungsbericht. Unvollständiger Skillstatus blockiert nur davon konkret abhängige Arbeit. Er ersetzt weder Produktprüfungen noch Merge- oder Goal-Nachweise.

## Quellen und Geltungsgrenze

Die [offizielle Codex-Dokumentation](https://learn.chatgpt.com/docs/build-skills) beschreibt Format, Erkennung, Suchpfade und Installer; geprüft am 12. September 2026. Bei relevanter Laufzeitänderung wird die passende aktuelle Dokumentation herangezogen. Abdeckungsmodell, `.codex`-Ablage, Cacheformat, Siebentagefrist und Auslöser sind Projektregeln dieser Vorlage, keine eingebauten Codex-Funktionen.
