# -*- coding: utf-8 -*-
import telebot
import os
import requests
import upl
import config
import time

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
  output = 'Lol'
  bot.send_message(message.chat.id,output)

servers = 'https://raw.githubusercontent.com/Kamakepar2029/decentralised_server/main/serverlist.txt'

srv = requests.get(servers)
print(srv.text)

srvd = (srv.text).split(',')

print(srvd[0])
print(srvd[1])
print(srvd[2])

upl.upload_to_server('get_phone.py', srvd[0])

@bot.message_handler(content_types=['text'])
def lalala(message):
  if (message.text == 'Hello'):
    bot.send_message(message.chat.id, 'Hello Man')
  else:
    u = 'Your message was: '+str(message.text)+' :-)'
    bot.send_message(message.chat.id, u)

@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
  try:
    chat_id = message.chat.id

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    print(message.document.file_name)
    src = 'received/' + message.document.file_name;
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    start = 0
    end = len(srvd)
    bot.reply_to(message, "📡 Your file is availible at our decentralised_servers:")
    while (start < (end)):
      upl.upload_to_server('received/'+message.document.file_name,srvd[start])
      bot.send_message(chat_id, srvd[start]+"/uploads/"+message.document.file_name)
      bot.send_message(chat_id, '⌛️ Waiting 5 sec to upload it to next server...')
      time.sleep(5)
      start+=1
    os.system('rm "received/'+message.document.file_name+'"')
    bot.send_message(chat_id, '🛢 Everything uploaded.')

  except Exception as e:
    bot.reply_to(message, e)

bot.polling(none_stop=True)
#url = ''
#files = {'media': open('test.jpg', 'rb')}
#requests.post(url, files=files)