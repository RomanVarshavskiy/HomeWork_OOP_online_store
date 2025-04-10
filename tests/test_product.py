def test_product_init(product):
    assert product.name == "orange"
    assert product.description == "from Egypt"
    assert product.price == 6.5
    assert product.quantity == 5
