#defining a function
# def greet_user(): #def is the function
# 	"""Display a simple greeting."""
# 	print("hello!\n")

# greet_user()

# # #e.g
# def describe(animal_type, pet_name, age):
# 	print(f"hello\n")
# 	print(f'I have a {animal_type},')
# 	print(f"my {animal_type}'s name is {pet_name} and he is {age} years old")

# describe('dog', 'Astro', 1)

#multiple cfunction calls
# def describe_ani(animal_type, pet_name):
# 	print(f"hello\n")
# 	print(f'I have a {animal_type},')
# 	print(f"my {animal_type}'s name is {pet_name.title()}.")

# describe_ani('dog', 'Stro')


# #defualt values
# def describe_animal(animal_species = 'dog', pet_name = 'jock'):
# 	print(f'I have a {animal_species},')
# 	print(f"my {animal_species}'s name is {pet_name.title()}.")

# describe_animal()


#example of optional arguement
def get_customer_name(first_name, last_name, middle_name = ''):
	if middle_name:
		full_name = f'{first_name} {last_name} {middle_name}'
	else:
		full_name = f'{first_name} {middle_name} {last_name}'

	return full_name.title()

customer = get_customer_name('ben', 'stiller')
print(customer)
customer = get_customer_name('ryan', 'benjamin', 'reynolds')
print(customer)


