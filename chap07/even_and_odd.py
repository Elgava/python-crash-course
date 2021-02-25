active = True
while active:
	number = input("\nEnter a number, and I'll tell you if it's even or odd \nEnter '0' to end the program: ")
	numbers = int(number)
	if number == '0':
		 active = False
	elif numbers % 2 == 0:
		print(f"\nThe number {number} is even.")
	elif numbers % 2 == 1: 
		print(f"\nThe number {number} is odd.")
	
		
# current_number = 1
# while current_number <= 5:
# 	print(current_number)
# current_number += 1

# using a flag
# number_2 = ("Enter a number")
# active = True
# while active:
# 	if int(number_2) % 2 == 0:
# 		print(f'\nThe number {number_2} is even')

# 	else:
# 		print(f"\nThe number {number_2} is odd")	


# number = "\nenter a number and ill tell you if its even or odd."
# number += "\nenter '-1' to end the program"
# message = ""

# while messsage != '-1':
# 	message = input(number)
# 	message = int(message)
# 	if number %2 == 0:
# 		print (f"\nthe number {number} is even")
# 	else:
# 		print(f"\nthe number {number} is odd")	