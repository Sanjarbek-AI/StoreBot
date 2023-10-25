from aiogram import Bot


async def check_subscription(user_id: int, channel_id: int):
    try:
        bot = Bot.get_current()
        member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        return member.is_chat_member()

    except Exception as exc:
        print(exc)
        return False
