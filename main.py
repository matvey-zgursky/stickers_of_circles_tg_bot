import asyncio
from aiogram import Bot, Dispatcher

from aiogram.filters import CommandStart
from aiogram.types import Message

import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def send_welcome(message: Message) -> None:
    await message.answer(text='Привет! Я бот для создания '
                         'стикеров из кружочков.\nКоманды бота:\n'
                         '/addpack - создать новый пак стикеров\n'
                         '/addpack - добавить стикер в пак\n'
                         '/deletepack - удалить пак\n'
                         '/deletestiker - удалить стикер')

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())