def find_max(numbers):
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best

data = [50, 90, 300, 250, 120]
result = find_max(data)
print("Максимум:", result)