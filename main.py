import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from data.config import API_TOKEN
from data.db import Database
from handlers import main_router
from aiohttp import web

# Initialize Flask app
app = Flask(__name__)

# Initialize storage, bot, and dispatcher
storage = MemoryStorage()
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)
db = Database()


async def start_bot():
    # Register routers or handlers
    main_router(dp=dp)
    # Start polling for updates
    await dp.start_polling(bot)


@app.route('/')
def index():
    return "Bot is running"


async def init_app():
    # Start the Flask app
    runner = web.AppRunner(web.Application())
    await runner.setup()
    site = web.TCPSite(runner, host='0.0.0.0', port=8000)
    await site.start()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_app())
    loop.run_until_complete(start_bot())
    loop.run_forever()
