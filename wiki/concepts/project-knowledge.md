---
type: Concept
title: Projektwissen klären und belegt fortschreiben
description: Verbindet belegte Projektinformationen und offene Entscheidungen mit ihren Quellen und zuständigen Rollen.
tags: [project, context, decisions]
status: stable
scope: shared
sources:
  - id: template-adoption
    resource: https://github.com/Ringert/Codex-Projektvorlage/blob/b001e1b700d75aa0f31f6ced84381ba194b79582/wiki/concepts/project-knowledge.md
  - id: governance
    resource: ../standards/governance.md
  - id: documentation
    resource: ../standards/documentation.md
  - id: identity
    resource: ../project/project-identity.md
  - id: stack
    resource: ../project/tech-stack.md
generated:
  by: codex/gpt-6-astra
  at: 2026-09-20T00:24:56Z
---
# Projektwissen klären und belegt fortschreiben

Die [Projektseiten](../project/index.md) beschreiben den untersuchten Python-/Lua-Bestand von wow-voiceover. Nur nicht belegte Entscheidungen bleiben `To be defined`; tatsächliche Grenzen stehen bei den betroffenen Komponenten. Kopierte Werkzeuge und gemeinsame Standards belegen kein konkretes Produkt, keine Geschäftsidentität und keinen bestätigten Produktstack. Ein begründet nicht benötigter Bereich kann als „Nicht zutreffend“ geklärt werden.

| Leserfrage | Maßgebliche Projektseiten |
| --- | --- |
| Für wen und wozu entsteht das Produkt? | [Identität](../project/project-identity.md), [Vision](../project/project-vision.md), [fachliches Modell](../project/domain-model.md) |
| Welche Aussagen und Zusammenarbeit sind bestätigt? | [Leistungen](../project/services-and-collaboration.md), [Geschäftsinformationen](../project/business-information.md), [Referenzen](../project/references.md) |
| Wie wird das Produkt verstanden und bedient? | [Content](../project/content-strategy.md), [UI-Leitfaden](../project/ui-ux.md), [Benutzerhandbuch](../project/user-manual.md) |
| Wie funktioniert die tatsächliche Umsetzung? | [Architektur](../project/architecture.md), [Stack](../project/tech-stack.md), [Entwicklung](../project/local-development.md) |
| Welche Schutz- und Betriebsgrenzen gelten konkret? | [Sicherheit](../project/security-and-privacy.md), [Betrieb](../project/deployment.md) |

## Von der Entscheidung zur Wissensseite

Halte bestätigte dauerhafte Produktentscheidungen mit Quelle und Geltungsgrenze fest. Storypläne und Lieferstatus bleiben in GitHub. Mit der tatsächlichen Umsetzung beschreibt der Documentation Writer das Ergebnis in den betroffenen Projektseiten und verknüpften Synthesen. Technische Entscheidungen verantwortet der Tech Lead, fachliche der Product Owner, Gestaltung der UX Designer.

Die [Storysynthese](story-delivery.md) verbindet diese Beiträge. Der [Dokumentationsvertrag](../standards/documentation.md) regelt Schreibumfang und Nachweise. Angaben zur Verfügbarkeit benötigen tatsächliche Release-/Betriebsevidenz; ein Merge allein genügt nicht. Ein neues Wikiformat widerruft keine vorhandene Freigabe und macht aus einer offenen Frage keine bestätigte Tatsache.

Bei jeder betroffenen Änderung werden Quelle, Text, Metadaten, Index und direkt abhängige Zusammenfassungen gemeinsam nach dem [Wiki-Pflegevertrag](../schema.md) fortgeschrieben. Neue Seiten entstehen bei eigenständigem Leserbedarf, ohne leere Kategorien auf Vorrat.
