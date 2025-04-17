import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


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
def product():
    return Product("orange", "from Egypt", 10.0, 5)


@pytest.fixture
def product2():
    return Product("apple", "from Poland", 4.0, 4)


@pytest.fixture
def product_iterator(category_2):
    return ProductIterator(category_2)
