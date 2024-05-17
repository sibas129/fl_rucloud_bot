from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="📂 Личные файлы", callback_data=f"personal_main"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="🏢 Мои организации", callback_data=f"organizations_main"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="⚙️ Настройки аккаунта", callback_data=f"settings_main"
        ),
        types.InlineKeyboardButton(
            text="📆 Календарь событий", callback_data=f"calendar_main"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="💬 Открыть приложение в браузере",
            url="https://nextcloud.prosto-web.agency",
        )
    )
    return builder.as_markup(resize_keyboard=True)
