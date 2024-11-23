"""
Программа проверяет порядковый номер месяца в году (переменная month)
и выводит сообщение с названием соответствующего сезона года
"""


def check_month(month: int):
    """Проверка порядкового номера месяца """
    if month == 1 or month == 2 or month == 12:
        result = "Зима"
    elif month == 3 or month == 4 or month == 5:
        result = "Весна"
    elif month == 6 or month == 7 or month == 8:
        result = "Лето"
    elif month == 9 or month == 10 or month == 11:
        result = "Осень"
    else:
        result = "Некорректный номер месяца"
    return result

