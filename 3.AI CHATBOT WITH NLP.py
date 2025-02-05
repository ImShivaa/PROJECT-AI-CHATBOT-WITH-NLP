import nltk
from nltk.chat.util import Chat, reflections

name = input("Enter your name: ").upper()
print(f"Welcome, {name}! Start chatting with the bot. Type 'bye' to exit.")

pairs = [
    ["hi|hello|hey|hii", ["Hello!", "Hi there!"]],
    ["how are you", ["I'm a bot, I'm always good!"]],
    ["what is your name", ["I'm a chatbot."]],
    ["Who created you", ["My Creator Name is Shiva..!"]],
    ["bye", ["Goodbye!", "See you later!"]]
]

chatbot = Chat(pairs, reflections)

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)

print(f"Thank you for using, {name}!")
