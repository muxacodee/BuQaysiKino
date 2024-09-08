import asyncio
import requests
from flask import Flask, request
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiohttp import web
from data.config import API_TOKEN
from data.db import Database
from handlers import main_router

# Initialize Flask app
app = Flask(__name__)

# Initialize storage, bot, and dispatcher
storage = MemoryStorage()
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)
db = Database()

# Webhook settings
WEBHOOK_PATH = '/webhook'
WEBHOOK_URL = 'https://buqaysikino.onrender.com' + WEBHOOK_PATH
WEBHOOK_SECRET = 'your-unique-secret-token'


async def on_startup(dp: Dispatcher):
    # Set webhook
    await bot.set_webhook(WEBHOOK_URL, secret_token=WEBHOOK_SECRET)


async def on_shutdown(dp: Dispatcher):
    # Remove webhook on shutdown
    await bot.delete_webhook()


@app.route('/')
def index():
    return "Bot is running"


@app.route(WEBHOOK_PATH, methods=['POST'])
async def handle_webhook():
    # Get the JSON data from the request
    update = await request.json()

    # Feed the update to the dispatcher
    await dp.feed_update(update)

    return 'ok'


async def ping_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully pinged {url}")
        else:
            print(f"Failed to ping {url}, Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error pinging {url}: {e}")


async def uptime_monitor(interval, url):
    while True:
        await asyncio.to_thread(ping_url, url)
        await asyncio.sleep(interval)


async def init_app():
    # Create an aiohttp web application
    aiohttp_app = web.Application()
    # Register webhook handler
    aiohttp_app.router.add_post(WEBHOOK_PATH, handle_webhook)
    runner = web.AppRunner(aiohttp_app)
    await runner.setup()
    site = web.TCPSite(runner, host='0.0.0.0', port=8000)
    await site.start()


async def main():
    # Start the Flask app and bot polling
    app.run(port=8000)
    await on_startup(dp)
    await init_app()

    # Start uptime monitoring
    await asyncio.gather(
        dp.start_polling(bot),
        uptime_monitor(5 * 60, 'https://buqaysikino.onrender.com')
    )


if __name__ == '__main__':
    asyncio.run(main())
