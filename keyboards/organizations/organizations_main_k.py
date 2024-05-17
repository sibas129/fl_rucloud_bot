from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="🏢 Здесь будет", callback_data=f"test"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="🏢 список организаций", callback_data=f"test"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="🏢 в которых вы состоите", callback_data=f"test"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="💎🏢 и которыми владеете", callback_data=f"test"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(text="🔙 В главное меню", callback_data="main_menu")
    )
    return builder.as_markup(resize_keyboard=True)