#6-4 gloassary 2

glossary = {
	'dictionary' : 'used to store a key and a value',
	'if statement' : 'used for diferent outcomes',
	'lists':'used to store more than one value',
	'while loop':'loops infinitely until told when to stop',
	'elements':'values in an array or list'
}
for key, value in glossary.items():
	print(f'\n{key}: {value}')

#6-5 rivers
rivers = {
	'nile' : 'egypt',
	'amazon river' : 'brazil',
	'yangtze' : 'china'
}
for key, value in rivers.items():
	print(f'{key} runs through {value}')

for river in rivers.keys():
	print(f'\n{river.title()}\n')

for river in rivers.values():
	print(f'{river.title()}\n')

#6-6 polling
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'adam' : '',
'phil': 'python'
}
for name in favorite_languages.keys():
	print(name.title())
	friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		language = favorite_languages[name].title()
		

print(f"\t{name.title()}, I see you love {language}!")