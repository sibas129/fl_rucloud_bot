from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="🗂 Здесь", callback_data=f"test"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="🗂 будут", callback_data=f"test"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="🗂 ваши папки", callback_data=f"test"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="📑 и файлы", callback_data=f"test"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(text="🔙 В главное меню", callback_data="main_menu")
    )
    return builder.as_markup(resize_keyboard=True)