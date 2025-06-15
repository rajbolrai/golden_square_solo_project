from lib.menu import *
from lib.food import *

"""
add food to menu
return all food
"""
def test_given_foods_return_list_of_all_food():
    pizza_food = Food("Pizza", 11.50)
    menu = Menu()
    menu.add(pizza_food)
    assert menu.see_all() == [pizza_food]