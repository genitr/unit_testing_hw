"""Программа проверяет логин и пароль пользователя"""


def check_auth(login: str, password: str):

    if login == "admin" and password == "password":
        result = 'Добро пожаловать'
    elif login == '' or password == '':
        result = 'Все поля должны быть заполнены'
    else:
        result = 'Доступ ограничен'

    return result
