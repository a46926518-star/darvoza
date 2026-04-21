import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import keyboards as kb
import api_service as api
from config import TOKEN, DJANGO_HOST

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# --- 1. Start buyrug'i ---
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, <b>{message.from_user.full_name}</b>!\nDarvoza savdo botiga xush kelibsiz.",
        reply_markup=kb.main_menu
    )

# --- 2. Katalog va Mahsulotlar ---
@dp.message(F.text == "🚪 Katalog")
async def show_categories(message: types.Message):
    data = await api.get_categories()
    if data:
        await message.answer("<b>Kategoriyani tanlang:</b>", reply_markup=kb.build_categories_kb(data))
    else:
        await message.answer("📭 Hozircha kategoriyalar yo'q yoki server bilan ulanishda xato.")

@dp.callback_query(F.data.startswith("category_"))
async def show_products(callback: types.CallbackQuery):
    cat_id = callback.data.split("_")[1]
    products = await api.get_products_by_category(cat_id)

    if not products:
        await callback.message.answer("❌ Bu bo'limda mahsulotlar yo'q.")
    else:
        for p in products:
            caption = (
                f"🏷 <b>{p.get('name', 'Nomsiz')}</b>\n"
                f"💰 Narxi: <b>{p.get('price', '0')} $</b>\n\n"
                f"📝 <i>{p.get('description') or 'Tavsif mavjud emas.'}</i>"
            )
            img_url = p.get('image')

            if img_url:
                if not img_url.startswith('http'):
                    img_url = f"{DJANGO_HOST.rstrip('/')}{img_url}"
                try:
                    await callback.message.answer_photo(
                        photo=img_url,
                        caption=caption,
                        reply_markup=kb.buy_product_kb(p['id'])
                    )
                except Exception as e:
                    logging.error(f"Rasm yuborishda xato: {e}")
                    await callback.message.answer(caption, reply_markup=kb.buy_product_kb(p['id']))
            else:
                await callback.message.answer(caption, reply_markup=kb.buy_product_kb(p['id']))
    await callback.answer()

# --- 3. Qolgan asosiy menyu tugmalari ---
@dp.message(F.text == "👤 Profilim")
async def show_profile(message: types.Message):
    text = (
        f"👤 <b>Sizning profilingiz:</b>\n\n"
        f"🆔 ID: <code>{message.from_user.id}</code>\n"
        f"👤 Ism: {message.from_user.full_name}\n"
        f"🌐 Til: {message.from_user.language_code}"
    )
    await message.answer(text)

@dp.message(F.text == "📦 Buyurtmalarim")
async def show_orders(message: types.Message):
    await message.answer("📦 Hozircha sizda faol buyurtmalar mavjud emas.")

@dp.message(F.text == "📞 Bog'lanish")
async def contact_us(message: types.Message):
    await message.answer(
        "📞 <b>Biz bilan bog'lanish:</b>\n\n"
        "📍 Manzil: Farg'ona viloyati\n"
        "☎️ Telefon: +998 91 857 18 11\n"
        "👨‍💻 Admin: @darvozaadmin\n"
        "Savollaringiz bo'lsa, bemalol qo'ng'iroq qiling!"
    )

@dp.message(F.text == "ℹ️ Ma'lumot")
async def info_cmd(message: types.Message):
    await message.answer(
        "ℹ️ <b>Bot haqida:</b>\n\n"
        "Ushbu bot darvoza savdosi bilan shug'ullanuvchi korxona uchun maxsus ishlab chiqilgan. "
        "Bu yerda siz turli xil (temir, yog'och, avtomat) darvozalarni ko'rishingiz va buyurtma berishingiz mumkin."
    )

# --- 4. Buyurtma berish tugmasi ---
@dp.callback_query(F.data.startswith("buy_"))
async def process_buy(callback: types.CallbackQuery):
    product_id = callback.data.split("_")[1]
    await callback.message.answer(
        f"✅ Buyurtmangiz qabul qilindi (ID: {product_id}).\n"
        f"Tez orada operatorimiz siz bilan bog'lanadi!"
    )
    await callback.answer()

# --- 5. Ishga tushirish (Main) ---
async def main():
    logging.info("🚀 Bot ishga tushirildi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot to'xtatildi.")