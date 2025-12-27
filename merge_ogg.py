#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
import tempfile


def merge_ogg_files(file1, file2, output_path):
    files = [file1, file2]

    for f in files:
        if not os.path.isfile(f):
            print(f"❌ Datei nicht gefunden: {f}")
            sys.exit(1)

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as concat_file:
        for file in files:
            concat_file.write(f"file '{os.path.abspath(file)}'\n")
        concat_list_path = concat_file.name

    try:
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-f", "concat", "-safe", "0",
                "-i", concat_list_path,
                "-c", "copy",
                output_path
            ],
            check=True
        )
    except subprocess.CalledProcessError:
        print("❌ ffmpeg Fehler beim Zusammenfügen")
        sys.exit(1)
    finally:
        os.remove(concat_list_path)

    print(f"✅ Zusammengeführt: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Fügt zwei OGG-Audiodateien zu einer zusammen (ohne Re-Encoding)"
    )
    parser.add_argument("file1", help="Erste OGG-Datei (relativ oder absolut)")
    parser.add_argument("file2", help="Zweite OGG-Datei (relativ oder absolut)")
    parser.add_argument(
        "-o", "--output",
        default="merged.ogg",
        help="Ausgabedatei (Standard: merged.ogg)"
    )

    args = parser.parse_args()
    merge_ogg_files(args.file1, args.file2, args.output)


if __name__ == "__main__":
    main()
