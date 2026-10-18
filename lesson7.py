from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()
chat = client.chats.create(model="gemini-3-flash-preview")

print("Chat started. Type quit when you want to stop.")

while True:
    message = input("You: ")

    if message.lower() == "quit":
        print("Bye!")
        break

    response = chat.send_message(message)
    print("AI:", response.text)
    print()