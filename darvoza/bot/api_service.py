import aiohttp
import logging
from config import BASE_URL

TIMEOUT = aiohttp.ClientTimeout(total=10)

async def get_categories():
    try:
        async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
            url = f"{BASE_URL}kategoriyalar/"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                logging.error(f"API Xato: {response.status}")
                return []
    except Exception as e:
        logging.error(f"Ulanishda xato: {e}")
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
        logging.error(f"Mahsulot xatosi: {e}")
        return []