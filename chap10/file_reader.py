# open aan dread files
with open('text folder/numbers.txt') as file_object:
	contents = file_object.read()
	print(contents)
print(f'\n{contents.rstrip()}\n')
print(f'{contents.lstrip()}\n')

# file_path = 'text folder/numbers.txt'
# with open(file_path) as file_object:
# 	contents = file_object.read()
# print(contents)

# read line by line
# file_path = 'text folder/numbers.txt'
# with open(file_path) as file_object:
# 	for line in file_object:
# 		print(line)


# file_path = 'text folder/numbers.txt'
# with open(file_path) as file_object:
# 	for line in file_object:
# pi_string = ''
# for line in file_object:
# 	pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))

