from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.admin import admin_main_menu
from loader import dp


@dp.message_handler(CommandStart(), chat_id=ADMINS, state="*")
async def bot_start(message: types.Message):
    text = "Assalomu alaylum, welcome back sir 🫡"
    await message.answer(text=text, reply_markup=admin_main_menu)


