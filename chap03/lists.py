#making lists, same as saying an array
bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles)

print (f"my first bicycle was {bicycles[2]}")

#making a list
motorcycles = ['Honda', 'yamaha', 'suzuki']
print (motorcycles)

#modifying the list(add to end)
motorcycles.append('ducati')
print(motorcycles)

#modifying the list(insert into)
motorcycles.insert(1, 'ducati')
print(motorcycles)

#modifying a list(removing)
del motorcycles[2]
print (motorcycles)

#modifying a list(pop method to rmeove but keep a value)
popped_motorcycles = motorcycles.pop()
print (motorcycles)
print(popped_motorcycles)

#modifying a list(pop from any position)
first_saw = motorcycles.pop(1)
print(motorcycles)
print(f"first motorcycle ive seen up close is a {first_saw}")


