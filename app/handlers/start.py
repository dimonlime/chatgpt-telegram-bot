from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from app.keyboards.dynamic.simple_buttons import simple_buttons
from app.keyboards.static.main_menu import simple_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Hi, {message.from_user.first_name}, it will be chatgpt bot soon...",
        reply_markup=await simple_buttons(),
    )


@router.message(F.text == "Hello!")
async def main_keyboard(message: Message):
    await message.answer(
        f"Don`t press this button again...\n"
        f"Name: {message.from_user.first_name}\n"
        f"Id: {message.from_user.id}\n"
        f"Username: {message.from_user.username}\n"
    )


@router.callback_query(F.data.startswith("simple_button"))
async def main_keyboard(callback: CallbackQuery):
    button_number = str(callback.data)[13:]
    await callback.answer("buttton is working)")
    await callback.message.answer(
        f"You pressed button {button_number}", reply_markup=simple_keyboard
    )
