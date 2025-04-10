import json

from config import PATH_TO_DATA
from src.product import Product
from src.category import Category

def read_json(filename: str) -> dict:
    """Функция для считывания данных из json"""
    with open(PATH_TO_DATA / filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

def create_objects_from_json(data: dict):
    """Создает объекты классов из данных json"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories

# if __name__ == '__main__':
#     raw_data = read_json("products.json")
#     categories_data = create_objects_from_json(raw_data)
#     print(raw_data)
#     print(categories_data)
#     print(categories_data[0].name)
#     print(categories_data[0].products)
#     print(categories_data[1].name)
#     print(categories_data[1].products)
