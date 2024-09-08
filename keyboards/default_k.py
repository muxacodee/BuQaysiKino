from keyboards import RkB, RBtn


class UserDefaultMenu:
    @staticmethod
    def main_menu():
        keyboard = RkB(markup=[
            [
                RBtn(text="🔍 Kino qidirish"),
            ],
            [
                RBtn(text="📥 Video yuklash"),
                RBtn(text="📋 Ma'lumotlar"),
            ]
        ]).as_markup(resize_keyboard=True)
        return keyboard

    @staticmethod
    def back_menu():
        keyboard = RkB(markup=[
            [
                RBtn(text="◀️ Orqaga")
            ]
        ]).as_markup(resize_keyboard=True)
        return keyboard


class AdminDefaultMenu:
    @staticmethod
    def admin_menu():
        keyboard = RkB(markup=[
            [
                RBtn(text="📤 Xabar yuborish")
            ]
        ]).as_markup(resize_keyboard=True)
        return keyboard
