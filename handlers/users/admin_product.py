from aiogram import types

from data.config import ADMINS
from keyboards.default.admin import *
from loader import dp


@dp.message_handler(text="🍟 Products", chat_id=ADMINS, state="*")
async def admin_product_handler(message: types.Message):
    text = "Welcome to products menu"
    await message.answer(text=text, reply_markup=admin_product_menu)


