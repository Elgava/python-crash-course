#5-1 condition test
car = 'subaru'
print("is the car a 'subaru'? i predict true.")	
print (car == 'subaru')

car = 'audi'
print("\nis this car an 'audi'? i predict false")
print (car != 'audi')

name = 'peterson'
print("\nis this persons name and 'peterson'? i predict true")
print (car == 'peterson')

car = 'peterson'
print("\nis this persons name 'peterson'? i predict false")
print (car != 'peterson')

car_model = 'R32'
print("\nis this car an 'audi'? i predict false")
print (car_model == 'audi')

car_model = 'R32'
print("\nis this car a 'Golf R32'? i predict true")
print (car_model == 'R32')

computer = 'dell'
print("\nis this computer a 'dell'? i predict true")
print (car == 'dell')

computer = 'dell'
print("\nis this computer a 'dell'? i predict true")
print (car != 'dell')

dog = 'poodle'
print("\nis this dog a 'poodle'? i predict false")
print (car == 'poodle')

dog = 'poodle'
print("\nis this dog a 'poodle'? i predict false")
print (car != 'poodle')

#5-2 more condition tests
names = 'jack'
print("this persons name is jack")
print(names == 'jack')

print("this persons name is jack")
print(names == 'john') 

print("this mans name is jack")
print(names.lower() == 'jack')

print("this mans name is jack")
print(names.lower() == 'JACK')

number = 12
numbeer2 = 19
number3 = 12
print(f'{number} is the same as {numbeer2}')
print(number == numbeer2)

print(f'{number} is the same as {number3}')
print(number == number3)

print(f'{number} is greater than {numbeer2}')
print(number > numbeer2)

print(f'{number} is greater than {numbeer2}')
print(number < numbeer2)

print(f'{number} is greater than or equal to {numbeer2}')
print(number >= numbeer2)

print(f'{number} is smaller than or equal to {numbeer2}')
print(number <= numbeer2)

age = 17
age1 = 19
age2= 21

print(f'{age} is the same as {age1} or {age} is the same as {age2}')
print(age == age1 or age == age2)

print(f'{age} is amaller than {age1} and {age} is smaller than {age2}')
print(age < age1 and age < age2)

dog_names = ['lilo', 'astro', 'snowy']

print(f'{dog_names[0]} is still in the yard')
print('lilo' in dog_names)

print('jock is still in the yard')
print ('jock' in dog_names)

