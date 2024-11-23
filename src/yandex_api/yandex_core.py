"""Модуль содержит класс и функции для работы с Яндекс.Диск"""

import requests

from src.config import DISC_URL


class YD:
    """ Класс для работы с API Яндекс.Диска """

    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {'Authorization': 'OAuth ' + self.access_token}

    def create_folder(self, folder_name, method='resources', param='path'):
        """ Создание новой папки на Яндекс.Диск """

        params = {param: folder_name}

        response = requests.put(f'{DISC_URL}{method}', params=params, headers=self.headers)
        return response.status_code

