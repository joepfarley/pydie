from Dice import roll,d4,d6,d8,d10,d12,d100,array,help
import re

def phraser():
	while True:
		try:
			x=input(">>> ")
			print x
		except SyntaxError:print "type help() for assistance"
		except NameError:print "type help() for assistance"
		except ZeroDivisionError:print "type help() for assistance"

phraser()




