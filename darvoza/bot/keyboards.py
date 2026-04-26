from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚪 Katalog"), KeyboardButton(text="📦 Buyurtmalarim")],
        [KeyboardButton(text="👤 Profilim"), KeyboardButton(text="ℹ️ Ma'lumot")],
        [KeyboardButton(text="📞 Bog'lanish")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Menyuni tanlang..."
)


def build_categories_kb(categories):
    builder = InlineKeyboardBuilder()
    for cat in categories:
        builder.button(text=f"📂 {cat['name']}", callback_data=f"category_{cat['id']}")
    builder.adjust(2)
    return builder.as_markup()

def buy_product_kb(product_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Sotib olish", callback_data=f"buy_{product_id}")]
    ])