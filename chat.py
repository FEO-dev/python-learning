import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
key = os.getenv("AI_API_KEY")

if not key:
    print("Ключ не найден. Проверьте файл .env")
    exit()

client = Groq(api_key=key, timeout=60)
MODEL = "openai/gpt-oss-20b"

messages = [
    {"role": "system", "content": "Ты помощник для начинающего программиста. Отвечай по-русски, коротко."}
]

print("Чат запущен. Для выхода напишите: выход")

while True:
    user_text = input("Вы: ").strip()
    if user_text == "":
        continue
    if user_text.lower() == "выход":
        break

    messages.append({"role": "user", "content": user_text})

    try:
        answer = client.chat.completions.create(model=MODEL, messages=messages)
    except Exception as error:
        print("Ошибка запроса:", error)
        messages.pop()
        continue

    text = answer.choices[0].message.content
    messages.append({"role": "assistant", "content": text})
    print("Бот:", text)
    print("Токены запроса:", answer.usage.prompt_tokens)
    print("Токены ответа:", answer.usage.completion_tokens)