from aiogram.fsm.state import State, StatesGroup


class MovieStates(StatesGroup):
    movie_id = State()


class DownStates(StatesGroup):
    link = State()


class AdsStates(StatesGroup):
    content = State()
