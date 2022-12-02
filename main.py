from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from controller import *

bot = Bot(token = '5900644164:AAGoh9XW1-JH6yTNJfv9MAgslmkyJLEZHv8')
updater = Updater(token = '5900644164:AAGoh9XW1-JH6yTNJfv9MAgslmkyJLEZHv8')
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
count_handler = MessageHandler(Filters.text, count)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(count_handler)


updater.start_polling()
updater.idle()