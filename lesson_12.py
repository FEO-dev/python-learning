import os
   
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("AI_API_KEY")

if key:
    print("Ключ найден, длина:", len(key))
else:
    print("Ключ не найден")