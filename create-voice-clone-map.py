import json
import os
import random
import argparse

from tts_cli.consts import RACE_DICT, GENDER_DICT

OUTPUT_FILE = "voice-clone-map.json"
BASE_DIR = "sound-input"

def select_random_voice(language: str, race: str, gender: str):
    race_dir = os.path.join(BASE_DIR, language, race)

    if not os.path.isdir(race_dir):
        print(f"[WARN] Ordner fehlt: {race_dir}")
        return None

    prefix = "m" if gender == "male" else "f"

    candidates = [
        f for f in os.listdir(race_dir)
        if f.lower().startswith(prefix)
        and os.path.isfile(os.path.join(race_dir, f))
    ]

    if not candidates:
        print(f"[WARN] Keine Dateien '{prefix}*' in {race_dir}")
        return None

    file = random.choice(candidates)

    # 🔧 Dateiendung entfernen (ogg, wav, mp3, ...)
    filename_no_ext = os.path.splitext(file)[0]

    return f"{language}/{race}/{filename_no_ext}"

def get_race_key_from_string(text: str):
    text_lower = text.lower()

    for key, value in RACE_DICT.items():
        if value.lower() in text_lower:
            return key

    return None

def main():
    parser = argparse.ArgumentParser(description="Weist jedem Eintrag in output.json eine Voice zu.")
    parser.add_argument("language", type=str, help="Sprache, z.B. deDE oder enUS")
    args = parser.parse_args()

    language = args.language

    if os.path.exists(OUTPUT_FILE):
        print(f"Datei '{OUTPUT_FILE}' existiert bereits – Abbruch.")
        return

    with open("output.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        entries = data.get("entries", [])
    else:
        entries = data

    result = {}

    for entry in entries:
        name = entry.get("name")
        if not name or name in result:
            continue

        race_id = entry.get("DisplayRaceID", -1)
        gender_id = entry.get("DisplaySexID", 0)

        main_char_race_id = get_race_key_from_string(name)

        if(main_char_race_id is not None):
            race_id = main_char_race_id

        # map zandalari to troll 
        if(race_id == 31):
            race_id = 8

        race = RACE_DICT.get(race_id, "narrator")
        gender = GENDER_DICT.get(gender_id, "male")

        if race == "narrator":
            race = "human"

        voice = select_random_voice(language, race, gender)

        if not voice:
            voice = select_random_voice(language, race, gender)

        if voice:
            result[name] = f"{BASE_DIR}/{voice}"
        else:
            print(f"[ERROR] Keine Voice für '{name}' ({race}, {gender})")

    if not result:
        print("[FATAL] Keine einzige Voice gefunden – JSON bleibt leer.")
        return

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"[OK] {len(result)} Einträge in '{OUTPUT_FILE}' geschrieben.")


if __name__ == "__main__":
    main()
