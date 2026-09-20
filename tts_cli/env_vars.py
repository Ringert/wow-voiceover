import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

MYSQL_HOST = "0.0.0.0"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "wow"
MYSQL_DATABASE = "wow"

# Shared origin for synthesis and audio downloads.
TTS_PROTOCOL = os.getenv("TTS_PROTOCOL", "http")
TTS_HOST = os.getenv("TTS_HOST", "localhost")
TTS_PORT = os.getenv("TTS_PORT", "8000")
TTS_BASE_URL = f"{TTS_PROTOCOL}://{TTS_HOST}:{TTS_PORT}"
