class Cupcake:
    def __init__(self, name, cake_flavor, filling, frosting_flavor, toppings):
        self.name = name
        self.cake_flavor = cake_flavor
        self.filling = filling
        self.frosting_flavor = frosting_flavor
        self.toppings = toppings
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

double_chocolate = Cupcake("Double Chocolate", "chocolate", False, "chocolate", False)

double_chocolate.add_sprinkles("chocolate")

print(double_chocolate.cake_flavor)