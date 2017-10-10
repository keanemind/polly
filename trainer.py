from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Polly", read_only=True)
chatbot.set_trainer(ListTrainer)

with open('training.txt') as training:
    for line in training:
        chatbot.train(line.split('++'))
