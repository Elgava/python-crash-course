#6-7 people
people = {
'emal': {
'first name': 'elgin',
'last name': 'malouw',
'location': 'midrand',
},
'dmal': {
'first name': 'dylan',
'last name': 'malouw',
'location': 'midrand',
},
}

for username, user_info in people.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first name']} {user_info['last name']}"
	location = user_info['location']
	print(f"Full name: {full_name.title()}")
	print(f"Location: {location.title()}")

#6-8 pets
