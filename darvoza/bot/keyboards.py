from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚪 Katalog")],
        [KeyboardButton(text="👤 Profilim"), KeyboardButton(text="📦 Buyurtmalarim")],
        [KeyboardButton(text="📞 Bog'lanish"), KeyboardButton(text="ℹ️ Ma'lumot")]
    ],
    resize_keyboard=True
)

def build_categories_kb(categories):
    builder = InlineKeyboardBuilder()
    for cat in categories:
        builder.button(text=cat['name'], callback_data=f"category_{cat['id']}")
    builder.adjust(2) # Tugmalarni 2 tadan qilib taxlaydi
    return builder.as_markup()

def buy_product_kb(product_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=f"buy_{product_id}")]
        ]
    )