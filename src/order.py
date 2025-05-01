from src.base_goods import BaseGoods
from src.exceptions import ZeroProductError
from src.product import Product


class Order(BaseGoods):
    """Класс для описания заказа."""

    def __init__(self, name: str, description: str, product: Product, quantity: int):
        super().__init__(name, description)
        if quantity > product.quantity:
            raise ValueError("Недостаточно товара на складе.")
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * quantity

    def __str__(self):
        return (
            f"Заказ: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Товар: {self.product.name}\n"
            f"Количество: {self.quantity}\n"
            f"Общая стоимость: {self.total_price} руб."
        )
