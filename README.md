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
