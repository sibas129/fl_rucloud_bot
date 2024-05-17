from aiogram import Bot, Dispatcher

import asyncio
import logging

from config import BOT_TOKEN


from handlers import commands_h, main_h
from handlers.calendar import calendar_main_h
from handlers.settings import setting_main_h
from handlers.personal import personal_main_h
from handlers.organizations import organizations_main_h


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main() -> None:
    dp.include_routers(
        commands_h.router,
        main_h.router,
        calendar_main_h.router,
        setting_main_h.router,
        personal_main_h.router,
        organizations_main_h.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
