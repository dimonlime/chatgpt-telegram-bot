from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def simple_buttons():
    buttons = ["button1", "button2", "button3"]
    keyboard = InlineKeyboardBuilder()
    for button in buttons:
        keyboard.add(
            InlineKeyboardButton(text=button, callback_data=f"simple_{button}")
        )
    return keyboard.adjust(3).as_markup()
