import os
import sys
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("8684701971:AAEHDCEE2BoDYgI-VycfvUGUr6nYFtCzVp8")
ADMIN_ID = os.getenv("8549599284")

BASE_URL = os.getenv( "https://darvoza-1.onrender.com/api/")
DJANGO_HOST = os.getenv("DJANGO_HOST", "http://127.0.0.1:8000")

if not TOKEN:
    sys.exit("❌ XATO: BOT_TOKEN topilmadi!")

if not BASE_URL.endswith('/'):
    BASE_URL += '/'