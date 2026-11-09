import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
key = os.getenv("AI_API_KEY")

if not key:
    print("Ключ не найден. Проверьте файл .env")
    exit()

client = Groq(api_key=key, timeout=60)

try:
    answer = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": "Объясни в двух предложениях, что такое переменная в Python."}
        ],
    )
    print(answer.choices[0].message.content)
    print("Токены:", answer.usage.total_tokens)
except Exception as error:
    print("Ошибка запроса:", error)