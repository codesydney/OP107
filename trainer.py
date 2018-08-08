from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Training
chatterbot = ChatBot("Training the chatbot")
chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "Hi!",
    "Hello!",
])

chatterbot.train([
    "Hi there!",
    "Hello",
])

chatterbot.train([
    "Hello!",
    "Hi!",
])

chatterbot.train([
    "Where can I find our accounts register?",
    "It's is in our network drive G:/Customer Folder/",
])

# Quick Testing
print("Hi!")
response = chatterbot.get_response("Hi!")
print(response)