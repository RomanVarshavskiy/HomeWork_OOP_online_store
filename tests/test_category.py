import pytest


def test_category_init(category_1, category_2):
    assert category_1.name == "Vegetables"
    assert category_1.description == "Useful vegetables"
    assert len(category_1.products_list) == 3

    assert category_1.category_count == 2
    assert category_2.category_count == 2
    assert category_1.product_count == 5
    assert category_2.product_count == 5


def test_category_products_property(category_1):
    assert category_1.products == (
        "огурцы, 5.5 руб. Остаток: 3 шт.\n"
        "помидоры, 10.0 руб. Остаток: 4 шт.\n"
        "лук, 3.4 руб. Остаток: 5 шт.\n"
    )


def test_category_add_products(category_1, product):
    assert len(category_1.products_list) == 3
    # category_1.add_product(Product("капуста", "пекинская", 3.0, 2))
    category_1.add_product(product)
    assert len(category_1.products_list) == 4


def test_category_str(category_1):
    assert str(category_1) == "Vegetables, количество продуктов: 12 шт."


def test_category_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "orange"
    assert next(product_iterator).name == "melon"

    with pytest.raises(StopIteration):
        next(product_iterator)
