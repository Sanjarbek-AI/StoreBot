from aiogram.dispatcher.filters.state import StatesGroup, State


class AddProduct(StatesGroup):
    name = State()
    price = State()
    about = State()
    image = State()
    category = State()
