from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from keyboards.personal import personal_main_k
from aiogram.enums.parse_mode import ParseMode


router = Router()


@router.callback_query(F.data == "personal_main")
async def main_menu(callback: CallbackQuery) -> None:
    await callback.message.delete()
    photo = FSInputFile("src/personal.png")
    markup_inline = personal_main_k.get()
    await callback.message.answer_photo(
        photo=photo,
        caption="> 📂 Это раздел личных файлов, здесь вы можете хранить файлы, которыми не планируте делиться с коллегами\.",
        reply_markup=markup_inline,
        parse_mode=ParseMode.MARKDOWN_V2
    )
