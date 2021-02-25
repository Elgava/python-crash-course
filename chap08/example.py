def build_profile(first, breed, **user_info):
	user_info['first name'] = first.title()
	user_info['breed'] = breed.title()
	return user_info

user_info = build_profile('jock', 'jack russel', size='medium',
health='dead')
# print(f"first name: {user_info['first name']}")
# print(f"breeed {user_info['breed']}")
# # print(f"size: {user_info}")
# # print(f"health: {user_info}")

print(user_info)