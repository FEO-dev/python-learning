# class Task:
#     def __init__(self, text):
#         self.text = text
#         self.done = False

#     def mark_done(self):
#         self.done = True

#     def describe(self):
#         if self.done:
#             mark = "[x]"
#         else:
#             mark = "[ ]"
#         return f"{mark} {self.text}"

# task = Task("купить хлеб")
# print(task.describe())
# task.mark_done()
# print(task.describe())
# tasks = [Task("купить хлеб"), Task("выкинуть мусор"), Task("позвонить маме")]
# tasks[1].mark_done()

# for number, item in enumerate(tasks, 1):
#     print(number, item.describe())



class Expense:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name} - {self.price}"

    def is_expensive(self, limit):
        return self.price > limit


    def show_expenses(expenses):
        for number, expense in enumerate(expenses, 1):
            print(f"{number}. {expense['name']} - {expense['price']}")
            print (total_price (price))

def total_price (expenses):
    total = 0
    for expense in expenses:
        total = total + expense.price
    return total

expenses = [
    Expense("хлеб", 50),
    Expense("молоко", 90),
    Expense("сыр", 300),
    Expense("кофе", 250),
    Expense("яблоки", 120),
]


for number, expense in enumerate(expenses, 1):
    print(f"{number}. {expense.describe()}")
print("Сумма всех:", total_price(expenses))
print(expenses[2].is_expensive(200))
print(expenses[0].is_expensive(200))
print(expenses[0]["price"])