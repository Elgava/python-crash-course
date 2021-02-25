#making for loops
cars = ['ford', 'golf', 'renault', 'toyota', 'lexus']
for car in cars:
	print(f"{car.title()} is such a good car\n")

print("i will get these cars\n")

#for loops with numbers
for value in range(1, 11):
	print(value)

#(list) built in function in python, to create lists
#for loop with list function
numbers = list(range(1, 6))
for num in numbers:
	print(num)

#for loop with even numbers
E_numbers = list(range(2, 11, 2))
print(E_numbers)

EV_numbers= list(range(2, 103, 2))
for e_num in EV_numbers:
	print(f"\n{e_num}") #do not print EV_numbers, print the variable aka e_num

#for loop with squares
squares = []
for value in range(1, 11):
	square = value ** 3
	squares.append(square)
print(squares)

#min, max and sum
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1]
print(f"{min(nums)}\n")
print(f"{max(nums)}\n")
print(f"{sum(nums)}\n")	

#slicing a list
games = ['fortnite', 'COD WZ', 'COD CW', 'COD BO2']
print(games[2:4])#start: 1 after ending
print(games[0:])#dont add end to finish
print(games[-3:])#takes the last 3 only, (count backwards)

print("best games in random order:\n")
for game in games[-2:]:#slicing the last 2 games
	print(f"\t{game.title()}\n")

#food list (learning to copy lists)
food_list = ["pizza", "mac n cheese", "burgers", "steak"]#making a list
friend_food = food_list[:]#copying list

print("my fave food are:")
print(f"{food_list}")

print(f"\nMy friends fave food is:")
print(f"{friend_food}")


food_list.append('brocs')
friend_food.append('cauli')
print(food_list)
print(friend_food)


#try it yourself for loops

#4-1 printing name of pizza
pizzas = ['pepperoni', 'BBQ Chicken', 'jalapeno']
for pizza in pizzas:
	print(f"\nI like {pizza}")
print("on a scale of 1 to 10, i would give pizza a 8 on the scale")

#4-2 animals
pets = ['dogs', 'cats', 'hamster']
for pet in pets:
	print(f"\n A {pet} would make a grwat pet")
print("\nany of these animals would make great pets")

#4-3 counting to twenty
count = range(1, 21)
for numb in count:
	print(numb)

#4-4 one to one milion
counts = range(1, 1_000_001)
for cnt in counts:
	print(cnt)

#4-5 summing a million
print(f"{min(counts)}\n")
print(f"{max(counts)}\n")
print(f"{sum(counts)}\n")

#4-6 off numbers
O_numbers= range(1, 20, 2)
for O_num in O_numbers:
	print(f"\n{O_num}")

#4-7 threes
threes = range(3,30, 3)
for three in threes:
	print(f"\n{three}")

#4-8 cubes
cubes = []
for values in range(1, 31):
	cube = values ** 3
	cubes.append(cube)
print(cubes)

#4-9 cube comprehension
cube_comp = [valus** 3 for valus in range(1,11)]
print(cube_comp)

#4-10
games = ['fortnite', 'COD WZ', 'COD CW', 'COD BO2', 'COD MW']
print(f"the first three items in teh list are:")
print(games[1:4])

print(f"the middle three items of the last are:")
print(games[2:5])

print(f"last three itemson the list are:")
print(games[-3:])

#4-11 my pizza, your pizza
friend_pizza = pizzas[:]
pizzas.append('anchovies')
friend_pizza.append('sweet chilli')
print(friend_pizza)
print(pizzas)

#4-12
