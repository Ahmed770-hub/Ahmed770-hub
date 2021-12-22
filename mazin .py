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


user = input("Enter link : ")
view = int(input("Enter number of view : "))
k = (view)/60
print(f'''
You will take {view} view in {k} Hours or {view} in minute''')
lim = round(view)
for i in range(0,lim):
	webbrowser.open(user)
	print("Done you take 1 view")
	time.sleep(5)



	