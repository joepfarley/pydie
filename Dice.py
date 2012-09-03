#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
/*		
 *		Copyright 2011 Joe Farley
 *	
 *	
 *      This program is free software; you can redistribute it and/or modify
 *      it under the terms of the GNU General Public License as published by
 *      the Free Software Foundation; either version 2 of the License, or
 *      (at your option) any later version.
 *      
 *      This program is distributed in the hope that it will be useful,
 *      but WITHOUT ANY WARRANTY; without even the implied warranty of
 *      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *      GNU General Public License for more details.                   
 *      
 *      You should have received a copy of the GNU General Public License
 *      along with this program; if not, write to the Free Software
 *      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 *      MA 02110-1301, USA.
 */
"""


from random import randint
import getopt, sys
import operator



#rolls the dice where x is the number of dice and y the number of dice
def roll(x=2,y=6): 
    total=0
    for count in range(0,x):
        total = randint(1,y)+total
    return total


def d4(): return roll(1,4)
def d6(): return roll(1,6)
def d8(): return roll(1,8)
def d10(): return roll(1,10)
def d12(): return roll(1,12)
def d20(): return roll(1,20)
def d100(): return roll(1,100)

def ability():
	x=[]
	for count in range(0,4): x.append(d6())
	x.sort()
	x.pop(0)
	x.reverse
	return sum(x)

def array(x=6,y=1,z=150):
	array=[]	
	while sum(array) < y or sum(array) > z:
		array=[]
		for count in range(0,x): array.append(ability())
	array.sort()
	return array

#below is the set of initiative functions

def addINIT(x): #x will be the init set to use
	name = raw_input("character's name: ")
	modifer = input("Initiative bonus: ")
	x[name]=modifer
	return x

def DROPINIT(x):
	init(x)
	name = raw_input("Who would you like to remove? ")
	del x[name]

def setINIT(x,y={}): #x=number of combatants
	y={}
	session = y
	for i in range(0,x):
		addINIT(session)
	return session

def dropINIT(y={},x=1): #x=number of combatants
	session = y
	for i in range(0,x):
		DROPINIT(session)
	return session
	
def INIT(z,x=0,y=0):
	tempSession = {}
	for i in z:
		b = z[i]+d20()
		tempSession[i] = b
	b=z
	sortedINIT = sorted(tempSession.iteritems(), reverse = True, key=operator.itemgetter(1))
	return sortedINIT

def init(z,x=0,y=0):
	q=INIT(z,x,y)
	for i in q:
		print i[0],':',i[1]






def basic_help():
	x= """ 
	Dice Rolling Terminal Application
	Type roll(x,y)+z 
	x = number of dice
	y = number of sides
	z = additional modifier
	For example:
	
		>>> roll(2d6)+8
		18

	type ability() to roll 4d6 and drop the lowest
	type array(x) to get the number of x as above
	
	type help() to get this menu plus more tidbits
	
	Copyright 2011 Joe Farley
	"""
	
def help():
	basic_help()
	x="""
	this program should be launched using -i argument
	which loads all of the functions but leaves the
	python interpreter open. Theoretically this allows
	you to use any python code to create custom dice 
	rolls. Here are some examples. 

	Custom attack roll. 

	Aginor has a +1 great sword, a base attack bonus 
	of +3, and a strength of 18. (a modifier of +4)
	A great sword does 1d12 damage plus strength. 
	Rather than type roll(1,20)+8 then roll(1,12)+5 
	you could create a function and name it what you
	want. Here’s how

	def gs():return [roll(1,20)+8,roll(1,12)+5]

	This will return an array with the attack roll
	and damage every time you type in gs()
	
	say he levels up and has multiple attacks with a 
	base attack bonus of 7/1
	
	def gs2():return [[roll(1,20)+1+4+7,roll(1,12)+5],[roll(1,20)+1+4+1,roll(1,12)+5]]

	Reminders:
	*python is case sensitive
	*use square [] brackets 
	*separate each item with a comma 
	*you may also create nestled functions like
	roll(roll(1,3),6) 
	this will roll 1d6 d6’s
	
	you may also use variables so you don't 
	need to type the number each time. 
	
	strength = 4
	def gs2():return [[roll(1,20)+1+strength+7,roll(1,12)+strength+1],[roll(1,20)+1+strength+1,roll(1,12)+strength+1]]
	
	then anytime Aginor's strength increases 
	permenantly or temporarly you can just
	update strength without changing the function.
	"""
	print x



if __name__ == '__main__':
	basic_help()

