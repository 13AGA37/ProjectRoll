import os
from models.RollModel import RollModel
from controllers.RollController import RollController
from views.RollView import RollView

if __name__ == "__main__":
    image_path = os.path.abspath('images/RollFiladelfia.jpg.')
    my_model = RollModel(
        name='Филадельфия',
        ingredients=["рис", "нори", "лосось", "авокадо", "сыр филадельфия", "огурец"],
        price=400,
        weight=240,
        picture=image_path,
        client_ingredients=['+соевый соус', '+палочки', '+имбирь', '+вассаби' ]
    )
    my_controller = RollController(my_model)
    my_view = RollView(my_controller)
    my_view.print_restaurant_menu()
    my_view.print_site_menu()
    # my_view.save_order_to_json("Филадельфия_+")
    my_view.get_data_from_json('Admin', r'orders\1728397109.96_Филадельфия_Стандарт_Стандарт')
    print()
    my_view.set_ingredients('user', ["рис", "нори", "лосось", "авокадо", "сыр филадельфия", "огурец"])
    my_view.set_ingredients('Admin', ("рис", "нори", "лосось", "авокадо", "сыр филадельфия", "огурец"))
    my_view.set_ingredients('Admin', ["рис", "нори", "лосось", "авокадо", "сыр филадельфия", "огурец"])
    print()
    my_view.set_price('user', "400")
    my_view.set_price('Admin', "четыреста")
    my_view.set_price('Admin', "400")
    print()
    my_view.set_weight('user', "250")
    my_view.set_weight('Admin', "двести пятьдесят")
    my_view.set_weight('Admin', "250")
    print()
    my_view.print_restaurant_menu()