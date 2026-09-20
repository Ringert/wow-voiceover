# Wesentliche Wissensänderungen

## 2026-09-20

- [Lokale WAV-Referenzen](project/user-manual.md#lokale-referenzstimmen-verwalten): NPC-Zuordnungen verwenden vollständige WAV-Pfade. Synthese sendet die Datei direkt als Multipart ohne Voice-ID; Generatoren, Stimmenwechsel und Regenerierung verwenden denselben Pfadvertrag. Die bisherigen Zuordnungen bleiben erhalten, Dateien sind noch bereitzustellen.

- [HTTP-Vertrag präzisiert](project/architecture.md): Explizite Syntheseparameter wiederhergestellt, Sprachcode `de` und Download über `file_id` gemäß Dienstanleitung. Für Payloadänderungen sind `/user-manual.md` und `/openapi.json` des konfigurierten Dienstes die aktuellen Referenzen.

- [Ausschließlicher Webservicebetrieb](project/architecture.md): Lokale Modellkonfiguration, alternativer Anbieterclient und Modelllaufzeit im Containerbuild entfernt. Syntheseparameter werden im Client-Payload an den Webservice übergeben; [Containeraufbau und Rebuild](project/local-development.md) sowie [Bedienung](project/user-manual.md) angepasst.

- [TTS-Konfiguration](project/user-manual.md#tts-adresse-einstellen): Protokoll, Host und Port werden für Synthese und Download gemeinsam aus `.env` beziehungsweise Umgebungsvariablen gelesen; [Architektur](project/architecture.md) und [Entwicklungsanleitung](project/local-development.md) nachgeführt.

- [Codex-Projektvorlage übernommen](sources/repository-baseline.md): Rollen, Standards, OKF-Wiki und Story-/PR-Konzept an das bestehende Python-/Lua-Projekt angepasst.
- [Projektbestand aufgenommen](sources/wow-voiceover-codebase.md): Architektur, Datenvertrag, Entwicklungsumgebung, Benutzerhandbuch, Auslieferung und Schutzgrenzen anhand des Codes dokumentiert.
- Widersprüche der älteren Anleitung geklärt: globale CLI-Optionen, Lookup-Erzeugung ohne Synthese, feste MySQL-/TTS-Konfiguration und begrenzte Locale-/Clientnachweise. Siehe [Projektentwicklung](project/local-development.md) und [Fachmodell](project/domain-model.md).
