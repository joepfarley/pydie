#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Dice import roll , d4, d6, d8, d10, d12, d20, d100

x=0
y=0
z=0

def setSession():
	session = {
	"Neald": -1+x,
	"Protoza": +x,
	"Gybon": 2+x,
	"Medalion":4+x,
	"Muerte":  4+x,
	}
	return session

session = setSession()

from Dice import addINIT,dropINIT,setINIT#init,INIT
import operator
import Dice


def init(x=session):Dice.init(x)
def INIT(x=session):Dice.INIT(x)


def GSPOT(x=0): # x = penalty or bonus to group. Will be 0 by default
	n = d20()+3+x
	p = d20()+1+x
	g = d20()+0+x
	me = d20()+3+x
	mu = d20()+6+x
	gSpot={
		"Neald": n,
		"Protoza": p,
		"Gybon": g,
		"Medailion": me,
		"Muerte":  mu,
		}
	return gSpot


def gspot(x=0): 
	gspot=GSPOT(x)
	for i in gspot:
		print i,":",gspot[i]

