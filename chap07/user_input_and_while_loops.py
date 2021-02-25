message = input("Tell me something, and I will repeat it back to you: ")
print("enter your name or enter 'p' to exit")
print(message)
name = input("Please enter your name: ")

while message != 'quit':
	
	print(f"\nHello, {name}!")
	if name == 'p':
		break

# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

#modulo