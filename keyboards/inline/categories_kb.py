from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db


def make_categories_inline():
    menu = InlineKeyboardMarkup(inline_keyboard=[])
    inline_buttons = []
    categories = db.get_categories_for_admin()

    for category in categories:
        category_id, name = category
        button = InlineKeyboardButton(text=name, callback_data=str(category_id))
        inline_buttons.append(button)
    
    menu.inline_keyboard.append(inline_buttons)

    return menu