red='\033[0;91m'
gre='\033[0;92m'
yel='\033[0;93m'
cy='\033[0;96m'
wh='\033[0;97m'

print("choose...")
print(gre+"[1] Times ")
print("[2] Subtract ")
print("[3] Add")
print("[4] ahmed")

g=input("choose : ")
c=input(yel+"your num 1:")
x=input("your num 2:")
if g=='1':
	res=(float (c)* float (x) )
	print(res)
	
elif g=='2':
	res=(float (c) - float (x) )
	print(res)
	
elif g=='3':
	res=(float (c) + float (x) )
	print(res)
	
elif g=='4':
	res=(float (c) / float (x) )
	print(res)
else:
	print("FALSE")


