intents = {
    "greet": ["hi", "hello", "hola"],
    "help": ["help", "assist", "support", "guide"],
    "price": ["price", "cost", "charges", "money"],
    "contact": ["contact", "call", "agent"],
    "code": ["code", "coding"]
}


intents_response = {
    "greet": "How! Can i assisst you today?",
    "help" : "you can ask me about time, price and vibe-codeing",
    "price": "this product value vares from 100$ to 10000$",
    "contact": "Contacing you with the agent!!!",
    "code": "vibe-coding is the best plcae to learn coding!!!"
}
def find_intent(user_input):
    user_words = user_input.split()
    for intent, keywords in intents.items():
        for word in keywords:
            if word in user_words:
                return intent
    return None

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break

    intent = find_intent(user_input)

    if intent:
        print("Chatbot:", intents_response.get(intent,"I don't understand the context.."))
    else:
        print("Chatbot: I don't understand.")
