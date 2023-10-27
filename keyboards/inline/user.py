from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def user_not_member_channels_def(not_member: list):
    markup = InlineKeyboardMarkup(row_width=1)
    checking = InlineKeyboardButton(text="Check ✅", callback_data="check_subscription")

    for channel in not_member:
        button = InlineKeyboardButton(text=channel['name'], url=channel["link"])
        markup.add(button)
    markup.add(checking)
    return markup
