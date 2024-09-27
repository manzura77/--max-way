from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


for_buyurtma_berish = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚖 Доставка"), KeyboardButton(text='🏃Еда на вынос')],
        [KeyboardButton(text='⬅️ Назад')]
    ],
    resize_keyboard=True
)


barcha_filiallar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='⬅️ Назад'), KeyboardButton(text='▶️ Следующий')],
        [KeyboardButton(text='MAX WAY ALAYSKIY'),KeyboardButton(text='MAX WAY BERUNIY')],
        [KeyboardButton(text='MAX WAY AVIASOZLAR'),KeyboardButton(text='MAX WAY RISOVIY')],
        [KeyboardButton(text='MAX WAY PARUS'),KeyboardButton(text='MAX WAY PARKENT')],
        [KeyboardButton(text='MAX WAY UNIVERSAM'),KeyboardButton(text='MAX WAY ROYSON')],
        [KeyboardButton(text='MAX WAY MUQUMIY'),KeyboardButton(text='MAX WAY GRAND MIR')],
        [KeyboardButton(text='MAX WAY SAYRAM'),KeyboardButton(text='MAX WAY MAKSIM GORKIY')],
        [KeyboardButton(text='MAX WAY SERGELI'),KeyboardButton(text='MAX WAY FONTAN')],
        [KeyboardButton(text='MAX WAY MINOR')]
    ]
)


yetkazib_berish_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Lokatsiya yuborish', request_location=True)],
        [KeyboardButton(text='⬅️ Назад')]
    ]
) 
