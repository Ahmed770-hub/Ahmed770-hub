import requests
from user_agent import generate_user_agent
from flask import Flask

#https://instagram.com/hanna_shawaly?igshid=YmMyMTA2M2Y=

app = Flask(__name__)

@app.route('/<name>')
def index(name):
	pase = 'ahmed'
	#pase = 'cudj'
	r = requests.Session()
	url = 'https://www.instagram.com/accounts/login/ajax/'
	head = {
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "x-asbd-id": "198387",
    "user-agent": generate_user_agent(),
    "x-csrftoken": "QTu4KQ5Urkz77mL6PkkqrmW6f1KcaG8Q",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://www.instagram.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.instagram.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar,fil;q\u003d0.9,en;q\u003d0.8",
    "cookie": "ig_nrcb\u003d1"
    }
	dat = {'username': name,
	'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(pase),
	'queryParams':'{}',
	'optIntoOneTap':'{}'}
	req = r.post(url, headers=head, data=dat, proxies=None).json()
	#u = req['user']
	if req['user'] == True:
	   u = {'user' : 'unavailable'}
	   return u
	elif req['user'] == False:
		p = {'user' : 'available'}
		return p
	else:
		s = {'status' : 'Error404'}
		return s

    

app.run()



