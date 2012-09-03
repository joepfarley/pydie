import readline
from commands import getoutput
from Dice import roll,d4,d6,d8,d10,d12,d20,d100,array,help,init
import re

def phraser():
	while True:
		try:
			x=input(">>> ")
			z=getoutput('''figlet -m 2 %s'''% x);
			print z
		except SyntaxError:print "type help() for assistance"
		except NameError:print "type help() for assistance"
		except ZeroDivisionError:print "type help() for assistance"
		except TypeError:print "type help() for assistance"

phraser()




