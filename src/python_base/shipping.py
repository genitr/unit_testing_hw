"""Программа проверяет вес посылки пользователя в килограммах"""


def get_cost(weight: int):
    if weight <= 10:
        result = 'Стоимость доставки: 200 руб.'
    else:
        result = 'Стоимость доставки: 500 руб.'
    return result
