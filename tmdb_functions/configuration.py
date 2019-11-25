import os

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)
TOKEN = '857019165:AAHkHPXfVU-iw6yb7EP5GOtQzXz4LJ8h03k'
PORT = int(os.environ.get('PORT', '5000'))
NOTHING = 'https://indiehoy.com/wp-content/uploads/2018/09/nicolas-cage-meme-640x434.jpg'
WEBHOOK = "https://moviegrambot.herokuapp.com/"
OPTIONS = '^(Serie|Pelicula|Actor|Director|Top Peliculas|Top Series|Top Directores)$'
HELP_MESSAGE = "Dale click al teclado de opciones para que veas las cosas que puedo hacer :D"
OPTIONS_KEYBOARD = [['Serie', 'Pelicula'],
                    ['Actor', 'Director'],
                    ['Top Peliculas', 'Top Directores'],
                    ['Top Series']]
WELCOME_MESSAGE = "Hola! Soy MovieGram bot. Estoy aqui para ayudarte en tus consultas relacionadas al cine, series o celebridades."
REPLY_MESSAGE = 'Por favor dime el nombre de la {} que estas buscando!'
REPLY_MESSAGE_FOUND = 'Genial! Entonces buscas la {} llamada {}...Encontre esto:\n'
