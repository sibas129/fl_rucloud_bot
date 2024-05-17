from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from keyboards import start_k

from utils.func_utils import auto_registration


router = Router()


@router.message(Command("start"))
async def start_command(message: Message) -> None:
    markup_inline = start_k.get()
    photo = FSInputFile("src/main.png")
    await message.answer_photo(
        photo=photo,
        caption=(
            "🎮 Это RuCloud - сервис, созданный для хранения данных и обмена ими "
            "с коллегами по работе."
        ),
        reply_markup=markup_inline,
    )
