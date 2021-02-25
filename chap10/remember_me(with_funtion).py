import json

def get_stored_username():
	filename = 'username,json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return none
	else:
		return username

def get_new_username():
	userName = input("what is your name? ")
	fileName = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"We'll remember you when you come back, {username}!")
	else:
		print(f"Welcome back, {username}!")

greet_user()



# import json
# def get_stored_username():
# 	username = input("what is your name?")
# 	filename = 'username.json'
# 	with open(filename, 'w') as f:
# 		json.dump(username, f)
# 	return username

# def greet_user():
# 	username = get_stored_username()
# 	if username:
# 		print(f'welcome back, {username}')
# 	else:
# 		print(f"we'll remember you when you come back, {username}")
# greet_user()
		