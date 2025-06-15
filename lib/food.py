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
        self.food_title = title 
        self.food_price = price
        
    def __repr__(self):
        return f"food: {self.food_title}, cost: {self.food_price}"