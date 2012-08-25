from Dice import roll,d4,d6,d8,d10,d12,d100

while True:
	try:
		x=input(">>> ")
		print x
	except SyntaxError:
		print "stop fuckin' around"