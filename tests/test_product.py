from unittest.mock import patch

from src.product import Product


def test_product_init(product):
    assert product.name == "orange"
    assert product.description == "from Egypt"
    assert product.price == 10.0
    assert product.quantity == 5


def test_new_product_update_product():
    existing_product = Product("orange", "from Egypt", 10.0, 5)
    products_list = [existing_product]
    data = {"name": "orange", "description": "from Spain", "price": 15.0, "quantity": 3}
    result = Product.new_product(data, products_list)
    assert existing_product.name == "orange"
    assert existing_product.price == 15.0
    assert existing_product.quantity == 8


def test_new_product_create_new_product():
    products_list = []
    data = {"name": "apple", "description": "from Spain", "price": 7.0, "quantity": 9}
    result = Product.new_product(data, products_list)
    assert result.name == "apple"
    assert result.price == 7.0
    assert result.quantity == 9


def test_product_price_negative(capsys, product):
    product.price = -8.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product.price = 0.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 10.0


def test_product_lower_price_with_agree(product):
    with patch("builtins.input", return_value="y"):
        product.price = 5.0
    assert product.price == 5.0


def test_product_lower_price_no_agree(product):
    with patch("builtins.input", return_value="n"):
        product.price = 5.0
    assert product.price == 10.0


def test_product_upper_price(product):
    product.price = 15.0
    assert product.price == 15.0


def test_product_str(product):
    assert str(product) == "orange, 10.0 руб. Остаток: 5 шт."


def test_product_add(product, product2):
    assert product + product2 == 66