"""Тесты для модуля shipping"""

import pytest

from src.python_base.shipping import get_cost


@pytest.mark.parametrize(
    'cost, expected',
    (
        (10, 'Стоимость доставки: 200 руб.'),
        (5, 'Стоимость доставки: 200 руб.'),
        (0, 'Стоимость доставки: 200 руб.')
    )
)
def test_cost_less_or_equals_10(cost, expected):
    result = get_cost(cost)
    assert result == expected


@pytest.mark.parametrize(
    'cost, expected',
    (
        (11, 'Стоимость доставки: 500 руб.'),
        (20, 'Стоимость доставки: 500 руб.'),
        (25, 'Стоимость доставки: 500 руб.')
    )
)
def test_cost_mor_than_10(cost, expected):
    result = get_cost(cost)
    assert result == expected