class Expense:
    def __init__ (self, name, price):
        self.name = name
        self.price = price

    def describe (self):
        return f"{self.name} - {self.price}"

    def is_expensive(self, limit):
        return self.price > limit