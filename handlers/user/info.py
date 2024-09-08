from aiogram import Router, types, F
from aiogram.filters import Command

info_r = Router()


@info_r.message(Command(commands=['help']))
@info_r.message(F.text("📋 Ma'lumotlar"))
async def send_help(message: types.Message):
    await message.reply(text="Hozircha ma'lumotlar mavjud emas.")
