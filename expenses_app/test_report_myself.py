from models import Expense
from report import most_expensive


def test_most_expensive_normal():
    bread = Expense("хлеб", 50)
    cheese = Expense("сыр", 300)
    coffee = Expense("кофе", 250)
    expenses = [bread, cheese, coffee]
    assert most_expensive(expenses) is cheese


def test_most_expensive_empty():
    assert most_expensive([]) is None


def test_most_expensive_single():
    bread = Expense("хлеб", 50)
    assert most_expensive([bread]) is bread


def test_most_expensive_first():
    cheese = Expense("сыр", 300)
    bread = Expense("хлеб", 50)
    milk = Expense("молоко", 90)
    assert most_expensive([cheese, bread, milk]) is cheese


def test_most_expensive_last():
    bread = Expense("хлеб", 50)
    milk = Expense("молоко", 90)
    cheese = Expense("сыр", 300)
    assert most_expensive([bread, milk, cheese]) is cheese