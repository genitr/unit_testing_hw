"""Тесты для модуля seasons"""

import pytest

from src.python_base.seasons import check_month


@pytest.mark.parametrize(
    'month_index, expected',
    (
        (1, 'Зима'),
        (5, 'Весна'),
        (6, 'Лето'),
        (9, 'Осень'),
        (0, 'Некорректный номер месяца'),
        (13, 'Некорректный номер месяца')
    )
)
def test_correct_seasons_index(month_index, expected):
    result = check_month(month_index)
    assert result == expected