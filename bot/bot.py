import telebot
import random

bot = telebot.TeleBot('957272676:AAHQ9kvyAbbchgGqqYe1Pct_SbjjZ9ebUis')


@bot.message_handler (content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, 'Вот и отличненько 😊')

# RUN
bot.polling (none_stop=True)