# def say_hello():
#     print("Привет!")
#     print("Рад вас видеть")

# say_hello()
# say_hello()

# def greet(name):
#     print("Привет,", name)

# greet("Влад")
# greet("Анна")
# def add(a, b):
#     return a + b

# result = add(3, 4)
# print(result)
# print(add(10, 5))
# print(add("5", "5"))
def show_tasks(tasks):
    for i in range(len(tasks)):
        print (tasks[i])

def add_task(tasks):
    new_task = input ('Введите задачу    ')
    tasks.append(new_task)

def delete_task(tasks):
    del_task = int (input ('Введите номер задачи которую надо удалить    '))
    tasks.pop(del_task - 1)

tasks = ['купить хлеб', 'купить молоко', 'выкинуть мусор']
while True:
    print('1 - показать задачи', '2 - добавить задачу', '3 - удалить задачу', '4 - выход')
    choice = int(input('Введите № действия'))
    if choice == 1:
        show_tasks(tasks)
    elif choice == 2:
        add_task(tasks)
    elif choice == 3:
        delete_task(tasks)
    elif choice == 4:
        break

    1


    # print('1 - показать задачи', '2 - добавить задачу', '3 - выход')
    # choice = int(input('Введите № действия'))
    # if choice == 1:
    #     for i in range(len(tasks)):
    #          print (tasks[i])
    # elif choice == 2:
    #     new_task = input ('Введите задачу    ')
    #     tasks.append(new_task)
    # elif choice == 3:
    #     break
