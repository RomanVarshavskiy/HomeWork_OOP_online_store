import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 13


def test_smartphone_add_error(smartphone1):
    with pytest.raises(TypeError):
        smartphone1 + 10


def test_lawngrass_init(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawngrass_add(grass1, grass2):
    assert grass1 + grass2 == 35


def test_lawngrass_add_error(grass1):
    with pytest.raises(TypeError):
        grass1 + 10
