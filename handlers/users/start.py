from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    try:

        await message.answer("Write ur data in next message to get answer")

    except Exception as e:
        print(f"An error occurred while handling /start command: {e}")
