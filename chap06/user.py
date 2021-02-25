#looping through dictionaries
user_0 = {
	'mini' : 'rossouw',
	'honda' : 'mo',
	'golf' : 'elgin',
	'bmw' : 'keo'
	}

for key, value in user_0.items():
	print(f'\ncar: {key}')
	print(f'owner: {value}\n')

for things in user_0.keys():
	print(f'{things.title()}\n')

for names in user_0.values():
	print(names.title())

for names in sorted(user_0.keys()):
	print(f'\n{names.title()} thank you for entering your information')

for user in set(user_0.values()):
	print(f'\n{user.title()}')

#nesting(storing multiple dictoinaries)



#list in dictoinary
# Store information about a pizza being ordered.
# pizza = {
# 'crust': 'thick',
# 'toppings': ['mushrooms', 'extra cheese'],
# }

# print(f"You ordered a {pizza['crust']}-crust pizza "
# "with the following toppings:")
# for topping in pizza['toppings']:
# 	print("\t" + topping)

favorite_cars = {
'elgin': ['VW', 'renault'],
'moha': ['honda'],
'ross': ['mini', 'ford'],
'keoo': ['bmw', 'mercedes'],

}
for name, car in favorite_cars.items():
	print(f"\n{name.title()}'s favorite cars are:")
	for brand in car:
		print(f"\t{brand.title()}")


#dictionary in a dictionary
users = {
'car 1': {
'brand': 'volkwagen',
'model': 'golf 5 GTI',
'mileage': '150000KM',
},
'car 2': {
'brand': 'hyundai',
'model': 'i30N',
'mileage': '75000km',
},
}

for cars, info in users.items():
	print(f'\nname: {cars}')
	car_name = f"{info['brand']} {info['model']}"
	mileage = info['mileage']
	print(f'\tbrand and model : {car_name.title()}')
	print(f'\tmileage : {mileage.title()}')
