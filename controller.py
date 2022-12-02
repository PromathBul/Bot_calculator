from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from separation import *
from logger import log

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите выражение, которое необходимо посчитать без пробелов...')

def count(update, context):
    expression = update.message.text
    expression_list = parse(expression)
    result = braces(expression_list)
    context.bot.send_message(update.effective_chat.id, f'Результат вашего выражения = {result}')
    log(update, context, expression_list, result)