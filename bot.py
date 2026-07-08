

import telebot
from urllib.parse import quote

TOKEN = "8812656255:AAGKsJ78U_1_xVvXMOb_N1f56vcMBmj2GZA" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom 🎵 Men musiqa qidiruvchi botman.\nQo‘shiq nomini yozing."
    )

@bot.message_handler(func=lambda message: True)
def search_music(message):
    song = message.text
    search = quote(song)

    youtube = f"https://www.youtube.com/results?search_query={search}"

    bot.send_message(
        message.chat.id,
        f"🎧 Qidiruv:\n{song}\n\nTopish uchun:\n{youtube}"
    )

bot.infinity_polling()
