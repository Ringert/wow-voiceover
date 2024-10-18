from dotenv import load_dotenv
load_dotenv()
import os

MYSQL_HOST = "localhost"
MYSQL_PORT = 1234
MYSQL_USER = "root"
MYSQL_PASSWORD = "mysql"
MYSQL_DATABASE = "wow"
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
