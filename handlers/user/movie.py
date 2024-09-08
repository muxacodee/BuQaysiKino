from main import bot
from states import MvS
from aiogram.enums import ParseMode
from aiogram import Router, types, F
from filters.filter import is_valid_id
from aiogram.fsm.context import FSMContext
from data.config import CHANNEL_ID, ADMIN_ID
from aiogram.exceptions import TelegramBadRequest
from keyboards.default_k import UserDefaultMenu

udm = UserDefaultMenu()
movie_r = Router()


@movie_r.message(F.text == "🔍 Kino qidirish")
async def get_movie_id(message: types.Message, state: FSMContext):
    await state.clear()
    await state.set_state(MvS.movie_id)
    await message.reply(text="<b>Iltimos, kino ID kiriting:</b>",
                        parse_mode=ParseMode.HTML,
                        reply_markup=udm.back_menu())


@movie_r.message(MvS.movie_id)
async def send_movie(message: types.Message, state: FSMContext):
    movie_id = message.text.strip()
    await state.update_data(movie_id=movie_id)
    user_id = message.from_user.id
    if not is_valid_id(movie_id=movie_id):
        await message.reply(text="<b>Iltimos, faqatgina raqamlardan iborat bo‘lgan IDni yuboring.</b>",
                            parse_mode=ParseMode.HTML, reply_markup=udm.back_menu())
        return

    try:
        await bot.forward_message(chat_id=user_id,
                                  from_chat_id=CHANNEL_ID,
                                  message_id=movie_id)
    except TelegramBadRequest:
        await message.reply(text="<b>Kino topilmadi. Iltimos kino ID sini yana bir bor tekshirib ko'ring va qayta "
                                 "yuboring:</b>", parse_mode=ParseMode.HTML, reply_markup=udm.back_menu())
        return
    except Exception as e:
        await bot.send_message(chat_id=ADMIN_ID,
                               text=f"{e}")
        await message.reply(text="<b>Kino topilmadi. Iltimos kino ID sini yana bir bor tekshirib ko'ring va qayta "
                                 "yuboring:</b>", parse_mode=ParseMode.HTML, reply_markup=udm.back_menu())
        return
    await state.clear()
