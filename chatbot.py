def chatbot_response(user_input):
    # Convert the input to lowercase for easier matching
    user_input = user_input.lower()

    # Basic greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    # Farewell responses
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    # Help responses
    elif "help" in user_input:
        return "I'm here to help! You can ask me questions about our services or just say hello."

    # Specific queries
    elif "weather" in user_input:
        return "I'm not connected to the internet, so I can't provide live weather updates. But you can check a weather app!"

    elif "your name" in user_input:
        return "I'm your friendly chatbot. You can call me ChatBuddy!"

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're very welcome!"

    # Default response if no keywords match
    else:
        return "I'm not sure I understand. Could you please rephrase?"

# Main function to keep the chatbot running
def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! It was nice chatting with you.")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
run_chatbot()
