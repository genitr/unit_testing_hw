"""Тесты для модуля authorization"""

import pytest

from src.python_base.authorization import check_auth


def test_incorrect_login_and_password():
    login = 'admnin'
    password = 'pass'
    expected = 'Доступ ограничен'

    assert check_auth(login, password) == expected


def test_incorrect_login():
    login = 'admnin'
    password = 'password'
    expected = 'Доступ ограничен'

    assert check_auth(login, password) == expected


def test_incorrect_password():
    login = 'admin'
    password = 'pass'
    expected = 'Доступ ограничен'

    assert check_auth(login, password) == expected


@pytest.mark.parametrize(
    'login, password, expected',
    (
        ('', '', 'Все поля должны быть заполнены'),
        ('admin', '', 'Все поля должны быть заполнены'),
        ('', 'password', 'Все поля должны быть заполнены')
    )
)
def test_empty_login_and_password(login, password, expected):
    result = check_auth(login, password)
    assert result == expected


def test_success_authorization():
    login = 'admin'
    password = 'password'
    expected = 'Добро пожаловать'

    assert check_auth(login, password) == expected
