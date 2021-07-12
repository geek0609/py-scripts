import telebot
import sys
import os

def send_mes(text):
    if text == "":
        text = "NO/EMPTY TEXT GIVEN TO SEND"
    return bot.send_message(CHAT_ID, text)


# Init telegram bot
try:
    BOT_API = sys.argv[2]
    CHAT_ID = sys.argv[1]
except LookupError:
    print("Proper arguments not given, usage\npython3 SendMessage.py <CHAT-ID> <BOT-API>")
    exit()

bot = telebot.TeleBot(BOT_API, parse_mode="HTML")

try:
    print (sys.argv[3])
    send_mes("**BUILD HAS COMPLETED**\n\n**Log:** " + os.popen("$ curl --upload-file ./*.zip https://transfer.sh/"+ sys.argv[3] + ".zip").read())
except:
    print("No 3rd Arg given")
    send_mes("**BUILD HAS COMPLETED**\n\n**Log:** " + os.popen("$ curl --upload-file ./*.zip https://transfer.sh/kernel.zip").read())
