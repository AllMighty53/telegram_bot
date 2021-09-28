#!/Users/idanso/miniconda3/bin/python ## make sure your path to python3 is right 

## in this example there are two commands one is "start" ans one is "command" you can replace that with anything just make
## sure the handler and the function have the same name 


import os
from telegram.ext import Updater ## make sure to install telegram lib using "pip install python-telegram-bot --upgrade"
from telegram.ext import CommandHandler


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hello")


def command(bot, update):
    var1 = os.popen('whoami').read() ## any command you want 
    var = "you are: "+ var1
    bot.send_message(chat_id=update.message.chat_id, text=var1)


def starthandling():
    updater = Updater(token=key)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    start_handler1 = CommandHandler('command', command)
    dispatcher.add_handler(start_handler1)
    dispatcher.add_handler(start_handler)
    updater.start_polling()

if __name__=='__main__':
    key = input("Input Your Telegram Token: ")
    starthandling()
111
1344311
