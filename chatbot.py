# Uncomment the following lines to enable verbose logging
#import logging
#logging.basicConfig(level=logging.DEBUG)
from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot import corpus
#from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot_corpus.corpus import DATA_DIRECTORY

app=Flask(__name__)

bot=ChatBot("panda",storage_adapter='chatterbot.storage.SQLStorageAdapter',tie_breaking_method="random_response",database_uri='sqlite:///database.sqlite3')
bot.storage.drop()

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train based on the english corpus
#trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.custom")

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    user_input=request.args.get('msg')
    return str(bot.get_response(user_input))

if __name__=="__main__":
    app.run()
