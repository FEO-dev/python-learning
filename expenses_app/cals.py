def total_price (expenses):
    total = 0
    for expense in expenses:
        total = total + expense.price
        # return f"{self.name} - {self.price}"
    return total