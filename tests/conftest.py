import pytest

from src.category import Category
from src.order import Order
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone_lawngrass_product import LawnGrass, Smartphone


@pytest.fixture
def category_1():
    return Category(
        name="Vegetables",
        description="Useful vegetables",
        products=[
            Product("огурцы", "огурцы для салата", 5.5, 3),
            Product("помидоры", "помидоры для салата", 10.0, 4),
            Product("лук", "лук для салата", 3.4, 5),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="Fruits",
        description="Sweet fruits",
        products=[
            Product("orange", "from Egypt", 10.0, 5),
            Product("melon", "from Turkey", 8.8, 6),
        ],
    )


@pytest.fixture
def category_empty_product():
    return Category(
        name="Fruits",
        description="from Spain",
        )


@pytest.fixture
def product():
    return Product("orange", "from Egypt", 10.0, 5)


@pytest.fixture
def product2():
    return Product("apple", "from Poland", 4.0, 4)


@pytest.fixture
def product_iterator(category_2):
    return ProductIterator(category_2)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def smartphone2():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def grass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def grass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )


@pytest.fixture
def order1(product):
    return Order("Заказ 1", "Описание заказа 1", product, 2)
