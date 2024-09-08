from aiogram.types import Message
from aiogram import Router

echo_r = Router()


@echo_r.message()
async def echo(message: Message):
    await message.send_copy(message.from_user.id)
