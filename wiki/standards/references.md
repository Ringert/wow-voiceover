---
type: Reference
title: Fachliche Referenzen
description: Primärquellen und Aktualisierungsregeln.
tags:
- shared
- references
status: stable
scope: shared
sources:
- id: original
  resource: https://github.com/Ringert/Codex-Projektvorlage/blob/c183c5095191ea9cb2baa38af8a4c5fddd05ecec/documentation/standards/references.md
  title: 'Vorlage vor der Wiki-Migration: standards/references.md'
generated:
  by: codex/gpt-6
  at: '2026-09-14T21:56:25Z'
---
# Fachliche Referenzen

## Quellenregel

Technische Entscheidungen verwenden die zum Entscheidungszeitpunkt aktuelle offizielle Dokumentation der tatsächlich betrachteten Technologie. Frühere Versionslisten oder Blogbeiträge gelten nicht als Auswahlbegründung. Der Tech Lead dokumentiert im Architekturartefakt Quelle, Abrufdatum und entscheidungsrelevante Support-, Sicherheits-, Lizenz- oder Hostingaussage.

Framework- und Versionsquellen werden nur für tatsächlich eingesetzte Technologien aufgenommen; eine Referenzliste allein begründet keine Präferenz.

## Übergreifende Primärquellen

### Gemeinsame Entwicklungsumgebung

- [Dev Containers: Metadatenreferenz](https://containers.dev/implementors/json_reference/)
- [Offizielles Docker-in-Docker-Feature](https://github.com/devcontainers/features/tree/main/src/docker-in-docker)
- [Docker Compose: Services](https://docs.docker.com/reference/compose-file/services/)
- [Docker: Volumes](https://docs.docker.com/engine/storage/volumes/)
- [VS Code: Entwicklung im Container](https://code.visualstudio.com/docs/devcontainers/containers)
- [Codex: benutzerdefinierte Rollen](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Codex: Konfigurationsreferenz](https://learn.chatgpt.com/docs/config-file/config-reference)

Diese Quellen beschreiben die tatsächlich verwendete gemeinsame Basis. Projektspezifische Technologie- und Fachquellen gehören nach [Projektreferenzen](../project/references.md).

### Orchestrator und Codex Goals

Abgleich vom 7. September 2026 für den [Orchestrator-Rollenvertrag](orchestrator.md) und den auswählbaren [Agenten](../../.codex/agents/orchestrator.toml):

- [OpenAI: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents): eigene Agents werden als einzelne TOML-Dateien unter `.codex/agents/` mit `name`, `description` und `developer_instructions` definiert. Eine rollenspezifische Hauptchat-/Subagent-Aufrufsperre ist dort nicht dokumentiert. Das Limit `max_concurrent_threads_per_session` zählt offene Subagententhreads und schließt den Hauptchat aus; mehrere inaktive Rollenthreads erlauben die spätere Wiederverwendung ihres Kontexts.
- [OpenAI: Developer commands](https://learn.chatgpt.com/docs/developer-commands): verfügbare Chatbefehle; ein Threadwechsel ist keine Auswahl einer eigenen TOML-Rolle als neuer Hauptagent.
- [OpenAI: Using goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex): Goals sind an den jeweiligen Chat gebunden und setzen Arbeit bis zum belegten Abschluss oder einer Laufzeitgrenze fort.
- [OpenAI: Config reference](https://learn.chatgpt.com/docs/config-file/config-reference): Projektkonfiguration wird für vertrauenswürdige Projekte geladen; Goal- und Subagenten-Einstellungen sowie Rollenparameter haben unterschiedliche Zwecke.

Die Vorlage verwendet für den Orchestrator dasselbe Agent-Dateiformat wie für die vorhandenen Fachrollen. Seine Beschränkung auf den Hauptchat ist als Rollenregel in den Anweisungen verankert, nicht als belegte technische TOML-Sperre. Genau eine aktive Story und Fachrolle, vollständige Storyrunden sowie die Dokumentationspflege im gemeinsamen Story-PR sind verbindliche Nutzerentscheidungen dieser Vorlage. Die Quellen begründen keine Parallelisierung, zusätzlichen Prozessphasen, Startup-Prüfungen oder Pflichtrecherche pro Story. Die sichtbare IDE-Auswahl muss von einer reinen Datei- oder Konfigurationsprüfung unterschieden werden.

### Web und Accessibility

- [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WHATWG HTML Living Standard](https://html.spec.whatwg.org/)
- [web.dev: Core Web Vitals](https://web.dev/articles/vitals)

### Anwendungssicherheit

- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

### GitHub-Arbeitsorganisation

- [GitHub Docs: About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues)
- [GitHub Docs: Adding sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues)
- [GitHub Docs: Issue dependencies](https://docs.github.com/en/rest/issues/issue-dependencies)
- [GitHub Docs: About milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones)

### Automatisierte Tests

Recherche vom 6. September 2026 für [Testpyramide und Testpflege](testing.md):

- [Martin Fowler: Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html): breite Basis schneller Tests und wenige Tests durch den vollständigen Produktweg; UI-Verhalten kann auch unterhalb von E2E geprüft werden. Entscheidend sind die Kosten und der zusätzliche Schutz, nicht allein die Bezeichnung der Ebene.
- [Ham Vocke: The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html): eigene Logik und tatsächliche Integrationsgrenzen passend prüfen; höhere Tests behalten nur dann ihren Wert, wenn sie eine zusätzliche Aussage liefern. Redundante oder nutzlos gewordene Tests dürfen ersetzt oder entfernt werden.
- [Software Engineering at Google, Kapitel 12: Unit Testing](https://abseil.io/resources/swe-book/html/ch12.html): Verhalten über öffentliche Schnittstellen prüfen, verständliche Fälle und Assertions schreiben und unnötige Bindung an interne Aufrufdetails vermeiden.
- [Google Testing Blog: Fixing a Test Hourglass](https://testing.googleblog.com/2020/11/fixing-test-hourglass.html): Erfahrungsbericht zur Stärkung von Integrationstests zwischen Unit und E2E; geeignete Integrationstests erlaubten das Entfernen redundant gewordener E2E-Tests.

Die Vorlage übernimmt diese Prinzipien als risikobezogene Entscheidungshilfe. Eine feste Prozentverteilung, pauschale Coverage-Vorgabe, ein Test pro Klasse oder E2E für jedes Feature wird daraus nicht abgeleitet. Der Schwerpunkt auf häufig wiederholten Kernabläufen und die direkte Testpflege durch den Developer sind bewusste Regeln dieses Entwicklungsprozesses. Es entsteht weder eine automatische Prüfung beim Containerstart noch eine Pflicht zu zusätzlicher Infrastruktur oder Recherche pro Änderung.

### Product Owner

Recherche vom 6. September 2026 für den [Product-Owner-Rollenvertrag](product-owner.md):

- [Schwaber und Sutherland: Scrum Guide 2020, Product Owner und Product Backlog](https://scrumguides.org/scrum-guide.html): Verantwortung für Produktwert, verständliche Ziele und geordneten Backlog; fortlaufendes Refinement und technische Größenbewertung durch die Ausführenden.
- [GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs): bestehende Abläufe und unterschiedliche Nutzer verstehen, Annahmen von belegtem Bedarf trennen und Erkenntnisse mit konkreten Stories verbinden.
- [Bill Wake: INVEST in Good Stories, and SMART Tasks](https://xp123.com/invest-in-good-stories-and-smart-tasks/): wertvolle, kleine, verhandelbare und prüfbare Stories; fachliche Schnitte durch die benötigten technischen Schichten. Unabhängigkeit ist ein Ziel, keine ausnahmslose Voraussetzung.
- [Mountain Goat Software: Five Story-Splitting Mistakes and How to Stop Making Them](https://www.mountaingoatsoftware.com/agile/five-story-splitting-mistakes-and-how-to-stop-making-them): Zuschnitt mit nötigem Teamwissen verbessern, nach fachlichen Wegen statt technischen Schichten teilen und die technische Lösung offenlassen.
- [GOV.UK Service Manual: Writing user stories](https://www.gov.uk/service-manual/agile-delivery/writing-user-stories): Nutzer, Bedarf und Ziel klar ausdrücken; Akzeptanz als beobachtbare Ergebnisse formulieren und Details zum passenden Zeitpunkt ergänzen.
- [GOV.UK Service Manual: Deciding on priorities](https://www.gov.uk/service-manual/agile-delivery/deciding-on-priorities): begrenzte Kapazität anhand nachvollziehbarer Evidenz priorisieren, Entscheidungen aktualisieren und neben neuen Features auch bestehende Nutzerprobleme berücksichtigen.

Die Vorlage übernimmt diese fachlichen Praktiken ohne zusätzliche Scrum-Termine, Sprintpflicht, starres Punktesystem oder formales Freigabegremium. Ein Epic pro zusammengehörigem Feature, die native GitHub-Hierarchie und die serielle Zusammenarbeit über den Orchestrator sind bewusste Regeln dieser Vorlage, keine Behauptung über vorgeschriebene Scrum-Artefakte. Projektziele, Nutzerbelege und konkrete Prioritäten werden im jeweiligen Projekt geklärt; sie werden aus keiner Methode erfunden. Die Quellen müssen nicht bei jedem Refinement erneut geladen werden.

### UX Designer

Recherche vom 6. September 2026 für den [UX-Rollenvertrag](ux-designer.md) und die [UI/UX-Regeln](ui-ux.md):

- [Nielsen Norman Group: Design Systems 101](https://www.nngroup.com/articles/design-systems-101/): gemeinsame Gestaltungsregeln, wiederverwendbare Komponenten und Muster schaffen eine verständliche Designsprache. Verwendungsregeln und fortlaufende Pflege gehören dazu; der Umfang muss zum tatsächlichen Bedarf passen.
- [Nielsen Norman Group: Maintain Consistency and Adhere to Standards](https://www.nngroup.com/articles/consistency-and-standards/): innerhalb des Produkts konsistent arbeiten und zugleich bekannte Plattform- und Domänenkonventionen beachten. Gleiche Bedeutung und Bedienung verlangen nicht in jedem Kontext dieselbe Layoutschablone.
- [GOV.UK Design System: Contribution criteria](https://design-system.service.gov.uk/community/contribution-criteria/): neue Komponenten und Muster brauchen belegten Nutzen und sollen vorhandene Lösungen nicht duplizieren; vorhandene Stile und Komponenten werden wiederverwendet und reale Einsatzkontexte berücksichtigt.
- [GOV.UK Service Manual: Making prototypes](https://www.gov.uk/service-manual/design/making-prototypes): Prototypen klären und vermitteln Entwürfe vor der Produktimplementierung. Detailtiefe und Interaktivität richten sich nach der offenen Frage; Prototypcode ist kein ungeprüft übernehmbarer Produktcode.
- [GOV.UK Service Manual: Writing user stories](https://www.gov.uk/service-manual/agile-delivery/writing-user-stories): Nutzerziel und beobachtbare Ergebnisse verbinden die gemeinsame Ausarbeitung im Team; passende Evidenz und Entwürfe werden an der Story referenziert.
- [W3C: Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/): überprüfbare Anforderungen unter anderem zu Kontrast, Bedienung, Orientierung, Eingaben und Konsistenz. WCAG 2.2 AA ist das interne Web-Qualitätsziel dieser Vorlage, keine durch einen Entwurf bereits belegte Konformität.
- [WAI: Focus Not Obscured (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) und [Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): erläutern fokussierte Elemente bei überlagernden Flächen sowie Größe, Abstand und Ausnahmen von Zeigerzielen. Die Erläuterungen ergänzen die normativen Kriterien.

Die Vorlage übernimmt diese Praktiken für einen gemeinsamen Projektleitfaden, angemessene Mockups und die serielle UX-Ticketvorbereitung. Gestalterische Hoheit, Ticketanhänge beziehungsweise externe Referenzen für Entwürfe und die Pflege des implementierten Leitfadens durch den Documentation Writer im Story-PR sind bewusste Prozessentscheidungen. Es entstehen weder eine fremde Markenpalette, ein festes Designwerkzeug, ein zusätzliches Freigabegremium noch eine Pflicht zu neuen Mockups oder Nutzerstudien für jede kleine UI-Änderung. Die Quellen ersetzen keine projektspezifische Gestaltung und werden nicht bei jedem Refinement erneut abgearbeitet.

### Tech Lead

Recherche vom 6. September 2026 für den [Tech-Lead-Rollenvertrag](tech-lead.md):

- [Pat Kua: The Definition of a Tech Lead](https://www.patkua.com/blog/the-definition-of-a-tech-lead/): technische Richtung und Qualität verantworten, Architektur mit Entwicklungserfahrung verbinden und für belastbare Entscheidungen nah am Code bleiben; Zusammenarbeit mit der fachlichen Produktverantwortung.
- [Industrial Empathy: Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/): Erfahrungsbericht über kurze Entwürfe mit Kontext, Zielen, Lösung und relevanten Abwägungen vor der Implementierung. Umfang und Detailtiefe folgen dem Problem; vollständige Code- und Schemakopien helfen normalerweise nicht.
- [Michael Nygard: Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions): bedeutsame Entscheidungen mit Kontext, gewähltem Weg, Status und Konsequenzen verständlich festhalten; auch Nachteile erklären und ersetzte Entscheidungen nachvollziehbar lassen.
- [arc42: Building Block View](https://docs.arc42.org/section-5/): Verantwortungen, Schnittstellen und Abhängigkeiten mit dem tatsächlichen Code verbinden. Tiefer beschrieben werden relevante, riskante oder überraschende Komponenten; normale Implementierungsdetails benötigen keine vollständige Zerlegung.
- [arc42: Quality Requirements](https://docs.arc42.org/section-10/): relevante Qualitätsziele konkret und überprüfbar ausdrücken, bei Bedarf als Szenario mit Bedingungen, Auslöser und erwartetem Ergebnis; bereits klare Anforderungen brauchen keine zusätzliche Darstellung.

Die [Testquellen](#automatisierte-tests) und [Refactoring-Grundlage](#software-developer) ergänzen die Umsetzungshilfen. Die Vorlage übernimmt diese Praktiken für technische GitHub-Ticketergänzungen und gezielte Beratung. Technische Hoheit innerhalb bestätigter Vorgaben, serielle Rollenarbeit und lokaler Developer-Spielraum sind bewusste Prozessentscheidungen. Es entstehen weder ein zusätzliches Architektur-Freigabegremium noch Personalführungsaufgaben, eine feste Programmierzeitquote oder eine vollständige arc42-/Design-Doc-Pflicht. Geplante Entscheidungen bleiben in GitHub; Nygards konkrete ADR-Dateiablage wird nicht als zusätzlicher Planungsordner übernommen. Die Quellen werden nicht pro Story erneut abgearbeitet.

### Software Developer

Recherche vom 6. September 2026 für den [Software-Developer-Rollenvertrag](software-developer.md):

- [GitHub Docs: Helping others review your changes](https://docs.github.com/en/pull-requests/concepts/helping-others-review-your-changes): fokussierte PRs mit verständlichem Kontext und Issue-Bezug vorbereiten; den eigenen Diff auf versehentliche Änderungen prüfen und relevante Builds beziehungsweise Tests vor dem unabhängigen Review ausführen.
- [Google Engineering Practices: Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html): zusammenhängende, überschaubare Änderungen erleichtern das Verständnis; zugehörige Tests gehören zur Änderung. Umfang wird nach inhaltlichem Zusammenhang beurteilt, nicht allein nach Zeilenzahl.
- [Google Engineering Practices: Writing good CL descriptions](https://google.github.io/eng-practices/review/developer/cl-descriptions.html): Problem, Wirkung und nötige Hintergründe für spätere Leser erklären; Beschreibung nach Änderungen im Review an den endgültigen Inhalt anpassen.
- [Martin Fowler: Refactoring](https://refactoring.com/): verhaltenserhaltende Strukturverbesserung in kleinen Schritten als Teil der normalen Programmierung; Tests helfen, Fehler beim Umbau zu erkennen.
- [Google Engineering Practices: How to handle reviewer comments](https://google.github.io/eng-practices/review/developer/handling-comments.html): Feedback verstehen, sachlich anhand technischer Gründe klären und bei Verständnisproblemen den Code verbessern, statt Wissen nur in der Review-Diskussion festzuhalten.
- [GitHub Docs: Resolving reviews](https://docs.github.com/en/pull-requests/concepts/resolving-reviews): Findings verstehen, Korrekturen lokal prüfen und auf denselben PR-Branch pushen; Konflikte beheben und ein erneutes Review anfordern. Außerhalb des Auftrags liegende Wünsche werden nicht beiläufig in den PR aufgenommen.

Die [Testquellen](#automatisierte-tests) ergänzen diese Praktiken. Genau ein PR pro Story, die integrierte Testpflege, der lokale Entscheidungsspielraum und die serielle Review-Übergabe sind bewusste Regeln dieser Vorlage. Googles zusätzliche Möglichkeiten wie gestapelte PRs, parallele Arbeit und separate Test-/Refactoring-PRs werden nicht als Pflicht übernommen. Es entstehen weder feste Zeilengrenzen, zusätzliche Rollen oder Freigabeschritte noch eine Pflicht zur erneuten Recherche bei jeder Umsetzung.

### Code Review

Recherche vom 6. September 2026 für den [Code-Review-Rollenvertrag](code-review.md):

- [Google Engineering Practices: The Standard of Code Review](https://google.github.io/eng-practices/review/reviewer/standard.html): Fakten und technische Gründe tragen Entscheidungen; gleichwertige Lösungen und persönliche Präferenzen rechtfertigen keine Verzögerung auf der Suche nach Perfektion.
- [Google Engineering Practices: What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html): Funktion, relevante Zusammenhänge und Aussagekraft von Tests verstehen; eigener geänderter Code und fremde beziehungsweise generierte Implementierung verlangen unterschiedliche Prüftiefe.
- [Google Engineering Practices: Navigating a CL in review](https://google.github.io/eng-practices/review/reviewer/navigate.html): mit Änderungszweck und zentralem Ablauf beginnen, danach die übrigen betroffenen Dateien nachvollziehbar prüfen.
- [Google Engineering Practices: How to write code review comments](https://google.github.io/eng-practices/review/reviewer/comments.html): sachlich am Code argumentieren, den Grund erklären und die Verantwortung für die konkrete Lösung beim Developer lassen.
- [Microsoft Research: Characteristics of Useful Code Reviews: An Empirical Study at Microsoft](https://www.microsoft.com/en-us/research/publication/characteristics-of-useful-code-reviews-an-empirical-study-at-microsoft/): empirische Untersuchung von 2015 zur Nützlichkeit von Review-Kommentaren. Die beobachtete Verbindung zwischen mehr geänderten Dateien und geringerem Anteil nützlicher Kommentare unterstützt überschaubare Reviews; sie begründet weder eine starre Dateigrenze noch das Auslassen relevanten Codes.

Die Google-Leitlinien verfolgen eine breitere langfristige Codequalität und lassen auch optionale Lern- und Stilhinweise zu. Diese Vorlage übernimmt die belegorientierte, respektvolle Arbeitsweise, begrenzt den Auftrag aber ausdrücklich auf vereinbarte Anforderungen und vom PR verursachte Vertragsbrüche. Der Verzicht auf Zusatzlisten, erneute Vollprüfungen ohne Anlass und unnötige Werkzeugaufrufe ist die konkrete Rollenentscheidung dieser Vorlage, keine behauptete allgemeine Pflicht aus den Quellen. Die Recherche wird nicht bei jedem Review wiederholt.

### Technische Dokumentation und Benutzerhandbuch

Recherche vom 6. September 2026 für den [Dokumentationsstandard](documentation.md), den [Tech Lead](tech-lead.md#technische-verantwortung-für-die-dokumentation) und den [Product Owner](product-owner.md#fachliche-verantwortung-für-das-benutzerhandbuch):

- [arc42: Architektur und Code synchron halten](https://faq.arc42.org/questions/H-3/): klare Verantwortung, sparsame Detailtiefe, stabile Übersichten und wichtige Querschnittskonzepte erleichtern dauerhafte Pflege.
- [arc42: Crosscutting Concepts](https://docs.arc42.org/section-8/): benötigte gemeinsame Prinzipien und ihr tatsächliches Funktionieren zentral erklären; passende Quellstellen verwenden und nur relevante Konzepte aufnehmen.
- [C4 Model: Diagrams](https://c4model.com/diagrams): Abstraktion und Detailtiefe nach Zielgruppe wählen; Kontext und wesentliche ausführbare Bausteine genügen oft, weitere Ebenen brauchen zusätzlichen Nutzen.
- [C4 Model: Notation](https://c4model.com/diagrams/notation): Diagramme sollen mit Titel, erkennbaren Elementen, beschrifteten Beziehungen und nötiger Legende verständlich sein; ein bestimmtes Zeichenwerkzeug ist nicht vorgeschrieben.
- [Diátaxis](https://diataxis.fr/): Einstieg zum Lernen, zielgerichtete Anleitungen, Nachschlageinformationen und Erklärungen bedienen unterschiedliche Leserbedürfnisse und werden passend gegliedert.
- [Diátaxis: How-to guides](https://diataxis.fr/how-to-guides/): Anleitungen folgen einer konkreten Nutzeraufgabe, ihrem logischen Ablauf und relevanten Varianten; erklärende oder vollständige Referenzdetails werden gezielt verlinkt.
- [Google Developer Documentation Style Guide: Procedures](https://developers.google.com/style/procedures): kurze handlungsorientierte Schritte, konsistente Benennung, sinnvolle Reihenfolge, erkennbare Ergebnisse und zugängliche Bedienhinweise; unnötige Wiederholung vermeiden.

Die inhaltliche Zuständigkeit von Tech Lead und Product Owner sowie die Ausführung beider Dokumentationsbereiche durch den Documentation Writer im gemeinsamen Story-PR sind Regeln dieser Vorlage, keine universellen Rollenvorschriften. Der Standard verbindet gezielte Pflege mit jeder betroffenen Story, Prüfung zum Epic-Abschluss und Korrekturen aus konkreten Rückmeldungen. Er verlangt weder eine vollständige arc42-/C4-/Diátaxis-Struktur für jedes Feature noch zusätzliche Produktreviews, automatische Hintergrundprüfungen oder neue Dokumentationswerkzeuge. Geplantes Verhalten und Mockups bleiben im Ticket; dokumentiert wird der tatsächliche Bestand.

### Signal-Bridge

Primärquellen für die [implementierte Signal-Anbindung](signal-integration.md), geprüft am 7. September 2026. Die versionsgebundenen Adapter werden bei einem Laufzeitwechsel gezielt neu geprüft; diese Liste behauptet keine persönliche Konto- oder Handyabnahme.

- [OpenAI: App Server](https://learn.chatgpt.com/docs/app-server): Thread-/Goal-Bezug und JSON-RPC-Transporte. Ein zusätzlicher Server übernimmt keine vorhandene private IDE-Sitzung automatisch.
- [OpenAI: MCP](https://developers.openai.com/codex/mcp/) und [Konfigurationsreferenz](https://learn.chatgpt.com/docs/config-file/config-reference): projektbezogene stdio-Integration in vertrauenswürdigen Repositories, optionaler Server mit `required = false`, Start-/Werkzeugtimeouts und Freigaben je Werkzeug. Allgemeine Sandbox- und Freigaberegeln bleiben erhalten.
- [Dev Containers: Metadatenreferenz](https://containers.dev/implementors/json_reference/): Imagebuild und Lifecycle-Befehle sind getrennte Mechanismen. Die gemeinsame Signal-Laufzeit wird im Image gebaut; der Containerstart löst keine Signal-Einrichtung oder Prüfung aus.
- [Codex 0.153.0: MCP-Metadaten](https://github.com/openai/codex/blob/rust-v0.153.0/codex-rs/core/src/mcp_tool_call.rs): Codex setzt die Thread-ID je Werkzeugaufruf, statt sie dem Modell als frei wählbares Zustellargument zu überlassen.
- [Codex 0.153.0: Queue-Service](https://github.com/openai/codex/blob/rust-v0.153.0/codex-rs/ext/queue/src/service.rs) und [Queue-Request-Processor](https://github.com/openai/codex/blob/rust-v0.153.0/codex-rs/app-server/src/request_processors/thread_queue_processor.rs): persistente Eingaben, Erkennung externer Queue-Änderungen und Fortsetzung geladener Originalthreads bei erhaltenem Kontext; bewusste Unterbrechungen werden respektiert.
- [Codex 0.153.0: Rollout-Persistenz](https://github.com/openai/codex/blob/rust-v0.153.0/codex-rs/rollout/src/policy.rs) und [Protokoll](https://github.com/openai/codex/blob/rust-v0.153.0/codex-rs/protocol/src/protocol.rs): persistierte terminale Turnereignisse einschließlich Fehlerklasse erlauben externe Überwachung ohne Stilleheuristik.
- [signal-cli 0.14.7: README](https://github.com/AsamK/signal-cli/blob/v0.14.7/README.md) und [Handbuch](https://github.com/AsamK/signal-cli/blob/v0.14.7/man/signal-cli.1.adoc): JRE-25-Anforderung, Kontokopplung, Gruppen und JSON-RPC-Betrieb der inoffiziellen Signal-Integration.
- [signal-cli 0.14.7: SendCommand](https://github.com/AsamK/signal-cli/blob/v0.14.7/src/main/java/org/asamk/signal/commands/SendCommand.java) und [JsonRpcNamespace](https://github.com/AsamK/signal-cli/blob/v0.14.7/src/main/java/org/asamk/signal/commands/JsonRpcNamespace.java): `notifySelf: true` wird auf `--notify-self` abgebildet, damit eigene Empfänger/Gruppen normale Nachrichten statt ausschließlich Sync-Nachrichten erhalten.

## Veröffentlichung und Recht

Rechtliche Quellen werden erst für den konkreten tatsächlichen Betrieb und seine Rechtsordnung bewertet. Ausgangspunkte sind amtliche Gesetzesfassungen und zuständige Behörden; für einen entsprechenden EU-/Deutschland-Bezug beispielsweise EUR-Lex und deutsche Bundesgesetze. Sekundärartikel oder alte Mustertexte ersetzen keine Prüfung der tatsächlich relevanten Informations-, Datenschutz-, Berufs-, Verbraucher-, Rechnungs- oder Vertragspflichten.

Bei einer konkreten rechtlichen oder betrieblichen Prüfung werden relevante Quellen mit Datum und bestätigter Aussage dokumentiert. Private Beratungsunterlagen und Identitätsnachweise verbleiben außerhalb des Repositories.
