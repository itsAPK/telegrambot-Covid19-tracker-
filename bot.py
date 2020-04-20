import telebot
import requests
from bs4 import BeautifulSoup
import time
from telebot import types


token='your_bot_token'
bot=telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id,'Hey There,\n Use /covid to acsess tracker')

@bot.message_handler(commands=['covid'])
def qr_code_handler(message):    
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, "retriving data...")
    req=requests.get('https://www.worldometers.info/coronavirus/')
    soup=BeautifulSoup(req.text,'html.parser')
    title=soup.find_all("div",class_='maincounter-number')
    total=title[0].text.strip()
    death=title[1].text.strip()
    reacover=title[2].text.strip() 
    t =f'📌Total Case : {total}\n📌Total Deaths : {death}\n📌Total Recoverd : {reacover}'
    bot.send_chat_action(message.chat.id,'typing')
    bot.send_message(message.chat.id,t)



@bot.message_handler(commands=['symptoms'])
def donate_handler(message):
    bot.send_chat_action(message.chat.id,'typing')
    bot.send_message(message.chat.id, "Coronavirus Symptoms (COVID-19)\n\n"
                                       "Reported illnesses have ranged from people with mild symptoms to people being severely ill and dying.\n\n"
                                        "Symptoms can include:\n\n"
                                        "📌Fever\n📌Cough\n📌Shortness of breath")
    

@bot.message_handler(commands=['donate'])
def donate_handler(message):
    bot.send_message(message.chat.id, "Donate And Support Us.\n\nUPI :terabyt3.network@sbi\nBITCOIN : 1DSdx7j7UT4TmnWr4xgXM2ispK87EU8G5Y")
    
        
       

  





while True:
	try:
		bot.infinity_polling(True)
	except Exception:
		time.sleep(1)
