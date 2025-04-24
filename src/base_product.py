from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов,
    представляющий общую функциональность."""


    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод сложения количества продуктов одного типа"""
        pass
