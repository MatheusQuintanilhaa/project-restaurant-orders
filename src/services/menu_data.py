from models.dish import Dish
from models.ingredient import Ingredient
import sys
import csv


def read_menu_file(source_path):
    try:
        if not source_path.endswith(".csv"):
            raise ValueError("Invalid source file format")

        with open(source_path, encoding="utf-8", mode="r") as file:
            file_data = csv.DictReader(file, delimiter=",", quotechar='"')
            return [row for row in file_data]

    except FileNotFoundError:
        print(f"File {source_path} not found", file=sys.stderr)

    except ValueError as error:
        print(error, file=sys.stderr)


class MenuData:
    @staticmethod
    def __add_ingredient(dish_data, dish_instance):
        ingredient = Ingredient(dish_data["ingredient"])
        amount = int(dish_data["recipe_amount"])
        dish_instance.add_ingredient_dependency(ingredient, amount)

    def __create_dishes(self, menu_file_data):
        dishes_instances = dict()

        for row in menu_file_data:
            name = row["dish"]

            if name in dishes_instances:
                self.__add_ingredient(row, dishes_instances[name])
            else:
                price = float(row["price"])
                dishes_instances[name] = Dish(name, price)
                self.__add_ingredient(row, dishes_instances[name])

        return dishes_instances

    def set_dishes(self, source_path):
        menu_file_data = read_menu_file(source_path)
        dishes_instances = self.__create_dishes(menu_file_data)
        self.dishes = set(dish for dish in dishes_instances.values())

    def __init__(self, source_path: str) -> None:
        self.set_dishes(source_path)
