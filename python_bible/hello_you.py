# ask user for a name

name = input("please enter your name:")

# ask user age

age = input("how old are you?: ")

#ask user city

city = input("which city do you live in?: ")

#ask user what they enjoy

love = input("what do you enjoy doing?: ")

#create output text

string = "Your name is {} and you are {} years old. You live in {} and you enjoy {}"
output = string.format(name, age, city, love)
                       
#print output to screen
print(output)
