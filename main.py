import asyncio
from handlers import main_router
from data.config import API_TOKEN
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

storage = MemoryStorage()
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)


async def main():
    main_router(dp=dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
