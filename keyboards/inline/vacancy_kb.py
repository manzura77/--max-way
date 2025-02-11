from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


kurer_menu = InlineKeyboardBuilder(
    markup = [
        [InlineKeyboardButton (text='Подать заявку',callback_data='kuryer')]
    ]
).as_markup()

operator_menu = InlineKeyboardBuilder(
    markup = [
        [InlineKeyboardButton(text='Подать заявку', callback_data='operator')]
    ]
).as_markup()

tozalik_xodimi_menu = InlineKeyboardBuilder(
    markup = [
        [InlineKeyboardButton(text='Подать заявку', callback_data='tozalik_xodimi')]
    ]
).as_markup()


ranner_menu = InlineKeyboardBuilder(
    markup = [
        [InlineKeyboardButton(text='Подать заявку',callback_data='ranner')]
    ]
).as_markup()

qadoqlovchi_menu = InlineKeyboardBuilder(
    markup = [
        [InlineKeyboardButton(text='Подать заявку',callback_data='qadoqlovchi')]
    ]
).as_markup()

kassir_menu = InlineKeyboardBuilder(
    markup = [
        [InlineKeyboardButton(text='Заполнение заявки', callback_data='kassir')]
    ]
).as_markup()

oshpaz_menu = InlineKeyboardBuilder(
    markup = [
        [InlineKeyboardButton(text='Подать заявку', callback_data='oshpaz')]
    ]
).as_markup()