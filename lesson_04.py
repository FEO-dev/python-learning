tasks = ['купить хлеб', 'купить молоко', 'выкинуть мусор']
while True:
    print('1 - показать задачи', '2 - добавить задачу', '3 - выход')
    choice = int(input('Введите № действия'))
    if choice == 1:
        for i in range(len(tasks)):
             print (tasks[i])
    elif choice == 2:
        new_task = input ('Введите задачу    ')
        tasks.append(new_task)
    elif choice == 3:
        break

# tasks = ['1 - показать задачи', '2 - добавить задачу', '3 - выход']
# print(tasks)
# while True:
#     task = int (input ('Введите № задачи  '))
#     for i in range(len(tasks)):
#         if task == 1:
#             print (tasks[i])
#         elif task == 2:
#             new_task = input ('Введите задачу    ')
#             tasks.append(new_task)
#             print(tasks)
#         elif tasks == 3:
#             break





# fruits = ["яблоко", "банан", "груша"]
# print(fruits)
# print(fruits[0])
# print(fruits[2])
# print(len(fruits))
# fruits.append("слива")
# fruits[1] = "апельсин"
# fruits.remove("груша")
# print(fruits)
# person = {"имя": "Влад", "возраст": 30, "город": "Москва"}
# print(person["имя"])
# person["возраст"] = 31
# person["профессия"] = "разработчик"
# person["рост"]
# print(person)
# for fruit in fruits:
#     print("Фрукт:", fruit)

# for key in person:
#     print(key, "->", person[key])
# В цикле while True показывайте меню: 1 - показать задачи, 2 - добавить задачу, 3 - выход.
# Пункт 1 выводит все задачи с номерами (подсказка: for i in range(len(tasks)) и tasks[i]).
# Пункт 2 спрашивает текст и добавляет его через append.
# Пункт 3 завершает цикл через break.