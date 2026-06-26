API_TOKEN = "8870043387:AAFm2SaIEXuPf688m0Vt7D-rXOYgmB_WURE"

import asyncio
import logging
from threading import Thread
from flask import Flask
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = "ТВОЙ_ТОКЕН_БОТА"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- Веб-сервер для Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return "OK"

def run_web():
    app.run(host='0.0.0.0', port=10000)
# -------------------------------


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Бот работает 24/7.")


@dp.message()
async def echo(message: Message):
    if message.from_user.is_bot or not message.text:
        return
    await message.answer(f"Вы сказали: {message.text}")


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    Thread(target=run_web).start()
    asyncio.run(main())


