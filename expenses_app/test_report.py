from models import Expense
from report import most_expensive, expensive_only


def make_expenses():
    return [
        Expense("хлеб", 50),
        Expense("молоко", 90),
        Expense("сыр", 300),
        Expense("кофе", 250),
        Expense("яблоки", 120),
    ]


def test_most_expensive_is_cheese():
    best = most_expensive(make_expenses())
    assert best.name == "сыр"


def test_most_expensive_of_empty_list():
    assert most_expensive([]) is None


def test_expensive_only_over_200():
    result = expensive_only(make_expenses(), 200)
    names = []
    for expense in result:
        names.append(expense.name)
    assert names == ["сыр", "кофе"]

def names_of(expenses):
    names = []
    for expense in expenses:
        names.append(expense.name)
    return names


def test_expensive_only_typical_limit():
    result = expensive_only(make_expenses(), 200)
    assert names_of(result) == ["сыр", "кофе"]


def test_expensive_only_nothing_matches():
    result = expensive_only(make_expenses(), 1000)
    assert result == []


def test_expensive_only_everything_matches():
    result = expensive_only(make_expenses(), 0)
    assert len(result) == 5


def test_expensive_only_price_equals_limit():
    result = expensive_only(make_expenses(), 250)
    assert names_of(result) == ["сыр"]


def test_expensive_only_empty_list():
    result = expensive_only([], 200)
    assert result == []