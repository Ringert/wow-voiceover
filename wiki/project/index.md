# Projektspezifischer Kontext

Diese Seiten dokumentieren den untersuchten Bestand von **wow-voiceover**. Grundlage sind Quellcode, Konfiguration und der dokumentierte lokale Devcontainer. **To be defined** steht ausschließlich bei ungeklärten Verantwortungs- oder Betriebsentscheidungen; Codelektüre belegt keine Ingame- oder Ende-zu-Ende-Prüfung. Nicht zutreffende Bereiche werden mit kurzer Begründung geklärt. Roadmap, Release-Scope, Prioritäten, Reihenfolge, Abhängigkeiten, Status und Ticketchronik bleiben ausschließlich in GitHub.

Beginne mit der [Synthese zum Projektwissen](../concepts/project-knowledge.md) und den vom Auftrag betroffenen Seiten. Bestätigte Entscheidungen erhalten Quelle und Geltungsgrenze; tatsächlicher Bestand und Bedienung werden mit ihrer Umsetzung gepflegt. Der [Pflegevertrag](../schema.md) regelt Metadaten und Zusammenhänge.

## Projektseiten

- [GitHub-Workflow](github-workflow.md) - Rollen, Branches, Labels, Story-PRs und Einrichtung der übernommenen Automatisierung.

- [Projektarchitektur](architecture.md) - tatsächlich umgesetzte Komponenten, Schnittstellen und Systemgrenzen.
- [Geschäfts- und Publikationsinformationen](business-information.md) - belegte Tatsachen, Rechte und zulässige Verwendung.
- [Content und Informationsarchitektur](content-strategy.md) - Inhaltsbedarf, Sprachen, Navigation und redaktionelle Quellen.
- [Projektauslieferung und Betrieb](deployment.md) - reale Betriebsziele, Einstiegspunkte, Sicherung und Wiederherstellung.
- [Fachliches Modell](domain-model.md) - Begriffe, Rollen, Abläufe, Lebenszyklen und fachliche Invarianten.
- [Projektspezifische Entwicklung](local-development.md) - tatsächliche Compose-Dienste, manuelle Einrichtung und Prüfbefehle.
- [Projektidentität](project-identity.md) - Name, Repository, Branchkürzel, Verantwortungen und Sprache.
- [Produktvision](project-vision.md) - Problem, Zielgruppen, Nutzen, Produktgrenzen und Erfolg.
- [Projektreferenzen](references.md) - konkrete Quellen, Aktualität, Verantwortung und Verwendungsgrenzen.
- [Projektsicherheit und Datenschutz](security-and-privacy.md) - Schutzwerte, Threat Model, Kontrollen und Datenlebenszyklus.
- [Leistungen und Zusammenarbeit](services-and-collaboration.md) - projektrelevantes Angebot, Zusammenarbeit und verbindliche Zusagen.
- [Projekt-Tech-Stack](tech-stack.md) - bestätigter Kern, verwendete Werkzeuge und maßgebliche Versionierungsdateien.
- [UI-Leitfaden des Projekts](ui-ux.md) - gemeinsame Gestaltungsregeln, umgesetzte Tokens und Komponenten, Nutzerführung, Inhalt und Qualitätsziele.
- [Benutzerhandbuch](user-manual.md) - Produktverständnis, erste Schritte, tatsächliche Nutzeraufgaben, Nachschlagehilfe und Problemlösung.

## Dauerhafte Pflege

Eine allgemeine Regel beschreibt ein für mehrere Projekte gültiges Verfahren. Eine Projektseite erklärt die konkrete Domäne oder tatsächlich umgesetzte Lösung. Beides ist releaseunabhängig. Entscheidungen einer Story sind bis zur Umsetzung im GitHub-Artefakt maßgeblich; sie werden nicht als vorhandene Fähigkeit dokumentiert.

Dokumentation wird mit einer Verhaltens- oder Architekturänderung gepflegt. Sie erklärt Gründe, Einstiegspunkte, Grenzen und Bedienung, ohne Code oder Ticketverlauf zu duplizieren. Weitere Feature-Seiten entstehen erst mit den jeweiligen Fähigkeiten und werden hier gezielt verlinkt.
