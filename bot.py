import telebot

TOKEN = "8812656255:AAGKsJ78U_1_xVvXMOb_N1f56vcMBmj2GZA" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! Men ishga tushdim 😊")

bot.infinity_polling()
