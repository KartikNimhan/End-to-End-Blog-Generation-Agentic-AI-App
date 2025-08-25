from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
print("Using key:", api_key[:12])

client = Groq(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Hello Groq!"}],
    )
    print("✅ Success:", response.choices[0].message["content"])
except Exception as e:
    print("❌ Error:", e)
