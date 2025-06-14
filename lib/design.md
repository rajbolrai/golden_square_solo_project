## 1. User Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## 2. Design the Class System

```python
class Menu:
    # User-facing properties:
    #   foods: list of instances of Food

    def __init__(self):
        pass # No code here yet

    def add(self, food):
        # Parameters:
        #   food: an instance of Food
        # Side-effects:
        #   Adds the food to the foods property of the self object
        pass # No code here yet

    def search_by_title(self, food_name):
        # Parameters:
        #   food_name: string
        # Returns:
        #   Food instance that has the same name
        pass # No code here yet

    def see_all(self):
        #return:
        #   a dictioinary of all the food and their price
        pass


class Food:
    # User-facing properties:
    #   title: string 
    #   price: float

    def __init__(self, title, price):
        # Parameters:
        #   title: string
        #   price: float
        # Side-effects:
        #   Sets the title and price properties
        pass # No code here yet

class Order:
    # User-facing properties:
    #   menu: Menu instance
    #   current_order: list of food instances
    def __init__(self, menu):
        # Parameters:
        #   menu: Menu instance
        #   order: emtpy list
        # Side-effects:
        #   Sets the menu and current_order properties
        pass # No code here yet

    def select_food(self, food):
        # Parameter:
        #   food: string
        # side-effects:
        #   finds food instance with given food name from menu and adds to current_order 
        pass

    def pay_for_food(self):
        # side-effects:
        #   create orderconfirmation class, pass requests module in and get receipt of food
        # Return:
        #   itemised receipt of order, in form of string with total in the end
        pass

    
class OrderConfirmation:
    # User-facing properties:
    #   order: list of Food instances
    #   request: instance of request module
    def __init__(self, order, request):
        # Parameters:
        #   order: Menu instance
        #   request: request module
        # Side-effects:
        #   Sets the order and request properties
        pass # No code here yet

    def confirm(self):
        # request to twilio api to send message
        #return:
        #   text message to user mobile phone 
        pass

    def generate_receipt(self):
        #return:
        #   itemised receipt of order, in form of string with total in the end
        pass

```

## 3. Create Examples as Integration Tests

```python

"""
Given a menu
When we add two food
In order go through the menu and select the second food item
after paying for it
we will see the food reciept
"""
menu = Menu()
food_1 = Food("Burger", 8.50)
food_2 = Track("Pizza", 11.50)
menu.add(food_1)
menu.add(food_2)
order = Order(menu)
order.select_food("Pizza")
assert order.pay_for_food()# => "Items: Pizza: 11.50 -- total: £11.50"
```


