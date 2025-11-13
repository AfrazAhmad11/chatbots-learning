import json
import random
import re
from datetime import datetime

# Load intents
with open('intents.json', 'r') as f:
    data = json.load(f)

def get_response(user_input):
    user_input = user_input.lower()

    for intent in data['intents']:
        for pattern in intent['patterns']:
            if re.search(pattern, user_input):
                response = random.choice(intent['responses'])
                return response
    
    return "I'm sorry, I didn't quite understand that. Could you please rephrase?"

def log_conversation(user_input, bot_response):
    with open("chat_log.txt", "a") as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] User: {user_input}\n")
        log.write(f"Bot: {bot_response}\n\n")

print(" Chatbot: Hello! I'm your virtual assistant. Type 'quit' to end.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print(" Chatbot: Goodbye! 👋")
        break
    response = get_response(user_input)
    print(f" Chatbot: {response}")
    log_conversation(user_input, response)
