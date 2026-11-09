def show_tasks(tasks):
    for i in range(len(tasks)):
        print(i + 1, tasks[i])

def save_tasks(tasks):
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write( task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
            return lines
    except FileNotFoundError:
        return []

    
def add_task(tasks):
    new_task = input ('Введите задачу    ')
    tasks.append(new_task)
    save_tasks(tasks)

def delete_task(tasks):
    try:
        del_task = int (input ('Введите номер задачи которую надо удалить    '))
        if del_task < 1:
            print("Номер должен быть не меньше 1")
            return
        tasks.pop(del_task - 1)
        save_tasks(tasks)
    except ValueError:
        print("Нужно ввести целое число")
    except IndexError:
        print("Такого номера нет в списке задач")

tasks = load_tasks()
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

# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("первая строка\n")
#     file.write("вторая строка\n")

# with open("test.txt", "r", encoding="utf-8") as file:
#     lines = file.read().splitlines()

# print(lines)

# try:
#     with open("nofile.txt", "r", encoding="utf-8") as file:
#         lines = file.read().splitlines()
# except FileNotFoundError:
#     lines = []

# print(lines)