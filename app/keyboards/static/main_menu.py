from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


simple_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Hello!")],
    ],
    resize_keyboard=True,
)
