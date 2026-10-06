#IMP: we can use openAI to make calls to gemini
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)


response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role": "user", "content": "Hey there! My name is Bakugo, who are you?"}
    ]
)

print(response.choices[0].message.content)  