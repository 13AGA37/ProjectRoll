import json
from json import JSONDecodeError
import time


class RollModel:


    def __init__(self, name: str, ingredients: list, price: float, weight: float, picture,
                 client_ingredients: list = None):

        self.__name = name
        self.__ingredients = ingredients
        self.__price = price
        self.__weight = weight
        self.__picture = picture
        if client_ingredients is not None:
            self.__client_ingredients = client_ingredients
        else:
            self.__client_ingredients = []



    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight

    def get_picture(self):
        return self.__picture

    def get_client_ingredients(self):
        return self.__client_ingredients

    def set_ingredients(self, new_ingredients: list):

        if type(new_ingredients) is list:
            self.__ingredients.clear()
            self.__ingredients.extend(new_ingredients)
        else:
            return "Ошибка неверный тип данных"


    def set_price(self, new_price):
        self.__price = new_price

    def set_weight(self, new_weight):
        self.__weight = new_weight

    def set_picture(self, new_picture):
        self.__picture = new_picture

    def add_client_ingredients(self):

        if self.__client_ingredients:
            self.__ingredients.extend(self.__client_ingredients)

    def make_Roll(self):

        client_ingredients = self.get_client_ingredients()
        all_ingredients = self.get_ingredients()
        price = self.get_price()
        weight = self.get_weight()
        if client_ingredients:
            self.add_client_ingredients()
            all_ingredients = self.get_ingredients()
            price = price + len(client_ingredients) * 100
            weight = weight + len(client_ingredients) * 50
        ordered_Roll = {
            'name': self.get_name(),
            'ingredients': all_ingredients,
            'price': price,
            'weight': weight
        }
        return ordered_roll

    def save_order_to_json(self, order):
        ordered_roll = self.make_roll()
        filename = fr'orders\{round(time.time(), 2)}_{order}.json'
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(ordered_roll, fp, ensure_ascii=False, indent=2)
        return f"Заказ {order} сохранен в файл {filename}"

    @staticmethod
    def get_data_from_json(filename):

        try:
            with open(fr"{filename}.json", 'r', encoding='utf-8') as fp:
                python_data = json.load(fp)
        except FileNotFoundError:
            return "Файл не найден!!!"
        except JSONDecodeError:
            return "Данные повреждены!!!/Неверный формат файла!!!"
        except Exception:
            return "Что-то пошло не так!!!"
        else:
            return python_data

