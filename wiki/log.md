# Wesentliche Wissensänderungen

## 2026-09-20

- [TTS-Konfiguration](project/user-manual.md#tts-adresse-einstellen): Protokoll, Host und Port werden für Synthese und Download gemeinsam aus `.env` beziehungsweise Umgebungsvariablen gelesen; [Architektur](project/architecture.md) und [Entwicklungsanleitung](project/local-development.md) nachgeführt.

- [Codex-Projektvorlage übernommen](sources/repository-baseline.md): Rollen, Standards, OKF-Wiki und Story-/PR-Konzept an das bestehende Python-/Lua-Projekt angepasst.
- [Projektbestand aufgenommen](sources/wow-voiceover-codebase.md): Architektur, Datenvertrag, Entwicklungsumgebung, Benutzerhandbuch, Auslieferung und Schutzgrenzen anhand des Codes dokumentiert.
- Widersprüche der älteren Anleitung geklärt: globale CLI-Optionen, Lookup-Erzeugung ohne Synthese, feste MySQL-/TTS-Konfiguration und begrenzte Locale-/Clientnachweise. Siehe [Projektentwicklung](project/local-development.md) und [Fachmodell](project/domain-model.md).
