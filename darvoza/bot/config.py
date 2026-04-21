import os
import sys
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

# Telegram Bot sozlamalari
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

# API va Host sozlamalari
BASE_URL = os.getenv("BASE_URL")
DJANGO_HOST = os.getenv("DJANGO_HOST")

# Pro himoya: Agar .env dagi eng muhim ma'lumotlar bo'lmasa, dastur ishga tushmaydi
if not all([TOKEN, BASE_URL, DJANGO_HOST]):
    sys.exit("❌ XATO: .env faylida kerakli o'zgaruvchilar (BOT_TOKEN, BASE_URL yoki DJANGO_HOST) topilmadi!")