#5-3 alien colours
alien_colour = 'green'
alien_colour1 = 'yellow'
alien_colour2 = 'red'
if alien_colour == 'green':
	print("you just earned 5 points")

if alien_colour == 'green':
	print("")

#5-4 alien colours 2
if alien_colour != 'green':
	print("you earned 5 points")
else:
	print("you earned 10 points")

#5-5 alien colours 3
if alien_colour == 'green':
	print("you earned 5 point")
elif alien_colour1 == 'yellow':
	print('you earned 10 points')
elif alien_colour2 == 'yellow':
	print("you earned 15 points")

#5-6 stages of life
age = 17

if age <2:
	print('you are a baby')
elif age >= 2 and age < 4:
	print('you are a toddler')
elif age >=4 and age <13:
	print('you are a kid')
elif age >=13 and age < 20:
	print('you are a teenager')
elif age >=20 and age <=65:
	print('you are an adult')
else:
	print('you are an elder')

#5-7 favourite fruit
favourite_fruit = ['grapes', 'apples', 'peaches']
for
if 'grapes' in favourite_fruit:
	print(f'you really like {favourite_fruit[0]}')
if 'apples' in favourite_fruit:
	print(f'you really like {favourite_fruit[1]}')
if 'peaches' in favourite_fruit:
	print(f'you really like peaches')
else:
	print('you do not like this fruit')