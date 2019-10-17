import re
from tmdb import *
import requests
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
token_ = '857019165:AAHkHPXfVU-iw6yb7EP5GOtQzXz4LJ8h03k'


def start(update, context):
    update.message.reply_text(
        'Hola! Soy MovieGram bot. Estoy aqui para ayudarte en tus aventuras cinefilas')


def main():
    updater = Updater(token_, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
