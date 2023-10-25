from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Products 🍟"),
            KeyboardButton(text="Orders 🛒")
        ],
        [
            KeyboardButton(text="Statistics 📊"),
            KeyboardButton(text="Send Feedback ⏏️")
        ]
    ], resize_keyboard=True
)
