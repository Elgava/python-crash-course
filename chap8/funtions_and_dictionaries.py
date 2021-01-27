def get_formatted_name(First, last):
	fullName = f"{First} {last}"
	return fullName.title()

while True:
		print("\nPlease tell me your name:")
		print("enter P to quit")
		f_name = input("First name:")
		# if f_name == 'p':
		# 	break
		l_name = input("last name:")
		if l_name or s_name == 'p':
			break
		formatted_name = get_formatted_name(f_name, l_name)
		print(f"Hello, {formatted_name}!")

#passing a list
def greet_users(names):

	for name in names:
		msg = f"\nHello, {name.title()}!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
