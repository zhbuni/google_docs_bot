import logging
from dotenv import load_dotenv
import os
from time import sleep
from get_info import get_info
from aiogram import Bot, Dispatcher, executor, types
from urllib.parse import urljoin


load_dotenv()

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


PROJECT_NAME = os.getenv('PROJECT_NAME', 'aiogram-example')

WEBHOOK_HOST = f'https://{PROJECT_NAME}.herokuapp.com/'
WEBHOOK_URL_PATH = '/webhook/' + TOKEN
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_URL_PATH)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет")


async def display_date():
    while True:
        name = 'Шангараев Владимир Евгеньевич'
        status = get_info(name)
        if status == 'готова':
            await bot.send_message(chat_id=228813251, text=f'Регистрация готова!')
        name = 'Бердников Олег Николаевич'
        status = get_info(name)
        if status == 'готова':
            await bot.send_message(chat_id=447200574, text=f'{name} - {status}')
        sleep(200)


async def on_startup(dp: Dispatcher):
    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)


if __name__ == '__main__':
    dp.loop.create_task(display_date())

    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_URL_PATH,
        on_startup=on_startup,
        skip_updates=True,
        host='0.0.0.0',
        port=int(os.getenv("PORT")),
    )
