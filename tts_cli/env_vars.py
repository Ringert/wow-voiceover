from dotenv import load_dotenv
load_dotenv()
import os

MYSQL_HOST = "0.0.0.0"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "wow"
MYSQL_DATABASE = "wow"
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
