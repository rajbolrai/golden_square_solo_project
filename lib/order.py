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
