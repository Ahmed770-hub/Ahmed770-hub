import os 

try:
	import requests
	import webbrowser
	import time
	import random
except ModuleNotFoundError:
	os.system("pip install webbrowser")
	os.system("pip install requests")
	os.system("pip install time")
	
import requests
import webbrowser
import random


a = input("Enter link : ")
u = input("Enter another link : ")
view = int(input("Enter number of view : "))/2

k = (view)/60
print(f'''
You will take {view} view in {k} Hours or {view} in minute''')
lim = round(view)
for i in range(0,lim):
	webbrowser.open(a)
	print("Done you take 1 view")
	time.sleep(61)
	webbrowser.open(u)
	print("Done you take 1 view")
	time.sleep(61)



	