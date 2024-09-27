from aiogram.types import Message
from loader import dp
from aiogram import F

from aiogram.fsm.context import FSMContext

from states.level_states import BuyurtmaBerishState, FiliallarState
from keyboards.default.second_level_btns import yetkazib_berish_kb, for_buyurtma_berish
from keyboards.default.start_menu import menu


@dp.message(F.text == '⬅️ Назад', FiliallarState.choose_filial)
async def back_from_choose_branch(message: Message, state: FSMContext):
    text = "Чтобы начать заказ 🛍 Нажмите кнопку «Заказать».\n\nВы также можете увидеть акции и познакомиться с нашими партнерами."
    await message.answer(text, reply_markup=menu)
    await state.clear()


@dp.message(F.text == '⬅️ Назад', BuyurtmaBerishState.yetkazib_berish)
async def back_from_yetkazib_berish(message: Message, state: FSMContext):
    await message.answer('Выберите тип доставки', reply_markup=for_buyurtma_berish)
    await state.clear()


@dp.message(F.text == '⬅️ Назад')
async def back_button_handler(message: Message, state: FSMContext):
    await state.clear()
    text = "Чтобы начать заказ 🛍 Нажмите кнопку «Заказать».\n\nВы также можете увидеть акции и познакомиться с нашими партнерами."
    await message.answer(text, reply_markup=menu)
