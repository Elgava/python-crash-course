# def get_formatted_name(First, last):
# 	fullName = f"{First} {last}"
# 	return fullName.title()

# while True:
# 		print("\nPlease tell me your name:")
# 		print("enter P to quit")
# 		f_name = input("First name:")
# 		# if f_name == 'p':
# 		# 	break
# 		l_name = input("last name:")
# 		if l_name or s_name == 'p':
# 			break
# 		formatted_name = get_formatted_name(f_name, l_name)
# 		print(f"Hello, {formatted_name}!")

#passing a list
# def greet_users(names):

# 	for name in names:
# 		msg = f"\nHello, {name.title()}!"
# 		print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

#modifying a list witha function
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
# 	current_design = unprinted_designs.pop()
# 	print(f"Printing model: {current_design}")
# 	completed_models.append(current_design)
# 	# Display all completed models.
# 	print("\nThe following models have been printed:")
# for completed_model in completed_models:
# 	print(completed_model)


#using arbitrary keyword arguments page 214
def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
	
user_profile = build_profile('albert', 'einstein',
		location='princeton',
		field='physics')

print(user_profile)