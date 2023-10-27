from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import CHANNELS
from keyboards.default.user import user_main_menu
from keyboards.inline.user import user_not_member_channels_def
from loader import dp
from utils.check_sub import check_subscription


@dp.callback_query_handler(text="check_subscription")
async def check_user_sub_handler(call: types.CallbackQuery):
    not_member = []
    for channel in CHANNELS:
        if not await check_subscription(call.message.chat.id, channel['id']):
            print(channel)
            not_member.append(channel)
    if len(not_member) == 0:
        text = "Assalomu alaykum."
        await call.message.answer(text=text, reply_markup=user_main_menu)
    else:
        await call.message.answer(text="Siz kanalga a'zo bo'lmagansiz",
                                  reply_markup=await user_not_member_channels_def(not_member))


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = "Assalomu alaykum."
    await message.answer(text=text, reply_markup=user_main_menu)
