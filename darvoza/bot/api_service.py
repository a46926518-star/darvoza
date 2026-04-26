import aiohttp
from config import BASE_URL
import logging

async def get_profile(telegram_id):
    """Mijoz profilini API dan olish"""
    url = f"{BASE_URL}profile/{telegram_id}/" # Renderdagi URL
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 404:
                     return None # Profil yo'q bo'lsa
                else:
                    logging.error(f"API Profil xatosi: {response.status}")
                    return None
        except Exception as e:
            logging.error(f"Ulanish xatosi (Profile): {e}")
            return None

async def get_orders(telegram_id):
    url = f"{BASE_URL}orders/"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    all_orders = await response.json()
                    user_orders = [o for o in all_orders if o.get('user_telegram_id') == telegram_id]
                    return user_orders
                else:
                     logging.error(f"API Buyurtmalar xatosi: {response.status}")
                     return None
        except Exception as e:
             logging.error(f"Ulanish xatosi (Orders): {e}")
             return None