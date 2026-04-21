import aiohttp
import logging
from config import BASE_URL

# Server javob bermasa bot qotib qolmasligi uchun 10 soniyalik limit (Pro yondashuv)
TIMEOUT = aiohttp.ClientTimeout(total=10)

async def get_categories():
    try:
        async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
            async with session.get(f"{BASE_URL}kategoriyalar/") as response:  # To'g'ri
                if response.status == 200:
                    return await response.json()
                logging.warning(f"Kategoriya olishda xato. Status: {response.status}")
                return []
    except Exception as e:
        logging.error(f"Kategoriyani olishda xatolik: {e}")
        return []

async def get_products_by_category(category_id):
    try:
        async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
            url = f"{BASE_URL}mahsulotlar/?category={category_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                return []
    except Exception as e:
        logging.error(f"Mahsulotlarni olishda xatolik: {e}")
        return []