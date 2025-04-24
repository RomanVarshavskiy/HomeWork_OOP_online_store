class PrintMixin:

    # def __init__(self, name="", description="", price=0.0, quantity=0):
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity
    #     print(repr(self))

    def __init__(self):
        print(repr(self))

    def __repr__(self) -> str:

        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
