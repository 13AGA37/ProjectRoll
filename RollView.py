class RollView:


    def __init__(self, controller):

        self.controller = controller

    def print_restaurant_menu(self):

        print(self.controller.get_restaurant_menu())

    def print_site_menu(self):

        print(self.controller.get_site_menu())


    def set_ingredients(self, user_rights, new_ingredients):
        if type(new_ingredients) is not list:
            print("Неверный тип данных!!!!")
            return
        set_ingredients_response = self.controller.set_ingredients(user_rights, new_ingredients)
        if set_ingredients_response == 'forbidden':
            print("Нет права доступа!")
        else:
            print(set_ingredients_response)

    def set_price(self, user_rights, new_price):
        try:
            new_float_price = float(new_price)
        except ValueError:
            print("Неверный тип данных!!!!")
            return
        set_price_response = self.controller.set_price(user_rights, new_float_price)
        if set_price_response == 'forbidden':
            print("Нет права доступа!")
        else:
            print(set_price_response)

    def set_weight(self, user_rights, new_weight):
        try:
            new_weight_float = float(new_weight)
        except ValueError:
            print("Неверный тип данных!!!!")
            return
        set_weight_response = self.controller.set_weight(user_rights, new_weight_float)
        if set_weight_response == 'forbidden':
            print("Нет права доступа!")
        else:
            print(set_weight_response)

    def set_picture(self, user_rights, new_picture):
        set_picture_response = self.controller.set_picture(user_rights, new_picture)
        if set_picture_response == 'forbidden':
            print("Нет права доступа!")
        else:
            print(set_picture_response)

    def save_order_to_json(self, order):

        print(self.controller.save_order_to_json(order))

    def get_data_from_json(self, user_rights, filename):

        get_data_from_json_response = self.controller.get_data_from_json(user_rights, filename)
        if get_data_from_json_response == 'forbidden':
            print("Нет права доступа!")
        else:
            print(get_data_from_json_response)