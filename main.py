import logging
from config.config import get_config
from aiogram import Bot, Dispatcher, executor
from handlers import handlers


def init():
    cfg = get_config()
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=cfg.get('BOT_TOKEN'))
    dp = Dispatcher(bot)
    handlers.register(dp)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    init()
