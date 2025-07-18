import nltk
import random

# Download required data
nltk.download('punkt')

# Sample questions and answers
pairs = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm just a chatbot, but I'm doing great!",
    "what is your name": "I am a simple AI chatbot.",
    "bye": "Goodbye! Have a nice day.",
    "thanks": "You're welcome!"
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    for question in pairs:
        if user_input == question:
            return pairs[question]
    return "Sorry, I don't understand that."

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Bye! Take care.")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
