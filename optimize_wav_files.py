#!/usr/bin/env python3
import os
import subprocess

INPUT_DIR = "sound-input"
TARGET_SR = 22050
TARGET_FORMAT = "pcm_s16le"

for root, dirs, files in os.walk(INPUT_DIR):
    for file in files:
        if file.lower().endswith(".wav"):
            file_path = os.path.join(root, file)
            temp_path = file_path + ".tmp.wav"  # temporäre Datei

            cmd = [
                "ffmpeg",
                "-y",
                "-i", file_path,
                "-ac", "1",  # Mono
                "-ar", str(TARGET_SR),  # Sample Rate
                "-c:a", TARGET_FORMAT,
                temp_path
            ]

            print(f"Konvertiere: {file_path}")
            try:
                subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                os.replace(temp_path, file_path)  # Original überschreiben
            except subprocess.CalledProcessError as e:
                print(f"FEHLER bei {file_path}: {e}")
                if os.path.exists(temp_path):
                    os.remove(temp_path)

print("Fertig! Alle WAVs wurden konvertiert und Originaldateien überschrieben.")
