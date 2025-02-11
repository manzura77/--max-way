from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message
from loader import dp

from keyboards.default.start_menu import menu


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}!",
        reply_markup=menu)
