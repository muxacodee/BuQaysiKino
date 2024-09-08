from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

info_r = Router()


@info_r.message(Command(commands=['help']))
@info_r.message(F.text == "📋 Ma'lumotlar")
async def send_help(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply(text="<b>🤷‍♂️ Hozircha ma'lumotlar mavjud emas.</b>", parse_mode=ParseMode.HTML)
