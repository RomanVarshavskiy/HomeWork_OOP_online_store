from src.base_goods import BaseGoods
from src.exceptions import ZeroProductCategoryOrder
from src.product import Product


class Category(BaseGoods):
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        super().__init__(name, description)
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        products_quantity = 0
        for product in self.__products:
            products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {products_quantity} шт."

    def add_product(self, product: Product):
        """Добавление нового продукта в категорию."""
        if isinstance(product, Product) or issubclass(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProductCategoryOrder("Товар с нулевым количеством не может быть добавлен")
            except ZeroProductCategoryOrder as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Продукт добавлен успешно")
            finally:
                print("Обработка добавления продукта завершена")
        else:
            raise TypeError("Передан неверный тип данных. Ожидался Product или его подкласс.")



    @property
    def products(self):
        """Свойство для получения списка продуктов, по нужному шаблону."""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_list(self):
        """Геттер для получения списка продуктов."""
        return self.__products

    def middle_price(self):
        """Метод для получения средней цены продуктов в категории."""
        try:
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())