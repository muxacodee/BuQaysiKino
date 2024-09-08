from data.db import Database
from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from keyboards.default_k import UserDefaultMenu


udm = UserDefaultMenu()
start_r = Router()
db = Database()


@start_r.message(CommandStart())
@start_r.message(F.text == "◀️ Orqaga")
async def send_welcome(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await state.clear()
    if not db.check_user(user_id=user_id):
        db.add_user(user_id=user_id)
        await message.reply(text=f"<b>Salom, {firstname}! Sizni ko‘rganimdan juda xursandman. </b>",
                            parse_mode=ParseMode.HTML, reply_markup=udm.main_menu())
    else:
        await message.reply(f"<b>🖥 Asosiy menyudasiz.</b>",
                            parse_mode=ParseMode.HTML, reply_markup=udm.main_menu())

