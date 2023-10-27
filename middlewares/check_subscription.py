from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from data.config import CHANNELS
from keyboards.inline.user import user_not_member_channels_def
from utils.check_sub import check_subscription


class ChannelChecker(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            message = update.message
        elif update.callback_query:
            message = update.callback_query.message
        else:
            return
        user_id = message.chat.id

        not_member = []
        for channel in CHANNELS:
            if not await check_subscription(user_id, channel['id']):
                not_member.append(channel)

        if len(not_member) != 0:
            await message.answer(text="Siz kanalga a'zo bo'lmagansiz",
                                 reply_markup=await user_not_member_channels_def(not_member))

            raise CancelHandler()
