def most_expensive(expenses):
    if len(expenses) == 0:
        return None
    best = expenses[0]
    for expense in expenses:
        if expense.price > best.price:
            best = expense
    return best
        
def expensive_only(expenses, limit):
    result = []
    for expense in expenses:
        if expense.is_expensive(limit):
            result.append(expense)
    return result