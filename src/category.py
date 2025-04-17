from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product: Product):
        """Добавление нового продукта в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Свойство для получения списка продуктов, по нужному шаблону."""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_list(self):
        return self.__products


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#     # product4 = Product("Samsung Galaxy U23 Ultra", "256GB, Серый цвет, 200MP камера", 200000.0, 5)
#
#     print(str(product1))
#     print(str(product2))
#     print(str(product3))
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(str(category1))
#
#     print(category1.products)
#
#     print(product1 + product2)
#     print(product1 + product3)
#     print(product2 + product3)
