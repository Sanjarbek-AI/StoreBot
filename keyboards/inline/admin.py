from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def admin_category_update_keyboards(category):
    cat_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Delete 🗑", callback_data=category[0]),
                InlineKeyboardButton("Update 🔄", callback_data=category[0]),
            ]
        ]
    )
    return cat_markup
