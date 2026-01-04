while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("chatbot: Goodbye! (^_^)")
        break
    elif user_input == "help":
        print("Chatbot: You can ask me about the price, help, contact or just have a casual chat!")
    elif user_input == "price":
        print("Chatbot: Prices ranges from 10PKR to 1000PKR")
    elif user_input == "contact":
        print("Chatbot: Contacting you to our Agent")
    else:
        print("Chatbot: I don't understand")