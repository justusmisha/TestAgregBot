from aiogram import types
from aiogram.dispatcher.filters import Command
from logging import getLogger
from loader import dp


logger = getLogger(__name__)


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    try:

        await message.answer("Write ur data in next message to get answer")

    except Exception as e:
        logger.error(f"An error occurred while handling /start command: %s", e)
