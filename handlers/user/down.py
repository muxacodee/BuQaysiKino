import os
import requests
from states import DnS
from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputFile
from keyboards.default_k import UserDefaultMenu
from filters.filter import get_instagram_video_link

udm = UserDefaultMenu()
down_r = Router()
DOWNLOAD_DIR = 'downloads'

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)


@down_r.message(F.text == "📥 Video yuklash")
async def video(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(text="<b>⚙️ Ushbu qism hozirda ta'mirlash jarayonida</b>", parse_mode=ParseMode.HTML)
    # await message.reply(text="<b>Yuklab olmoqchi bo'lgan videoyingiz havolasini yuboring:</b>",
    #                     parse_mode=ParseMode.HTML, reply_markup=udm.back_menu())
    # await state.set_state(DnS.link)


@down_r.message(DnS.link)
async def download_and_send_content(message: Message):
    link = message.text.strip()

    if "instagram.com" in link:
        modified_link = link.replace("instagram.com", "ddinstagram.com")
        video_url = get_instagram_video_link(modified_link)

        if video_url:
            try:
                response = requests.get(video_url)
                if response.status_code == 200:
                    file_name = f"downloads/{video_url}.mp4"
                    with open(file_name, "wb") as file:
                        file.write(response.content)
                    insta_video = InputFile(file_name)
                    await message.reply_video(video=insta_video,
                                              caption=f"<b>💎 @BuQaysiKinoBot orqali yuklab olindi</b>")
                    os.remove(file_name)
                else:
                    await message.reply("Faylni yuklab bo'lmadi, qayta urinib ko'ring.")
            except Exception as e:
                await message.reply(f"Xatolik yuz berdi: {str(e)}")
        else:
            await message.reply("Kontent manzilini topib bo'lmadi. Qayta urinib ko'ring.")
    else:
        await message.reply("Iltimos, to'g'ri Instagram havolasini yuboring.")
