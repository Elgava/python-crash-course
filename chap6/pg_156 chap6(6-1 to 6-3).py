#6-1 person
person = {
	'first name' : 'elgin',
	'last name' : 'malouw',
	'age' : '19',
	'city' : 'johanesburg',
}
for key, value in person.items():
	print(f'\n{key}: {value}')

# for things in person.keys():
# 	print(f'{things.title()}\n')

# for names in person.values():
# 	print(names.title())

# for names in sorted(person.keys()):
# 	print(f'\n{names.title()} thank you for entering your information')

# for user in set(person.values()):
# 	print(f'\n{user.title()}')

#6-2 favourite numbers
fave_numbers ={
	
	'elgin': '17',
	'muha': '27',
	'ross': '37',
	'keoo': '47',

}
for name, num in fave_numbers.items():
	print(f"\n{name.title()}'s favorite number are:")
	for number in num:
		print(f"\t{number.title()}")
