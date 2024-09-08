from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from data.db import Database


start_r = Router()
db = Database()


@start_r.message(CommandStart())
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    firstname = message.from_user.first_name

    if not db.check_user(user_id=user_id):
        db.add_user(user_id=user_id)
        await message.reply(text=f"<b>Salom, {firstname}! Sizni ko‘rganimdan juda xursandman. </b>",
                            parse_mode=ParseMode.HTML)
    else:
        await message.reply(f"<b>🖥 Asosiy menyudasiz.</b>",
                            parse_mode=ParseMode.HTML)

