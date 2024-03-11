import asyncio
from less3 import config
from aiogram import Bot, Dispatcher
import logging
from handlers import common, carrer_choise, messages


async def main():
    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота
    bot = Bot(token=config.token)

    # Диспечер
    dp = Dispatcher()

    dp.include_router(carrer_choise.router)
    dp.include_router(common.router)
    dp.include_router(messages.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
