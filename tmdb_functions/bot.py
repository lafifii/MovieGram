import logging
from tmdb import getMovie, getSerie
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)


class MovieGramBot():
    def __init__(self):
        # no nos hackeen porfi t.t
        self.token_ = '857019165:AAHkHPXfVU-iw6yb7EP5GOtQzXz4LJ8h03k'
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.reply_keyboard = [['Serie', 'Pelicula'],
                               ['Celebridad', 'Proximamente lol'],
                               ['Adios']]

        self.markup = ReplyKeyboardMarkup(
            self.reply_keyboard, one_time_keyboard=True)

    def start(self, update, context):
        update.message.reply_text(
            "Hola! Soy MovieGram bot. Estoy aqui para ayudarte en tus aventuras cinefilas",
            reply_markup=self.markup)

        return CHOOSING

    def regular_choice(self, update, context):
        text = update.message.text
        context.user_data['choice'] = text
        update.message.reply_text(
            'Por favor dime el nombre de la {} que estas buscando!'.format(text.lower()))
        return TYPING_REPLY

    def received_information(self, update, context):
        user_data = context.user_data
        text = update.message.text
        category = user_data['choice']
        del user_data['choice']
        msj = 'Genial! Entonces buscas la ' + category + \
            ' llamada ' + text + '...Encontré esto:\n'
        text = text.replace(' ', '+')
        if(category == 'Pelicula'):
            js = getMovie(text)
            msj += js['title'] + ": " + js["overview"]
            ph = js['image']
        elif(category == 'Serie'):
            js = getSerie(text)
            msj += js['title'] + ": " + js["overview"]
            ph = js['image']
        update.message.reply_text(msj, reply_markup=self.markup)
        update.message.reply_text(ph)
        return CHOOSING

    def done(self, update, context):
        update.message.reply_text("Espero haberte ayudado, hasta luego")
        return ConversationHandler.END

    def error(self, update, context):
        self.logger.warning('Update "%s" caused error "%s"',
                            update, context.error)

    def run(self):
        updater = Updater(self.token_, use_context=True)
        dp = updater.dispatcher

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', self.start)],

            states={
                CHOOSING: [MessageHandler(Filters.regex('^(Serie|Pelicula|Celebridad)$'),
                                          self.regular_choice)],

                TYPING_CHOICE: [MessageHandler(Filters.text,
                                               self.regular_choice)
                                ],

                TYPING_REPLY: [MessageHandler(Filters.text,
                                              self.received_information),
                               ],
            },

            fallbacks=[MessageHandler(Filters.regex('^Adios$'), self.done)]
        )

        dp.add_handler(conv_handler)
        dp.add_error_handler(self.error)
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    obj = MovieGramBot()
    obj.run()
