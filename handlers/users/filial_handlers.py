from aiogram.types import Message
from loader import dp
from aiogram import F

from states.level_states import FiliallarState

@dp.message(F.text == 'MAX WAY ALAYSKIY',FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY ALAYSKIY \n\n🗺 Адрес:  проспект Амира Темура, 25 \n\n🏢 Ориентир:\n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 03:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.318379, 
        longitude=69.280708
    )

@dp.message(F.text == 'MAX WAY AVIASOZLAR', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY AVIASOZLAR\n\n🗺 Адрес:  улица Авиасозлар, 23 \n\n🏢 Ориентир:  \n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 03:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.290894, 
        longitude=69.342153
    )

@dp.message(F.text == 'MAX WAY RISOVIY', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY ROYSON \n\n🗺 Адрес:  Узбекистан, Ташкент, улица Заркайнар, 2 \n\n🏢 Ориентир:  Ориентир: Цирк \n\n ☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 01:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.322643,
        longitude=69.241973
    )

@dp.message(F.text == 'MAX WAY BERUNIY', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY BERUNIY\n\n🗺 Адрес:  улица Беруни, 47, Ташкент\n\n🏢 Ориентир:  Метро Беруний\n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 23:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.344430,
        longitude=69.205021
    )

@dp.message(F.text == 'MAX WAY PARUS', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY PARUS \n\n🗺 Адрес:  улица Катартал, 60/5 \n\n🏢 Ориентир:  ТЦ Парус\n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 03:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.293536,
        longitude=69.212856
    )

@dp.message(F.text == 'MAX WAY PARKENT', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY PARKENT \n\n🗺 Адрес:  улица Паркент, 30В, Ташкент \n\n🏢 Ориентир:  Паркентский рынок \n\n ☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 03:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.314772,
        longitude=69.325067 
    )

@dp.message(F.text == 'MAX WAY ROYSON', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY ROYSON \n\n🗺 Адрес:  Узбекистан, Ташкент, улица Заркайнар, 2 \n\n🏢 Ориентир:  Ориентир: Цирк \n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 01:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.322643,
        longitude=69.241973 
    )

@dp.message(F.text == 'MAX WAY MUQUMIY', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY MUQUMIY \n\n🗺 Адрес:  улица Чиланзар, Ташкент \n\n🏢 Ориентир:  Ориентир: Чиланзар 1-й квартал \n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 04:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.287875,
        longitude=69.229238
    )

@dp.message(F.text == 'MAX WAY GRAND MIR', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY GRAND MIR \n\n🗺 Адрес:  Узбекистан, Ташкент, улица Шота Руставели, 9А \n\n🏢 Ориентир:  Ориентир: Гостиница Гранд Мир \n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 04:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.295095,
        longitude=69.267970
    )

@dp.message(F.text == 'MAX WAY SAYRAM', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY SAYRAM \n\n🗺 Адрес:  Узбекистан, Ташкент, улица Юнусота \n\n🏢 Ориентир:  Ориентир: Рынок сайрам. \n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 03:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.371941,
        longitude=69.3105 
    )

@dp.message(F.text == 'MAX WAY SERGELI', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY SERGELI\n\n🗺 Адрес:  Узбекистан, Ташкент, Сергелийский район, массив Сергели-VIIIА, 11 \n\n🏢 Ориентир:  Ориентир: Сергели Дехкон Бозори \n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 03:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.226369,
        longitude=69.219899
    )
 
@dp.message(F.text == 'MAX WAY MINOR', FiliallarState.choose_filial)
async def buyurtma_berish(message: Message):
    text = '📍 Филиал:  MAX WAY MINOR\n\n🗺 Адрес:  улица Осиё, 84А, Юнусабадский район, Ташкент \n\n🏢 Ориентир:  бывший кинотеатр Казахстан \n\n☎️ Номер для связи:  +998712005400\n\n🕙 Рабочие часы: 10:00 - 03:00'
    await message.answer(text)
    await message.answer_location(
        latitude=41.328054,
        longitude=69.282584
    )
