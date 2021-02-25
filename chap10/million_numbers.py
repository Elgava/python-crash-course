file_path = 'text folder/pi_million_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
pi_string = ''
for line in contents:
	pi_string += line.strip()

print(f'{pi_string[:52]}')
print(len(pi_string))

birthday = input('enter your birhday, in the form mmddyy')
if birthday in pi_string:
	print('your birthday appears in teh first million digits of pi!')
else:
	print('your birthday does not appear in the first million digits of pi')