import telebot

TOKEN = "5366141483:AAEiYvQgf_zeWHU6I4EVzgPMxILNTEAoGMY"

bot = telebot.TeleBot(TOKEN)

keys={
    'биткоин': 'BTC',
    'эфириум':'ETH',
    'доллар':'USD'
}



@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text= 'Чтобы начать работать введите команду бота в следующем формате через пробел :\n<имя валюты> \
<в какую валютуперевести> \
<количество переводимой валюты>\n Увидеть список всех доступных валют /values '
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text ='Доступные валюты'
    for key in keys.keys():
       text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(commands=['stop'])
def stop(message: telebot.types.Message):
    stop=False
    text = "Ну и вали!"
    bot.reply_to(message, text)

bot.polling()
updater.idle()

