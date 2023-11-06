from abc import ABC, abstructmethod
class Sale_item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstructmethod
    def calculate_cost(self):
        pass

class Food(Sale_item, ABC):
    def __init__(self, name, price):
        super().__init__(name, price)
    @abstructmethod

    def calculate_cost(self):
        pass

class Book(Sale_item):
    def __init__(self, name, price, amount, discount):
        super().__init__(name, price)
        self.amount = amount
        self.discount = discount
    def calculate_cost(self):
        return self.price * (self.amount * ((100 - self.discount)/ 100))
    
class Appliance(Sale_item):
    def __init__(self, name, price, amount, vat):
        super().__init__(name, price)
        self.amount = amount
        self.vat = vat

    def calculate_cost(self):
        return self.price * (self.amount * ((100 + self.vat)/100))
    
class Itemized_food(Food):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    def calculate_cost(self):
        return self.price * self.amount
    
class Measured_food(Food):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def calculate_cost(self):
        return self.price * self.weight
    
vegetable = Itemized_food("Vegetable", 40, 2)
mango = Measured_food("Mango", 70, 1,8)
book = Book("Python book", 200, 1)
cooker = Appliance("Rice Cooker", 1200, 1)

purchased = [vegetable, mango, book, cooker]

for item in purchased:
    print(item.name, item.calculate_cost())