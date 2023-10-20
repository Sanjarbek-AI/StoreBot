from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db_manager

admin_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍟 Products"),
            KeyboardButton(text="🛒 Orders")
        ],
        [
            KeyboardButton(text="📊 Statistics"),
            KeyboardButton(text="⏏️ Send Message")
        ]
    ], resize_keyboard=True
)

admin_product_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍕 Products"),
            KeyboardButton(text="📝 Categories")
        ],
        [
            KeyboardButton(text="🔙 Back To Main Menu")
        ]
    ], resize_keyboard=True
)

admin_product_inside_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Add Product")
        ],
        [
            KeyboardButton(text="🔙 Back To Products Menu")
        ]
    ], resize_keyboard=True
)


async def admin_category_inside_menu_def():
    categories = db_manager.get_all_categories()
    cat_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    add_cat = KeyboardButton(text="➕ Add Category")
    back = KeyboardButton(text="🔙 Back To Products Menu")
    cat_markup.insert(add_cat)
    cat_markup.insert(back)

    for cat in categories:
        button = KeyboardButton(text=cat[1])
        cat_markup.insert(button)

    return cat_markup


async def admin_product_inside_menu_def():
    products = db_manager.get_all_products()
    product_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    add_cat = KeyboardButton(text="➕ Add Product")
    back = KeyboardButton(text="🔙 Back To Products Menu")
    product_markup.insert(add_cat)
    product_markup.insert(back)

    for cat in products:
        button = KeyboardButton(text=cat[1])
        product_markup.insert(button)

    return product_markup


async def admin_categories_menu_def():
    categories = db_manager.get_all_categories()
    cat_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    for cat in categories:
        button = KeyboardButton(text=cat[1])
        cat_markup.insert(button)

    return cat_markup
