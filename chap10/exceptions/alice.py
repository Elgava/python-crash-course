def count_words(filename):
	filename = 'alice.txt'
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
		else:
			words = contents.split()
			num_words = len(words)
			print(f"The file {filename} has about {num_words} words.") 
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
count_words(filename)

# 	Count the approximate number of words in the file.file_path = 'text folder/numbers.txt'
# with open(file_path) as file_object:
# 	for line in file_object:

#exception for missing file
# file_name = 'alice.txt'
# try:
# 	with open(file_name, encoding='utf-8') as f:
# 		contents = f.read()
# except fileNotFoundError:
# 	print(f'sorry, teh file {file_name} does not exist.')

# filename = 'alice.txt'
# try:
# 	with open(filename, encoding='utf-8') as f:
# 		contents = f.read()
# except FileNotFoundError:
# 	print(f"Sorry, the file {filename} does not exist.")