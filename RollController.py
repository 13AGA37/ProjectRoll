import os


class RollController:


    def __init__(self, model):

        self.model = model

    def get_restaurant_menu(self):

        roll_data = (f'Ролл :: {self.model.get_name()}\n'
                      f'Цена :: {self.model.get_price()}\n'
                      f'Вес :: {self.model.get_weight()}\n'
                      f'Состав :: {", ".join(self.model.get_ingredients())}\n')
        return roll_data

    def get_site_menu(self):

        roll_data = (f'Ролл :: {self.model.get_name()}\n'
                      f'Цена :: {self.model.get_price()}\n'
                      f'Вес :: {self.model.get_weight()}\n'
                      f'Состав :: {", ".join(self.model.get_ingredients())}\n'
                      f'Фото ::{os.startfile(self.model.get_picture())}')
        return roll_data

    def set_ingredients(self, user_rights, new_ingredients):
        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']:
            self.model.set_ingredients(new_ingredients)
            return "Рецепт изменен!"
        else:
            return "forbidden"

    def set_price(self, user_rights, new_float_price):
        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']:
            self.model.set_price(new_float_price)
            return "Цена изменена"
        else:
            return "forbidden"

    def set_weight(self, user_rights, new_weight_float):
        # try:
        #     new_weight_float = float(new_weight_float)
        # except ValueError:
        #     return "Неверный тип данных!!!!"
        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']:
            self.model.set_weight(new_weight_float)
            return "Вес изменен"
        else:
            return "forbidden"

    def set_picture(self, user_rights, new_picture):
        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']:
            self.model.set_picture(new_picture)
            return "Изображение изменено"
        else:
            return 'forbidden'

    def save_order_to_json(self, order):

        return self.model.save_order_to_json(order)

    def get_data_from_json(self, user_rights, filename):

        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']:
            return self.model.get_data_from_json(filename)
        else:
            return 'forbidden'