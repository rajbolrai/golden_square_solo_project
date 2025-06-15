class Menu:
    # User-facing properties:
    #   foods: list of instances of Food
    def __init__(self):
        self.foods = []

    def add(self, food):
        # Parameters:
        #   food: an instance of Food
        # Side-effects:
        #   Adds the food to the foods property of the self object
        self.foods.append(food)

    def search_by_title(self, food_name):
        # Parameters:
        #   food_name: string
        # Returns:
        #   Food instance that has the same name
        for i in self.foods:
            if i.food_title == food_name:
                return i
        return "No food found"

    def see_all(self):
        #return:
        #   a dictioinary of all the food and their price
        return self.foods