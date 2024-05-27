from handlers import dp
from aiogram.utils import executor
from loader import logger


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    logger.info("service start")
