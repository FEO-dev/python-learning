# numbers = [10, 20, 30, 40, 50, 60]

# print(numbers[0])
# print(numbers[5])
# print(numbers[-1])
# print(numbers[-2])

# numbers = [10, 20, 30, 40, 50, 60]

# print(numbers[1:4])
# print(numbers[2:])
# print(numbers[:2])
# print(numbers[-3:])
# print(numbers[1:])

# numbers = [10, 20, 30, 40, 50, 60]

# first = numbers[0]
# rest = numbers[1:]
# print(first)
# print(rest)

# last_two = rest[-2:]
# print(last_two)

# result = [first] + last_two
# print(result)

# def keep_last(items, limit):
#     first = items[0]
#     rest = items[1:]
#     trimmed = rest[-limit:]
#     return [first] + trimmed

# numbers = [10, 20, 30, 40, 50, 60]
# print(keep_last(numbers, 2))
# print(keep_last(numbers, 4))
# print(keep_last(numbers, 10))

def trim_history(messages, limit):
    system = messages[0]
    rest = messages[1:]
    trimmed = rest[-limit:]
    return [system] + trimmed

test = [
    {"role": "system", "content": "инструкция"},
    {"role": "user", "content": "1"},
    {"role": "assistant", "content": "2"},
    {"role": "user", "content": "3"},
    {"role": "assistant", "content": "4"},
    {"role": "user", "content": "5"},
]

result = trim_history(test, 10)
for item in result:
    print(item["role"], item["content"])