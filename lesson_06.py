# try:
#     number = int(input("Введите число: "))
#     print("Вы ввели", number)
# except ValueError:
#     print("Это не число")

# print("Программа продолжает работу")
# numbers = [10, 20, 30]
# try:
#     index = int(input("Номер элемента: "))
#     print(numbers[index])
# except ValueError:
#     print("Нужно ввести число")
# except IndexError:
#     print("Такого номера нет в списке")


def show_tasks(tasks):
    for i in range(len(tasks)):
        print(i + 1, tasks[i])

def add_task(tasks):
    new_task = input ('Введите задачу    ')
    tasks.append(new_task)

def delete_task(tasks):
    try:
        del_task = int (input ('Введите номер задачи которую надо удалить    '))
        if del_task < 1:
            print("Номер должен быть не меньше 1")
            return
        tasks.pop(del_task - 1)
    except ValueError:
        print("Нужно ввести целое число")
    except IndexError:
        print("Такого номера нет в списке задач")

tasks = ['купить хлеб', 'купить молоко', 'выкинуть мусор']
while True:
    try:
        print('1 - показать задачи', '2 - добавить задачу', '3 - удалить задачу', '4 - выход')
        choice = int(input('Введите № действия'))
    except ValueError:
        print("Нужно ввести число")
        continue
    if choice == 1:
        show_tasks(tasks)
    elif choice == 2:
        add_task(tasks)
    elif choice == 3:
        delete_task(tasks)
    elif choice == 4:
        break