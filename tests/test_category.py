def test_category_init(category_1, category_2):
    assert category_1.name == "Vegetables"
    assert category_1.description == "Useful vegetables"
    assert len(category_1.products) == 3

    assert category_1.category_count == 2
    assert category_2.category_count == 2
    assert category_1.product_count == 5
    assert category_2.product_count == 5
