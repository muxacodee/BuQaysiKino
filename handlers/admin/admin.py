from aiogram import Router
from data.config import ADMIN_ID
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from keyboards.default_k import AdminDefaultMenu

admin_r = Router()
adm = AdminDefaultMenu()


@admin_r.message(Command(commands=['admin', 'panel']))
async def admin(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.reply("<b>Admin panelga hush kelibsiz.</b>",
                            parse_mode=ParseMode.HTML,
                            reply_markup=adm.admin_menu())
    else:
        pass

