from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
# bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)

for files in os.listdir('D:\Projects\CB\chatterbot-corpus-1.2.0\chatterbot-corpus-1.2.0\chatterbot_corpus\data\english/'):
	data = open('D:\Projects\CB\chatterbot-corpus-1.2.0\chatterbot-corpus-1.2.0\chatterbot_corpus\data\english/' + files , 'r').readlines()
	trainer.train(data)
	
while True:
	msg = input('User: ')
	if msg.strip() != 'Bye' :
		reply = bot.get_response(msg)
		print('Bot: ',reply)
	elif msg.strip() == 'Bye' :
		print('Bot: - Thank You. Have a nice day.')
		break	
