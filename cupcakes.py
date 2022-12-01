from abc import ABC, abstractmethod
import csv
from pprint import pprint

class Cupcake(ABC):
    type = "regular"
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
    type = "mini"
    def __init__(self, name, price, cake, frosting):
        self.name = name
        self.price = price
        self.cake = cake
        self.frosting = frosting
        self.sprinkles = []
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

class Mega(Cupcake):
    type = "mega"
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

class GlutenFree(Cupcake):
    type = "gluten free"
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

# ////////////////////////////////////////////////

# ////////////////////////////////////////////////

cupcake1 = Mini("Cinnamon Sugar", .99, "vanilla", "cinnamon-sugar")
cupcake2 = Mega("Lemon", 2.99, "vanilla", True, "lemon")
cupcake2.add_sprinkles("lemon heads")
cupcake3 = Mega("Red Velvet", 2.99, "red velvet", True, "cream cheese")
cupcake4 = GlutenFree("Chocolate", 2.99, "chocolate", False, "chocolate")
cupcake4.add_sprinkles("chocolate shavings")

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3,
    cupcake4
]

# ////////////////////////////////////////////////

# ////////////////////////////////////////////////

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

read_csv("sample.csv")

def write_csv(file, cupcake_list):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames= ["type", "name", "cake", "price", "filling", "frosting", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcake_list:
            if hasattr(cupcake, "filling"):
                writer.writerow({"type": cupcake.type, "name": cupcake.name, "cake": cupcake.cake, "price": cupcake.price, "filling": cupcake.filling, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"type": cupcake.type, "name": cupcake.name, "cake": cupcake.cake, "price": cupcake.price, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

# write_csv("sample.csv", cupcake_list)