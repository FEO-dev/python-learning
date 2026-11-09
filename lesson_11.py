import requests

name = input("Введите имя пользователя GitHub: ")
url = "https://api.github.com/users/" + name
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Логин:", data["login"])
    print("Публичных репозиториев:", data["public_repos"])
    print("Подписчиков:", data["followers"])
elif response.status_code == 404:
    print("Пользователь не найден")
else:
    print("Ошибка запроса, код:", response.status_code)