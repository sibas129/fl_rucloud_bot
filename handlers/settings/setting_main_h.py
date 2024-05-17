from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from keyboards.settings import setting_main_k
from aiogram.enums.parse_mode import ParseMode


router = Router()


@router.callback_query(F.data == "settings_main")
async def main_menu(callback: CallbackQuery) -> None:
    await callback.message.delete()
    photo = FSInputFile("src/settings.png")
    markup_inline = setting_main_k.get()
    await callback.message.answer_photo(
        photo=photo,
        caption="> ⚙️ Это раздел настроек аккаунта, здесь вы можете поменять имя или статус, а также добавить новую организацию\.\nУправление ее будет доступно в разделе '🏢 Мои организации'",
        reply_markup=markup_inline,
        parse_mode=ParseMode.MARKDOWN_V2
    )
