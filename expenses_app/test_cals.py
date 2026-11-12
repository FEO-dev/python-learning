from models import Expense
from cals import total_price

def test_total_price_of_two_item ():
    expenses = [Expense ("Хлеб", 50), Expense ("Молоко", 90)]
    assert total_price(expenses) == 140

def test_total_price_of_emply_list ():
    assert total_price ([]) == 0