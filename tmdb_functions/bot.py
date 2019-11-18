import logging
from tmdb import getMovie, getSerie, getPeople, getTrendMovies, getTrendSeries, getTrendDirectors
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)


class MovieGramBot():
    def __init__(self, token):
        self.token_ = token
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.reply_keyboard = [['Serie', 'Pelicula'],
                               ['Celebridad', 'Top Peliculas'],
                               ['Top Peliculas', 'Top Directores'],
                               ['Top Series']]

        self.markup = ReplyKeyboardMarkup(
            self.reply_keyboard, one_time_keyboard=True)

    def start(self, update, context):
        update.message.reply_text(
            "Hola! Soy MovieGram bot. Estoy aqui para ayudarte en tus consultas relacionadas al cine, series o celebridades.",
            reply_markup=self.markup)

        return CHOOSING

    def help(self, update, context):
        update.message.reply_text(
            "Dale click al teclado de opciones para que veas las cosas que puedo hacer :D",
            reply_markup=self.markup)

        return CHOOSING

    def regular_choice(self, update, context):
        text = update.message.text
        context.user_data['choice'] = text
        if(text != 'Pelicula' and text != 'Serie' and text != 'Celebridad'):

            if(text == 'Top Peliculas' or text == 'Top Series'):
                if(text == 'Top Peliculas'):
                    data = getTrendMovies()['results']
                else:
                    data = getTrendSeries()['results']
                for item in data:
                    msj = '{} Vote Average: {}'.format(
                        item['title'], item['vote_average'])
                    update.message.reply_text(msj, reply_markup=self.markup)
                    update.message.reply_text(item['image'])

            elif(text == 'Top Directores'):
                data = getTrendDirectors()['results']
                for directors in data:
                    for js in directors:
                        msj = '{}. Popularidad: {}'.format(
                            js['name'], js["popularity"])
                        update.message.reply_text(
                            msj, reply_markup=self.markup)
                        update.message.reply_text(js['image'])
            return CHOOSING

        update.message.reply_text(
            'Por favor dime el nombre de la {} que estas buscando!'.format(text.lower()))
        return TYPING_REPLY

    def received_information(self, update, context):
        user_data = context.user_data
        text = update.message.text
        category = user_data['choice']
        del user_data['choice']
        ph = 'https://indiehoy.com/wp-content/uploads/2018/09/nicolas-cage-meme-640x434.jpg'
        msj = 'Genial! Entonces buscas la {} llamada {}...Encontre esto:\n'.format(
            category, text)
        text = text.replace(' ', '+')
        if(category == 'Pelicula'):
            js = getMovie(text)
            if(js != None):
                msj += js['title'] + ": " + js["overview"]
                ph = js['image']
        elif(category == 'Serie'):
            js = getSerie(text)
            if(js != None):
                msj += js['title'] + ": " + js["overview"]
                ph = js['image']
        elif(category == 'Celebridad'):
            js = getPeople(text)
            if(js != None):
                msj += js['name'] + ", Popularidad: " + str(js["popularity"])
                ph = js['image']
            return CHOOSING

        if(js == None):
            msj = 'No se encontro nada'

        update.message.reply_text(msj, reply_markup=self.markup)
        update.message.reply_text(ph)
        return CHOOSING

    def done(self, update, context):
        update.message.reply_text("Espero haberte ayudado, hasta luego")
        return ConversationHandler.END

    def error(self, update, context):
        self.logger.warning('Actualizacion "%s" causo un error "%s"',
                            update, context.error)

    def run(self):
        updater = Updater(self.token_, use_context=True)
        dp = updater.dispatcher

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler(
                'start', self.start)],

            states={
                CHOOSING: [MessageHandler(Filters.regex('^(Serie|Pelicula|Celebridad|Top Peliculas|Top Series|Top Directores)$'),
                                          self.regular_choice)],

                TYPING_CHOICE: [MessageHandler(Filters.text,
                                               self.regular_choice)
                                ],

                TYPING_REPLY: [MessageHandler(Filters.text,
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


if __name__ == '__main__':
    obj = MovieGramBot('857019165:AAHkHPXfVU-iw6yb7EP5GOtQzXz4LJ8h03k')
    obj.run()
