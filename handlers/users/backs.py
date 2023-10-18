from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.admin import *
from loader import dp


@dp.message_handler(text="🔙 Back To Main Menu", chat_id=ADMINS, state="*")
async def admin_product_handler(message: types.Message, state: FSMContext):
    text = "Welcome to main menu"
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.message_handler(text="🔙 Back To Products Menu", chat_id=ADMINS, state="*")
async def admin_product_handler(message: types.Message):
    text = "Welcome to Products menu"
    await message.answer(text=text, reply_markup=admin_product_menu)
