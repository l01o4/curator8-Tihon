import telebot

bot = telebot.TeleBot('6904102355:AAGWpUI_3THQVNja2FvDLl2gNcQOaQHWZQw')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'Я рад что вы пользуетесь нашим ботом!!!')


@bot.message_handler(commands=['tame'])
def main(message):
    bot.send_message(message.chat.id, 'Все? \nПроверка закончена?')


@bot.message_handler(commands=['sos'])
def main(message):
    bot.send_message(message.chat.id, 'Я рад что *вы* можете проверять мою разработку!!!', parse_mode='Markdown')


@bot.message_handler(commands=['end'])
def main(message):
    bot.send_message(message.chat.id, 'Надеюсь у *вас* все прекрасно!!!', parse_mode='Markdown')


bot.infinity_polling()
