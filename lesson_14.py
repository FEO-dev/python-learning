# numbers = [10, 20, 30, 40, 50]

# # print(numbers[-2:])
# # print(numbers[-0:])

# def last_items (items, n):
#     if n < 1:
#         return []
#     return items [-n:]

# print(last_items(numbers, 2))
# print(last_items(numbers, 0))
# print(last_items(numbers, 10))

# total = 0
# for number in numbers:
#     total = total + number
#     print ("Добавили", number, "в копилке", total)

# print ("Итого", total)

expenses = [
    {"name": "хлеб", "price": 50},
    {"name": "молоко", "price": 90},
    {"name": "сыр", "price": 300},
    {"name": "кофе", "price": 250},
    {"name": "яблоки", "price": 120},
]
numbers = [10, 20, 30]
def last_expenses(expenses, n):
    if n < 1:
        return []
    return expenses [-n:]

def total_price (expenses):
    total = 0
    for expense in expenses:
        total = total + expense["price"]
    return total

def show_expenses(expenses):
    for number, expense in enumerate(expenses, 1):
        print(f"{number}. {expense['name']} - {expense['price']}")


recent = last_expenses(expenses, 3)
show_expenses(recent)
print("Сумма последних:", total_price(recent))
print("Сумма всех:", total_price(expenses))
print (last_expenses(expenses, 0))
print (last_expenses(expenses, 10))
print (total_price([]))