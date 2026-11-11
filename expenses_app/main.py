from models import Expense
from cals import total_price
from report import most_expensive
from report import expensive_only 


expenses = [
    Expense("хлеб", 50),
    Expense("молоко", 90),
    Expense("сыр", 300),
    Expense("кофе", 250),
    Expense("яблоки", 120),
]

best = most_expensive(expenses)
print("Самый дорогой:", best.describe())

print("Дороже 200:")
for expense in expensive_only(expenses, 200):
    print(" ", expense.describe())


for number, expense in enumerate(expenses, 1):
    print(f"{number}. {expense.describe()}")

print("Сумма всех:", total_price(expenses))
print("проверяю:", expense.name, expense.price, "лучший сейчас:", best.name)
print(most_expensive([]))