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


@dp.message(F.text == "👤 Profilim")
async def show_profile(message: types.Message):
    telegram_id = message.from_user.id
    profile_data = await api.get_profile(telegram_id)

    if profile_data:
        text = (f"👤 <b>Sizning Profilingiz:</b>\n\n"
                f"👤 <b>Ism:</b> {profile_data.get('username', 'Ko\'rsatilmagan')}\n"
                f"📞 <b>Telefon:</b> {profile_data.get('phone_number', 'Kiritilmagan')}\n"
                f"📍 <b>Manzil:</b> {profile_data.get('address', 'Kiritilmagan')}")
        await message.answer(text)
    else:
        await message.answer("❌ Profilingiz topilmadi. Buyurtma berish jarayonida ma'lumotlaringiz saqlanadi.")

@dp.message(F.text == "📦 Buyurtmalarim")
async def show_orders(message: types.Message):
    telegram_id = message.from_user.id
    orders = await api.get_orders(telegram_id)

    if orders:
        text = "📦 <b>Sizning buyurtmalaringiz:</b>\n\n"
        for order in orders:
            status_emoji = "⏳" if order['status'] == 'pending' else "✅" if order['status'] == 'delivered' else "🔄"
            text += f"🆔 <b>Buyurtma #{order['id']}</b> - {status_emoji} {order['status']}\n"
            text += f"💰 <b>Jami:</b> {order['total_amount']} $\n"
            text += f"📅 <b>Sana:</b> {order['created_at'][:10]}\n"
            text += "-" * 20 + "\n"
        await message.answer(text)
    else:
        await message.answer("📭 Sizda hozircha tasdiqlangan buyurtmalar yo'q.")

@dp.message(F.text == "ℹ️ Ma'lumot")
async def show_info(message: types.Message):
    text = (
        "🏢 <b>Darvoza Bot - Sifatli Temir Darvozalar</b>\n\n"
        "Biz orqali siz eng zamonaviy va chidamli darvozalarni buyurtma qilishingiz mumkin. "
        "Barcha savollar bo'yicha admin bilan bog'laning."
    )
    await message.answer(text)

@dp.message(F.text == "📞 Bog'lanish")
async def contact_admin(message: types.Message):
    text = (
        "📞 <b>Biz bilan bog'lanish:</b>\n\n"
        "📱 <b>Telefon:</b> +998 90 123 45 67\n"
        "👨‍💻 <b>Admin:</b> @admin_username\n\n"
        "Shuningdek, bizga taklif yoki shikoyatlaringizni yuborishingiz mumkin. Shunchaki yozing!"
    )
    await message.answer(text)

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