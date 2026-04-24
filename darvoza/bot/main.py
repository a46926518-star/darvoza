import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import keyboards as kb
import api_service as api
from config import TOKEN, DJANGO_HOST

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(f"Xush kelibsiz, {message.from_user.full_name}!", reply_markup=kb.main_menu)


@dp.message(F.text == "🚪 Katalog")
async def show_categories(message: types.Message):
    data = await api.get_categories()
    if data:
        await message.answer("<b>Kategoriyani tanlang:</b>", reply_markup=kb.build_categories_kb(data))
    else:
        await message.answer("📭 Hozircha katalog bo'sh yoki server uyg'onmagan.")


@dp.callback_query(F.data.startswith("category_"))
async def show_products(callback: types.CallbackQuery):
    cat_id = callback.data.split("_")[1]
    products = await api.get_products_by_category(cat_id)

    if not products:
        await callback.message.answer("❌ Mahsulot topilmadi.")
    else:
        for p in products:
            caption = f"🏷 <b>{p['name']}</b>\n💰 Narxi: {p['price']} $\n\n{p.get('description', '')}"
            img_url = p.get('image')

            # Agar rasm URL'i to'liq bo'lmasa, hostni qo'shamiz
            if img_url and not img_url.startswith('http'):
                img_url = f"{DJANGO_HOST.rstrip('/')}{img_url}"

            if img_url:
                await callback.message.answer_photo(photo=img_url, caption=caption,
                                                    reply_markup=kb.buy_product_kb(p['id']))
            else:
                await callback.message.answer(caption, reply_markup=kb.buy_product_kb(p['id']))
    await callback.answer()


async def main():
    logging.info("🚀 Bot ishladi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())