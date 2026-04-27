import os
import sys
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000/api/")
DJANGO_HOST = os.getenv("DJANGO_HOST", "http://127.0.0.1:8000")

if not TOKEN:
    sys.exit("❌ XATO: BOT_TOKEN topilmadi!")

if not BASE_URL.endswith('/'):
    BASE_URL += '/'