from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from keyboards.organizations import organizations_main_k
from aiogram.enums.parse_mode import ParseMode


router = Router()


@router.callback_query(F.data == "organizations_main")
async def main_menu(callback: CallbackQuery) -> None:
    await callback.message.delete()
    photo = FSInputFile("src/organizations.png")
    markup_inline = organizations_main_k.get()
    await callback.message.answer_photo(
        photo=photo,
        caption="> 📂 Это раздел организаций, из него вы можете попасть в рабочую область любой из ваших организаций\.",
        reply_markup=markup_inline,
        parse_mode=ParseMode.MARKDOWN_V2
    )
