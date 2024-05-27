from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from utils.data_calculator.data_analyzer import DataCalculator


@dp.message_handler(lambda message: message.text.startswith('{'))
async def start(message: types.Message):
    try:
        dc = DataCalculator(data=message.text)
        await message.answer(text=await dc.data_calculation())

    except Exception as e:
        print(f"An error occurred while handling /start command: {e}")
