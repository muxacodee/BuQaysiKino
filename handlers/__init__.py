from aiogram import Dispatcher


def main_router(dp: Dispatcher):
    from handlers.user.info import info_r
    from handlers.user.echo import echo_r
    from handlers.user.down import down_r
    from handlers.user.start import start_r
    from handlers.user.movie import movie_r
    from handlers.admin.admin import admin_r
    from handlers.admin.message import message_r
    dp.include_routers(start_r, admin_r, down_r, movie_r, info_r, message_r, echo_r)
