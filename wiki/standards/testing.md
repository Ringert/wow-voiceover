---
type: Policy
title: Automatisierte Tests und Testpflege
description: Unit-, Integrations- und E2E-Tests sowie sinnvolle Testpflege während der Entwicklung.
tags:
- shared
- testing
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/testing.md
  title: 'Vorlage vor der Wiki-Migration: standards/testing.md'
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# Automatisierte Tests und Testpflege

## Verantwortung und Ziel

Der Software Developer verantwortet die Tests seiner Änderung gemeinsam mit dem Produktcode. Er kontrolliert vorhandenen Schutz, ergänzt echte Lücken und pflegt obsolete oder wenig nützliche Tests während derselben Entwicklungsaufgabe. Das Ergebnis geht einschließlich Prüfevidenz in den gemeinsamen Story-PR und dessen Code Review. Es gibt keinen zusätzlichen Testpflege-Durchlauf nach dem Review und keinen Pflichtcommit nur für weitere Tests.

Der Tech Lead benennt relevante Risiken, Integrationsgrenzen und erforderliche Nachweise. Innerhalb dieses Auftrags und des vorhandenen Setups entscheidet der Developer konkrete Testfälle und Bereinigungen selbst. Neue Infrastruktur oder geänderte verbindliche Architekturgrenzen werden wie andere technische Planänderungen geklärt. Der Reviewer bleibt beim [vereinbarten Codeabgleich](code-review.md); er übernimmt keinen zusätzlichen Testauftrag.

## Verteilung nach der Testpyramide

Die gemeinsame Richtung lautet: **viele schnelle Unit-Tests, weniger gezielte Integrationstests, sehr wenige E2E-Tests**. Teste ein Risiko auf der niedrigsten Ebene, die es wirklich erkennen kann. Eine feste Prozentquote, eine maximale Testzahl oder vollständige Klassen-/Zeilenabdeckung ist kein Qualitätsziel. Entscheidend sind Fehlerschutz, Aussagekraft, Laufzeit, Zuverlässigkeit und Wartungsaufwand. Ein integrationsreiches Feature kann mehr Integrationstests benötigen als reine Fachlogik; die Verteilung wird nicht durch nutzlose zusätzliche Tests korrigiert.

| Ebene       | Sichert ab                                                                                                                                          | Grenze                                                                                                                      |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Unit        | eigenes Verhalten von Funktionen, Klassen und Komponenten: Geschäftsregeln, Transformationen, Validierung, Zustandswechsel und relevante Grenzfälle | schnell und isoliert; kein vollständiger Anwendungsstart, keine echte Datenbank oder entfernte Dienste                      |
| Integration | Zusammenspiel eines Features und tatsächliche Verträge zwischen eigenen Modulen, API, Persistenz oder Adaptern                                      | nur benötigte Komponenten und Abhängigkeiten; die gerade geprüfte Grenze wird nicht vollständig weggemockt                  |
| E2E         | wenige häufig wiederholte zentrale Nutzerabläufe durch den dafür nötigen integrierten Produktweg                                                    | nur zusätzlicher Schutz, den Unit- und Integrationstests nicht liefern; keine vollständige Varianten- oder Fehlerfallmatrix |

Die Einordnung folgt dem tatsächlich geprüften Umfang, nicht Dateiname oder Werkzeug. Ein UI-Komponententest braucht keinen vollständigen E2E-Lauf. Fachliche Akzeptanz kann bereits mit Unit- oder Integrationstests nachgewiesen werden.

## Jederzeit reproduzierbar ausführen

Tests müssen nach Bereitstellung ihrer festgelegten Abhängigkeiten jederzeit und unmittelbar wiederholt ausführbar sein. Ihr Ergebnis darf nicht von Tageszeit, Kalenderdatum, dem Ablauf einer realen Fachfrist, einer künftig erwarteten externen Veröffentlichung oder dem Restkontingent eines vorherigen Laufs abhängen. Auf ein solches Ereignis zu warten ist kein zulässiger Weg zum grünen Test und keine Abschlussbedingung für eine Implementierung.

Steuere fachliche Zeit, Zufall, externe Antworten und Ausgangsdaten an geeigneten Grenzen. Prüfe Fristen unmittelbar vor, an und nach ihrer Grenze mit einer kontrollierten Uhr statt durch reales Abwarten. Verwenden Anwendung, Datenbank oder native Abhängigkeiten eigene Zeitquellen, muss die Teststeuerung die tatsächlich geprüften Quellen konsistent erfassen. Reale Laufzeitbegrenzungen und Prozessabbrüche bleiben wirksam; eine fachliche Testuhr darf sie nicht unbemerkt ausschalten. Synchronisiere Nebenläufigkeit über beobachtbare Zustände oder gezielte Barrieren statt über zufällig passende Schlafzeiten.

Jeder Lauf besitzt isolierte oder nachweisbar zurückgesetzte eigene Daten, Quoten, Caches und weitere veränderliche Zustände. Wiederholung und andere Ausführungsreihenfolgen dürfen keine Wartefrist erfordern. Setze nur dem Test gehörenden Zustand kontrolliert zurück; lösche keine fremden Daten und umgehe nicht die gerade geprüfte Schutzregel. Ein Quotenfall prüft die echte Begrenzung einschließlich Konkurrenz und kontrolliertem Fristwechsel; andere Tests teilen sich nicht versehentlich dessen ausgeschöpftes Kontingent.

Benötigte externe Testdaten werden als versionierte, unveränderliche Fixtures mit Herkunft, Integritätsprüfung und nachvollziehbarer Bereitstellung gesichert. Ein Testlauf benötigt keine neue Veröffentlichung und ersetzt fehlende Fixtures nicht still durch wechselnde aktuelle Daten. Bewahre echte Integrationen dort, wo Parser, Protokolle, Signaturen, Persistenz oder Prozesse das Risiko tragen. Kontrollierte Zustandswechsel an einer externen Grenze sind zulässig, müssen aber ausdrücklich als Simulation bezeichnet werden; sie belegen weder eine echte Anbieterantwort noch eine aktuelle externe Freigabe. Prüfe die reale Grenze ergänzend mit passenden stabilen Daten.

Testuhren, Ersatzantworten und besondere Fixture-Zugänge bleiben auf isolierte Testeinstiege begrenzt. Der normale Anwendungsweg verwendet die tatsächlichen Zeit- und Schutzregeln. Weise bei sicherheitsrelevanter Teststeuerung nach, dass sie dort nicht über Eingaben, Konfiguration oder mitgelieferte Testartefakte aktivierbar ist.

Zeitabhängige Live-Betriebschecks werden getrennt ausgewiesen: Sie können die momentane Erreichbarkeit, Beschaffung oder Aktualität eines externen Dienstes belegen, sind aber keine deterministischen Regressionstests. Fehlende externe Änderung wird nicht durch Warten, Skip, Umbenennung oder erfundene Evidenz als Testerfolg behandelt. Der erforderliche Fehlerschutz wird durch jederzeit ausführbare Tests hergestellt; bestehende gültige Live-Nachweise behalten ihre ausdrücklich benannte Aussagegrenze. Ein tatsächlicher Betriebsfehler wird als solcher gemeldet, nicht durch diese Trennung verdeckt.

## Unit-Tests für Verhalten

Prüfe nicht triviales eigenes Verhalten über seine nutzbare Schnittstelle. Ein Test beschreibt einen verständlichen Fall mit Ausgangszustand, Aktion und erwartetem Ergebnis. Decke die relevanten normalen Fälle, Grenzen und Fehlerfolgen ab; mehrere fachlich unterschiedliche Fälle dürfen dieselbe Klasse betreffen. Umgekehrt braucht ein interner Helfer keinen zusätzlichen isolierten Test, wenn sein Verhalten schon angemessen über die öffentliche Schnittstelle geschützt ist.

Keine Tests nur für triviale Getter/Setter, reine Datenbehälter, generierten Code, Frameworkgarantien oder bereits vom Typsystem gesicherte Aussagen. Eigene Regeln in solchen Komponenten bleiben testwürdig. Prüfe Ergebnisse und fachlich relevante Zustandsänderungen; private Methoden, interne Aufrufreihenfolgen und Klassenzuschnitte sind normalerweise keine stabilen Verträge. Interaktionen werden nur geprüft, wenn gerade die Interaktion eine Anforderung erfüllt, etwa das Verhindern einer doppelten externen Aktion.

Keine Tests, die Dokumentationswörter oder Implementierungslisten lediglich abschreiben. Prüfe bei Dokumentationsänderungen stattdessen betroffene Aussagen, Links und Formate mit vorhandenen Werkzeugen nach dem [Dokumentationsvertrag](documentation.md#nachweis-und-abschluss).

Nutze echte kleine, deterministische Objekte, soweit das die Isolation erhält. Test-Doubles ersetzen langsame oder externe Abhängigkeiten, nicht die zu prüfende Fachlogik. Kontrolliere Zeit, Zufall und externe Antworten bei Bedarf. Halte Daten und Assertions verständlich; berechne erwartete Ergebnisse nicht mit derselben Produktionslogik, deren Fehler der Test finden soll.

## Integrationstests für Features und Grenzen

Prüfe das Feature über einen passenden Einstieg mit den tatsächlich zusammenarbeitenden Komponenten. Geeignet sind beispielsweise Request → Validierung/Berechtigung → Fachlogik → Speicherung → auslesbares Ergebnis oder ein eigener Adapter mit seinem konsumierten Datenvertrag. Teste dabei Wiring, Datenabbildung, Transaktionen und relevante Fehlerübergänge, die isolierte Unit-Tests nicht belegen.

Eine Datenbankintegration verwendet eine isolierte Instanz des tatsächlich eingesetzten Datenbanksystems, wenn dessen Verhalten Teil des Risikos ist. Externe Fremdsysteme werden an ihrer definierten Grenze kontrolliert ersetzt oder über vorhandene geeignete Testumgebungen geprüft. Ein Test mit einer Ersatzimplementierung beweist keine reale Verbindung zum Anbieter. Führe keine Standardtests gegen Produktivkonten oder produktive Daten aus.

Wähle wenige aussagekräftige Fälle je betroffener Grenze und ergänze weitere nur für eigenständige Risiken. Wiederhole nicht alle Berechnungs-, Validierungs- oder Textvarianten der Unit-Ebene. Eine echte Integrationsaussage bleibt aber wertvoll, auch wenn dieselben Funktionen bereits isoliert getestet werden. „Diese Codezeilen sind abgedeckt“ genügt nicht als Grund, einen Test des Zusammenspiels zu entfernen.

## E2E bewusst klein halten

Ein E2E-Test braucht einen benannten häufig genutzten Kernablauf und eine konkrete zusätzliche Aussage über den integrierten Produktweg. Bewahre einen geeigneten vorhandenen Test und erweitere ihn nur für den geänderten Vertrag. Ein neues Feature, eine neue Klasse, Route oder Komponente erzeugt für sich keine E2E-Pflicht.

Schütze den repräsentativen Kernablauf und nur unverzichtbare Varianten. Formulardetails, einzelne Berechnungen, sämtliche Berechtigungsfälle, Texte, Viewports und Layoutpositionen werden grundsätzlich auf geeigneten niedrigeren Ebenen geprüft. Seltene Fälle werden ebenfalls dort abgesichert, wo ihr Risiko sichtbar ist. Erzwingt ein konkreter systemübergreifender Fehlerfall ausnahmsweise einen E2E-Nachweis, begründe genau diese zusätzliche Notwendigkeit; daraus entsteht keine pauschale Erweiterung der Suite.

Nutze isolierte synthetische Daten, stabile fachliche Einstiegspunkte und bei Browsern bevorzugt zugängliche Rollen beziehungsweise Namen. Warte auf beobachtbare Zustände statt mit festen Schlafzeiten. Halte Tests unabhängig von Ausführungsreihenfolge und gemeinsamem veränderlichem Zustand. Visuelle Snapshots brauchen einen ausdrücklich stabilen visuellen Vertrag; sie sind kein Standard für jedes UI-Detail.

## Vorhandene Tests pflegen

Betrachte bei einer Änderung die betroffenen Tests und ihre unmittelbar relevanten Zusammenhänge. Prüfe, welche Anforderung ein Test sichert, ob seine Assertions einen Fehler erkennen und ob ein günstigerer Test denselben Schutz bietet. Kein vollständiger Audit der gesamten Testsuite bei jeder Aufgabe.

- **Weiterverwenden**, wenn Verhalten und Schutz weiterhin passen. Zusätzlicher Testcode ist dann nicht erforderlich.
- **Ergänzen oder korrigieren**, wenn ein vereinbartes Verhalten oder konkretes Änderungsrisiko bislang nicht aussagekräftig geschützt ist.
- **Ersetzen oder vereinfachen**, wenn ein Test unnötig breit, an interne Details gekoppelt oder redundant ist. Verlagere Varianten nach unten; bewahre jede eigenständige Aussage über Integration oder Kernablauf.
- **Entfernen**, wenn die zugehörige Anforderung nachweislich entfallen ist oder der Test keinen eigenen nützlichen Schutz bietet, etwa bei bloß kopierten Quelltextmustern oder vollständig gleichwertiger anderer Abdeckung. Begründe die Entfernung kurz im Änderungsnachweis und passe verwaiste Fixtures oder Hilfen im selben Scope mit an.

Ein Test wird nicht allein wegen Fehlschlag, Aufwand, Alter oder sporadischer Instabilität entfernt. Kläre zuerst Produktfehler, ungültige Erwartung und Test-/Umgebungsfehler. Benötigter Schutz wird repariert oder aussagekräftig ersetzt, nicht durch Skip, schwächere Assertions, großzügige Timeouts oder Wiederholen bis zum grünen Lauf verdeckt. Korrigiere Fehler im verantworteten Produktcode direkt; eine geänderte fachliche Erwartung braucht eine entsprechende verbindliche Grundlage.

## Ausführen und übergeben

Führe während der Umsetzung zuerst schnelle betroffene Tests aus, danach passende Integrationstests und gegebenenfalls betroffene E2E-Prüfungen. Vor der Übergabe müssen die durch Code- und Teständerungen erforderlichen Nachweise sowie verbindliche Projektchecks vorliegen. Verbreitere den Lauf bei gemeinsam genutzten Komponenten oder neuen Fehlerhinweisen; wiederhole unveränderte geeignete Nachweise nicht routinemäßig. Eine Testentfernung oder geänderte Fixture ist ebenfalls eine Änderung mit zu prüfenden Auswirkungen.

Bei einer Fehlerkorrektur sichere den ursprünglichen Fehler nach Möglichkeit mit einem gezielten zunächst fehlschlagenden Regressionstest ab und bestätige danach den korrigierten Stand. Erfinde keinen beobachteten roten Lauf. Es besteht keine Pflicht, für jeden neuen Test Produktcode künstlich zu mutieren, ein Mutationstest-Werkzeug einzuführen oder eine eigene Verifikationsrunde zu erzeugen. Neue Tests müssen den beabsichtigten Fehler tatsächlich erkennen können; bei konkreter Unsicherheit prüfe dies gezielt.

Nutze vorhandene Compiler, Linter und Test Runner. Starte benötigte Dienste ausschließlich bei Bedarf im laufenden Dev Container über das Projektsetup, mit isolierten Testdaten. Tests, Installationen und Projektprozesse bleiben außerhalb des Containerstarts. Die [lokale Entwicklung](local-development.md) und [Projektbefehle](../project/local-development.md) bleiben maßgeblich.

Die normale Developer-Übergabe und der PR enthalten geprüften Stand, verwendete Evidenz, tatsächlich ausgeführte Befehle und Ergebnisse sowie wesentliche Ergänzungen, Ersetzungen oder Entfernungen mit kurzer Begründung. Unterscheide neue Prüfläufe von weiterverwendetem Nachweis und benenne nicht ausführbare notwendige Prüfungen konkret. Für die Mergeentscheidung gilt der [Merge-Vertrag](development-process.md#merge-nachweise): Nachweise müssen den aktuellen Stand tragen; reine Dokumentationsänderungen erlauben belegte Weiterverwendung der Codeprüfungen. Änderungen führen nur zu den dadurch erforderlichen Nachprüfungen.

Die [Recherchegrundlage](references.md#automatisierte-tests) begründet diese Regeln und ist kein erneut abzuarbeitender Quellenkatalog pro Änderung.
