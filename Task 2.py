

import random

responses = {
    "hi": ["Hello!", "Hi there!", "Greetings!"],
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm a bot, so I don't have feelings, but thanks for asking!", "I'm here to help you!", "I'm functioning as expected!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "what is your name": ["I'm ChatBot123, your friendly assistant!", "You can call me ChatBot123.", "I am ChatBot123, nice to meet you!"],
    "what can you do": ["I can help you with various tasks, just ask!", "I'm here to assist you with information and tasks.", "I can answer questions, provide information, and help with tasks!"],
    "thank you": ["You're welcome!", "Happy to help!", "Anytime!", "No problem!"],
    "help": ["How can I assist you today?", "What do you need help with?", "Feel free to ask me anything!"],
    "what's the weather like": ["I don't have real-time data, but you can check a weather website!", "Weather can vary, check your local forecast!"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "good morning": ["Good morning! How can I assist you today?", "Morning! Hope you have a great day!"]
}

# Function to generate chatbot response
def chatbot_response(user_input):
    for key in responses:
        if key in user_input.lower():
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

# Function to print styled messages
def print_message(sender, message):
    if sender == "Chatbot":
        print(f"\033[1mChatbot:\033[0m {message}")  
    else:
        print(f"\033[94m{sender}:\033[0m {message}")  

# Main chatbot loop
def chatbot():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("\033[92mYou:\033[0m ")  
        if "bye" in user_input.lower():
            print_message("Chatbot", "Goodbye!")
            break
        response = chatbot_response(user_input)
        print_message("Chatbot", response)

# Run the chatbot
chatbot()