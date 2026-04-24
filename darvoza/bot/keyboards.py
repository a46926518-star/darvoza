from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Asosiy menyu
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚪 Katalog"), KeyboardButton(text="📦 Buyurtmalarim")],
        [KeyboardButton(text="👤 Profilim"), KeyboardButton(text="ℹ️ Ma'lumot")],
        [KeyboardButton(text="📞 Bog'lanish")]
    ],
    resize_keyboard=True
)

# Kategoriyalar uchun Inline tugmalar
def build_categories_kb(categories):
    builder = InlineKeyboardBuilder()
    for cat in categories:
        builder.button(text=cat['name'], callback_data=f"category_{cat['id']}")
    builder.adjust(2) # 2 tadan qator qilib tizish
    return builder.as_markup()

# Sotib olish tugmasi
def buy_product_kb(product_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Sotib olish", callback_data=f"buy_{product_id}")]
    ])