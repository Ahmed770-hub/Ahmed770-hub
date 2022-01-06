import os
#import string
import requests
from user_agent import generate_user_agent
import random
import telebot

os.system("pip install user_agent")
os.system("pip install requests")

print("work now")
token = input("Enter your token : ")

bot = telebot.TeleBot(token)

	
	
#{"user":true,"authenticated":false,"status":"ok"}

#Done » JPXAT

@bot.message_handler(commands=["start"])
def start(message):
	name = message.chat.first_name
	bot.send_message(message.chat.id,f"Welcom {name}\nEnter size of user »")
	
	
	
	
@bot.message_handler(func=lambda m:True)
def run(message):
	size = int(message.text)
	if size == '3':
		bot.send_message(message.chat.id,f"Error")
	elif size == '4':
		bot.send_message(message.chat.id,f"Hard to take one")
	else:
		bot.send_message(message.chat.id,f"Wait...")
		pass
	while True:
		chars="QWERTYUIOPASDFGHJKLZ"
		user = ''.join(random.sample(chars,size))
		pase = "01025596953"
		url = 'https://www.instagram.com/accounts/login/ajax/'
		head = {
		'Host': 'www.instagram.com',
		'content-length': '318',
		'sec-ch-ua': '\' Not A;Brand\';v\u003d\'99\', \'Chromium\';v\u003d\'96\', \'Google Chrome\';v\u003d\'96\'',
		'x-ig-app-id': '1217981644879628',
		'x-ig-www-claim': '0',
		'x-requested-with': 'XMLHttpRequest',
		'sec-ch-ua-mobile': '?1',
		'x-instagram-ajax': '05272981ffad',
		'content-type': 'application/x-www-form-urlencoded',
		'accept': '*/*',
		'user-agent': generate_user_agent(),
		'x-asbd-id': '198387',
		'save-data': 'on',
		'x-csrftoken': 'nvJWhjTz2FSucDSsfpAhgDj21FHzuR4N',
		'sec-ch-ua-platform': '\'Android\'',
		'origin': 'https://www.instagram.com',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-mode': 'cors',
		'sec-fetch-dest': 'empty',
		'referer': 'https://www.instagram.com/accounts/login/',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,fil;q\u003d0.9,en;q\u003d0.8',
		'cookie': 'ig_nrcb\u003d1'
		}
		dat = {'username': user,'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(pase),'queryParams':'{}','optIntoOneTap':'{}'
		}
		
		r = requests.Session()
		req = r.post(url, headers=head, data=dat, proxies=None).json()
		print(req)
		if "user" in req:
			if req["user"] == False:
				bot.send_message(message.chat.id,f"[+] Done » {user}")
			else:
				print(f"fail » {user}")
		else:
			print("fuck")

	
	
	
bot.polling()
