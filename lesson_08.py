import json

def show_tasks(tasks):
    for i in range(len(tasks)):
        task = tasks[i]
        if task["done"]:
            mark = "[x]"
        else:
            mark = "[ ]"
        print(i + 1, mark, task["text"])

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_task(tasks):
    text = input('Введите задачу    ')
    new_task = {"text": text, "done": False}
    tasks.append(new_task)
    save_tasks(tasks)

def delete_task(tasks):
    try:
        del_task = int(input('Введите номер задачи которую надо удалить    '))
        if del_task < 1:
            print("Номер должен быть не меньше 1")
            return
        tasks.pop(del_task - 1)
        save_tasks(tasks)
    except ValueError:
        print("Нужно ввести целое число")
    except IndexError:
        print("Такого номера нет в списке задач")

def mark_done(tasks):
    try:
        number = int(input('Введите номер выполненной задачи    '))
        if number < 1:
            print("Номер должен быть не меньше 1")
            return
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
    except ValueError:
        print("Нужно ввести целое число")
    except IndexError:
        print("Такого номера нет в списке задач")

tasks = load_tasks()
while True:
    try:
        print('1 - показать задачи', '2 - добавить задачу', '3 - удалить задачу', '4 - отметить выполненной', '5 - выход')
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
        mark_done(tasks)
    elif choice == 5:
        break
    else:
        print("Такого пункта нет в меню")