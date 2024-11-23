"""Модуль конфигурации"""

import os

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


DISC_TOKEN = os.getenv('YANDEX_DISC_TOKEN')
DISC_URL = os.getenv('YANDEX_DISC_URL')
CREATE_FOLDER = f'{DISC_URL}resources'
