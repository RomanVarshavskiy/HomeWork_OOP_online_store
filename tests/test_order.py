import pytest

from src.order import Order


def test_order_init(order1):
    assert order1.name == "Заказ 1"
    assert order1.description == "Описание заказа 1"
    assert order1.quantity == 2
    assert order1.total_price == 20.0


def test_order_error_quantity(product):
    with pytest.raises(ValueError, match="Недостаточно товара на складе."):
        Order("Заказ 1", "Описание заказа 1", product, 10)


def test_order_str(order1):
    assert str(order1) == (
        "Заказ: Заказ 1\n"
        "Описание: Описание заказа 1\n"
        "Товар: orange\n"
        "Количество: 2\n"
        "Общая стоимость: 20.0 руб."
    )
