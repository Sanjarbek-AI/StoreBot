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


async def admin_product_update_keyboards(product):
    product_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Delete 🗑", callback_data=product[0]),
                InlineKeyboardButton("Update 🔄", callback_data=product[0]),
            ]
        ]
    )
    return product_markup
