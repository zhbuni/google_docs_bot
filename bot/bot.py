import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from bot.settings import (BOT_TOKEN, HEROKU_APP_NAME,
                      WEBHOOK_URL, WEBHOOK_PATH,
                      WEBAPP_HOST, WEBAPP_PORT)
from bot.get_info import get_info
from time import sleep

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    logging.warning(f'Recieved a message from {message.from_user}')
    await bot.send_message(message.chat.id, message.text)


async def on_startup(dp):
    logging.warning(
        'Starting connection. ')
    await bot.set_webhook(WEBHOOK_URL,drop_pending_updates=True)


async def on_shutdown(dp):
    logging.warning('Bye! Shutting down webhook connection')


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


def main():
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
