#if statement
food = ['pizza', 'burgers', 'jalapeno', 'dumpling']
for foods in food:
	if foods == 'dumpling': # == means checking for equality and != means checking for inequalities
		print(foods.upper())
	else:
		print(foods.title())

#checking multiple conditions
for foods in food:
	if 'jalapeno' in food:
		print(f"\n{'jalapeno'} is a spice")
		break

#simple if statements
age = 19
if age >=18:
	print("you are old enough to vote!")
	print("have you registered to vote yet")
else:
	print("sorry youre ntoo young to vote")
	print("register when you're old enough\n")

age_1 = 13
if age_1 >4 and age_1 <10:
	print("your admission cost is %0.00\n")
elif age_1 < 18:
	print("your admission fee is $25\n") #same as an if but its an else
else:
	print("your admission cost is $40\n")

#using if statements with lists
requ_toppings = ['mushroom', 'jalapenos', ]
if 'mushroom' in requ_toppings:
	print('adding mushrooms\n')
elif 'jalapenos' in requ_toppings:
	print('adding jalapenos')


#checking if a list is not empty


#using multiple lists
available_snacks = ['chips', 'chocolate', 'candy bar', 'jelly babies', 'sour jelly beans', 'coke']
requested_snacks = ['chips', 'coke', 'jelly babies', 'Blah', 'fanta']
for requested_snack in requested_snacks:
	if requested_snack in available_snacks:
		print(f'adding {requested_snack}')
	else:
		print(f'\tsorry we dont have {requested_snack.title()}')
print(f'\nFinished ordering your {requested_snack}')