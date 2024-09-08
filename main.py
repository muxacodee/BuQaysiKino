import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from data.config import API_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from data.db import Database
from handlers import main_router

storage = MemoryStorage()
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)
db = Database()


async def main():
    main_router(dp=dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
