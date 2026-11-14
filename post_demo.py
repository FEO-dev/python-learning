import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Мой первый пост",
    "body": "Привет из Python",
    "userId": 1,
}

response = requests.post(url, json=data, timeout=10)
print(response.status_code)
print(response.json())