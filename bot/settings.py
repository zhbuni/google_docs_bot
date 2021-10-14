import os
from dotenv import load_dotenv

BOT_TOKEN = '2083748158:AAEsXvpl5mvieEQTshNnyv2rN21tLf9-PUY'

if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

HEROKU_APP_NAME = 'aiogram-example1'


# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))
