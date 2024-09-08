import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from data.config import API_TOKEN
from data.db import Database
from handlers import main_router
import threading

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


def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())


@app.route('/')
def index():
    return "Bot is running"


if __name__ == '__main__':
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Start Flask app
    app.run(host='0.0.0.0', port=8000, debug=True)
