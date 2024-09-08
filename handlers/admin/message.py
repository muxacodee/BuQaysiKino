from states import AdS
from data.config import ADMIN_ID
from aiogram.enums import ParseMode
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from keyboards.default_k import UserDefaultMenu, AdminDefaultMenu
from data.db import Database

db = Database()
message_r = Router()
udm = UserDefaultMenu()
adm = AdminDefaultMenu()


@message_r.message(F.text == "📤 Xabar yuborish")
async def send_message(message: types.Message, state: FSMContext):
    await state.clear()
    if message.from_user.id == ADMIN_ID:
        await message.answer(text="<b>Iltimos yubormoqchi bo'lgan xabaringizni kiriting:</b>",
                             parse_mode=ParseMode.HTML, reply_markup=udm.back_menu())
        await state.set_state(AdS.content)
    else:
        pass


@message_r.message(AdS.content)
async def send_to_all(message: types.Message, state: FSMContext):
    all_user_ids = db.get_all_users()
    for user_id in all_user_ids:
        try:
            await message.send_copy(chat_id=user_id)
        except Exception as e:
            print(f"Xabar yuborishda xatolik: {user_id}: {e}")
    await state.clear()
    await message.answer(text="<b>Xabar yuborildi!</b>",
                         parse_mode=ParseMode.HTML,
                         reply_markup=adm.admin_menu())
