from abc import ABC, abstractmethod

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, cake, filling, frosting):
        self.name = name
        self.price = price
        self.cake = cake
        self.filling = filling
        self.frosting = frosting
        self.sprinkles = []
 
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod 
    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    specialty = "mini"
    def __init__(self, name, price, cake, frosting):
        self.name = name
        self.price = price
        self.cake = cake
        self.frosting = frosting
        self.sprinkles = []

class GlutenFree(Cupcake):
    specialty = "gluten free"





# ////////////////////////////////////////////////

my_cupcake = Mini("strawberry_vanilla", 2, "vanilla", "strawberry")
print(my_cupcake.price, my_cupcake.cake)