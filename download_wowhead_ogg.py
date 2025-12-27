import os
import sys
import time
import subprocess
from urllib.parse import quote, urlparse

from playwright.sync_api import sync_playwright
from tts_cli.consts import RACE_DICT


URL_TEMPLATE = "https://www.wowhead.com/{lang}/sounds/npc-greetings/name:{term}"
BASE_OUTPUT_DIR = "sound-input"


# --------------------------------------------------
# Hilfsfunktionen
# --------------------------------------------------

def download_file(page, url, download_dir):
    filename = os.path.basename(urlparse(url).path)
    path = os.path.join(download_dir, filename)

    if os.path.exists(path):
        return path

    response = page.request.get(url)
    with open(path, "wb") as f:
        f.write(response.body())

    print(f"    ✔ {filename}")
    return path


def detect_gender(filename):
    name = filename.lower()
    if "female" in name or "-f" in name or "_f" in name:
        return "f"
    if "male" in name or "-m" in name or "_m" in name:
        return "m"
    return "unknown"


def merge_ogg_files(files, output_path):
    if not files:
        return

    with open("concat_list.txt", "w") as f:
        for file in files:
            f.write(f"file '{os.path.abspath(file)}'\n")

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", "concat_list.txt",
            "-c", "copy", output_path
        ],
        check=True
    )

    os.remove("concat_list.txt")

    for file in files:
        try:
            os.remove(file)
        except Exception:
            pass

    print(f"  ✅ Zusammengeführt: {os.path.basename(output_path)}")


# --------------------------------------------------
# Kernlogik
# --------------------------------------------------

def process_search_term(browser, language, race_name):
    race_name = str(race_name).strip().lower()
    encoded_term = quote(race_name)

    output_dir = os.path.join(BASE_OUTPUT_DIR, language, race_name)
    os.makedirs(output_dir, exist_ok=True)

    print("\n==============================")
    print(f"🌍 Sprache: {language}")
    print(f"🧬 Rasse:   {race_name}")
    print(f"📁 Ziel:    {output_dir}")
    print("==============================")

    counters = {"f": 1, "m": 1, "unknown": 1}
    page = browser.new_page()

    start_url = URL_TEMPLATE.format(lang=language, term=encoded_term)
    page.goto(start_url, timeout=60000)

    if not page.locator('//*[@id="lv-sounds"]').count():
        print("⚠ Keine Soundliste gefunden – übersprungen")
        page.close()
        return

    page.wait_for_selector('//*[@id="lv-sounds"]')

    while True:
        rows = page.locator('//*[@id="lv-sounds"]/div[2]/div/table/tbody/tr')
        if rows.count() == 0:
            break

        for i in range(rows.count()):
            npc_href = rows.nth(i).locator("td a").first.get_attribute("href")
            npc_url = npc_href if npc_href.startswith("http") else f"https://www.wowhead.com{npc_href}"

            npc_page = browser.new_page()
            npc_page.goto(npc_url, timeout=60000)
            time.sleep(0.4)

            ogg_links = npc_page.locator("a[href$='.ogg']")
            downloaded = []
            gender = None

            for j in range(ogg_links.count()):
                ogg_url = ogg_links.nth(j).get_attribute("href")
                path = download_file(npc_page, ogg_url, output_dir)
                downloaded.append(path)

                if gender is None:
                    gender = detect_gender(os.path.basename(path))

            if downloaded:
                gender = gender or "unknown"
                out_name = f"{gender}-{race_name}-{counters[gender]}.ogg"
                out_path = os.path.join(output_dir, out_name)
                merge_ogg_files(downloaded, out_path)
                counters[gender] += 1

            npc_page.close()
            time.sleep(0.2)

        next_btn = page.locator('//*[@id="lv-sounds"]//a[contains(@class,"next")]')
        if next_btn.count() == 0:
            break

        next_btn.click()
        page.wait_for_timeout(1200)

    page.close()


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python download_wowhead_ogg.py <sprache> [race]")
        sys.exit(1)

    language = sys.argv[1].lower()

    if len(sys.argv) >= 3:
        races = [sys.argv[2]]
    else:
        print("ℹ Kein Suchbegriff übergeben – verwende RACE_DICT")
        races = sorted(set(RACE_DICT.values()))

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for race in races:
            process_search_term(browser, language, race)

        browser.close()

    print("\n🎉 Fertig – alle Sounds verarbeitet.")


if __name__ == "__main__":
    main()
