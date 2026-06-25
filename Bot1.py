API_TOKEN = "8870043387:AAFm2SaIEXuPf688m0Vt7D-rXOYgmB_WURE"

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}!\nЯ работаю! Напиши мне что-нибудь."
    )


@dp.message()
async def echo(message: Message):
    if message.from_user.is_bot:
        return
    await message.answer(f"Вы сказали: {message.text}")


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())