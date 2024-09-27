from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🛍 Оформить заказ')],
        [KeyboardButton(text='🎉 Акция'), KeyboardButton(text='🏘 Все филиалы')],
        [KeyboardButton(text='💼 Вакансии'), KeyboardButton(text="ℹ️ О нас")],
    ],
    resize_keyboard=True
)

