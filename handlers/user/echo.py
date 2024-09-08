from aiogram.types import Message
from aiogram import Router
from handlers.start import send_welcome

echo_r = Router()


@echo_r.message()
async def echo(message: Message):
    return await send_welcome(message)
