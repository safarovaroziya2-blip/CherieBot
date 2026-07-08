
import telebot
from urllib.parse import quote

TOKEN = "8812656255:AAGKsJ78U_1_xVvXMOb_N1f56vcMBmj2GZA" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom 😊 Qo‘shiq nomini yozing, men qidirib beraman 🎵"
    )

@bot.message_handler(func=lambda message: True)
def search_song(message):
    song = message.text
    query = quote(song)

    youtube_link = f"https://www.youtube.com/results?search_query={query}"

    bot.send_message(
        message.chat.id,
        f"🎵 Siz qidirgan qo‘shiq:\n{song}\n\n🔎 YouTube qidiruvi:\n{youtube_link}"
    )

bot.infinity_polling()

