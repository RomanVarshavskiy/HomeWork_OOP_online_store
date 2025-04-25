from abc import ABC, abstractmethod


class BaseGoods(ABC):
    """Абстрактный класс, содержащий общие свойства для всех сущностей."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod  # pragma: no cover
    def __str__(self):
        pass
