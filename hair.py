#DAY-37
# object = a bundle of related attributes (variables) and methods (functions)
# a "class" is required to create many objects

# class = blueprint used to design the structure and layout of an object

class Hair:
    def __init__(self, source, type, color, in_stock):
        self.source = source
        self.type = type
        self.color = color
        self.in_stock = in_stock

    def buy(self):
        print(f"You bought the {self.color} {self.type}")

    def sell(self):
        print(f"You sold the {self.color} {self.type}")

    def describe(self):
        print(f"{self.type} {self.source} {self.color}")

