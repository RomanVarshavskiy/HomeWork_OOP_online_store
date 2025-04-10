import pytest

from src.category import Category
from src.product import Product


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
            Product("orange", "from Egypt", 6.5, 5),
            Product("melon", "from Turkey", 8.8, 6),
        ],
    )


@pytest.fixture
def product():
    return Product("orange", "from Egypt", 6.5, 5)
