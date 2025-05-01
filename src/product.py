from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity: int = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError

    @classmethod
    def new_product(cls, data, products_list):
        """Класс-метод для обработки/создания нового продукта.
        Если продукт с указанным именем уже есть в products_list, обновляем его quantity и price.
        Если продукта с данным именем нет, создаем новый объект Product и возвращаем его.
        """

        for product in products_list:
            if product.name == data.get(
                "name"
            ):  # Проверяю существование продукта по имени
                product.quantity += data.get("quantity")  # Добавляю количество
                product.price = data.get(
                    "price"
                )  # Меняю цену в соответствии с логикой проверки через сеттер
        else:
            # Если продукта с таким именем нет, создаю новый
            name = data.get("name")
            description = data.get("description")
            price = data.get("price")
            quantity = data.get("quantity")
            return Product(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_des = input(
                'Цена товара указана ниже существующей.\nХотите снизить цену? Введите "Да/Нет" или "Y/N"\n'
            )
            if user_des.lower() in ["да", "y", "d"]:
                self.__price = new_price
        else:
            self.__price = new_price
