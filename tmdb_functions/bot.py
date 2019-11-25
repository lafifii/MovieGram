import logging
import json
import configuration


from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from tmdb import getMovie, getSerie, getActor, getDirector, getTrendMovies, getTrendSeries, getTrendDirectors
from telegram import ReplyKeyboardMarkup
from flask import Flask

app = Flask(__name__)


class MovieGramBot():
    def __init__(self, token):
        self.token_ = token
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.reply_keyboard = configuration.OPTIONS_KEYBOARD

        self.markup = ReplyKeyboardMarkup(
            self.reply_keyboard, one_time_keyboard=True)

    def start(self, update, context):
        update.message.reply_text(configuration.WELCOME_MESSAGE,
                                  reply_markup=self.markup)

        return configuration.CHOOSING

    def help(self, update, context):
        update.message.reply_text(configuration.HELP_MESSAGE,
                                  reply_markup=self.markup)

        return configuration.CHOOSING

    def regular_choice(self, update, context):
        text = update.message.text
        context.user_data['choice'] = text
        if(text != 'Pelicula' and text != 'Serie' and text != 'Actor' and text != 'Director'):
            if(text == 'Top Peliculas' or text == 'Top Series'):
                if(text == 'Top Peliculas'):
                    self.toppeliculas(update)
                else:
                    self.topseries(update)
            elif(text == 'Top Directores'):
                self.topdirectores(update)
            return configuration.CHOOSING

        update.message.reply_text(
            configuration.REPLY_MESSAGE.format(text.lower()))
        return configuration.TYPING_REPLY

    def received_information(self, update, context):
        # information
        user_data = context.user_data
        text = update.message.text
        category = user_data['choice']
        del user_data['choice']
        photo = configuration.NOTHING
        message = configuration.REPLY_MESSAGE_FOUND.format(
            category, text)
        text = text.replace(' ', '+')

        # answer
        if(category == 'Pelicula'):
            js, message, photo = self.getpelicula(text, message)
        elif(category == 'Serie'):
            js, message, photo = self.getserie(text, message)
        elif(category == 'Actor'):
            js, message, photo = self.getactor(text, message)
        elif(category == 'Director'):
            js, message, photo = self.getdirector(text, message)

        if(js == None):
            message = 'No se encontro nada'

        update.message.reply_text(message, reply_markup=self.markup)
        update.message.reply_text(photo)
        return configuration.CHOOSING

    def done(self, update, context):
        update.message.reply_text("Espero haberte ayudado, hasta luego")
        return ConversationHandler.END

    def error(self, update, context):
        self.logger.warning('Actualizacion "%s" causo un error "%s"',
                            update, context.error)

    def run(self):
        updater = Updater(self.token_, use_context=True)
        updater.start_webhook(listen="127.0.0.1",
                              port=configuration.PORT,
                              url_path=configuration.TOKEN)

        updater.bot.setWebhook(configuration.WEBHOOK + configuration.TOKEN)
        dp = updater.dispatcher

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler(
                'start', self.start)],

            states={
                configuration.CHOOSING: [MessageHandler(Filters.regex(configuration.OPTIONS),
                                                        self.regular_choice)],

                configuration.TYPING_CHOICE: [MessageHandler(Filters.text,
                                                             self.regular_choice)
                                              ],

                configuration.TYPING_REPLY: [MessageHandler(Filters.text,
                                                            self.received_information),
                                             ],
            },

            fallbacks=[CommandHandler(
                'Adios', self.done), CommandHandler('help', self.help)]
        )

        dp.add_handler(conv_handler)
        dp.add_error_handler(self.error)
        updater.start_polling()
        updater.idle()

    def toppeliculas(self, update):
        data = getTrendMovies()['results']
        for item in data:
            msj = '{} Vote Average: {}'.format(
                item['title'], item['vote_average'])
            update.message.reply_text(msj, reply_markup=self.markup)
            update.message.reply_text(item['image'])

    def getpelicula(self, text, msj):
        js = getMovie(text)
        if(js != None):
            msj += js['title'] + ": " + js["overview"]
            ph = js['image']

        return js, msj, ph

    def getdirector(self, text, msj):
        js = getDirector(text)
        if(js != None):
            msj += js['name'] + ", Popularidad: " + str(js["popularity"])
            ph = js['image']
        return js, msj, ph

    def getactor(self, text, msj):
        js = getActor(text)
        if(js != None):
            msj += js['name'] + ", Popularidad: " + str(js["popularity"])
            ph = js['image']
        return js, msj, ph

    def getserie(self, text, msj):
        js = getSerie(text)
        if(js != None):
            msj += js['title'] + ": " + js["overview"]
            ph = js['image']

        return js, msj, ph

    def topseries(self, update):
        data = getTrendSeries()['results']
        for item in data:
            msj = '{} Vote Average: {}'.format(
                item['title'], item['vote_average'])
            update.message.reply_text(msj, reply_markup=self.markup)
            update.message.reply_text(item['image'])

    def topdirectores(self, update):
        data = getTrendDirectors()['results']
        for d in data:
            s = d[0]['name'] + ", es conocidx por: \n"
            for p in d[0]['known_for']:
                s += p + "\n"

            update.message.reply_text(s, reply_markup=self.markup)
            update.message.reply_text(d[0]['image'])


@app.route("/")
def main():
    obj = MovieGramBot(configuration.TOKEN)
    obj.run()


if __name__ == '__main__':
    app.run(debug=False)
