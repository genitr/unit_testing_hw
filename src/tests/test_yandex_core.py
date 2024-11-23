"""Тесты для модуля yandex_core"""

import pytest
import requests

from src.yandex_api.yandex_core import YD
from src.config import DISC_TOKEN


@pytest.mark.parametrize(
    'token, method, param, folder_name, status_code',
    (
        (DISC_TOKEN, 'resources', 'path', 'new_folder', 201),
        (DISC_TOKEN, 'resources', print(), 'new_folder', 400),
        ('DISC_TOKEN', 'resources', 'path', 'new_folder', 401),
        (DISC_TOKEN, 'resource', 'path', 'new_folder', 404),
        (DISC_TOKEN, 'resources', 'path', 'new_folder', 409)
    )
)
def test_create_folder(token, method, param, folder_name, status_code):
    yd = YD(token)
    result = yd.create_folder(folder_name=folder_name, method=method, param=param)
    assert result == status_code

