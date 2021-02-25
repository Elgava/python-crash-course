#still lists

#tuples
dimensions = (200, 50)#constant value and cannot be changed
print(dimensions[0])
print(dimensions[1])

#writing over tuples
dimensions = (200, 50)
print("original dimension")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 75)
print("modified dimension")
for dimension in dimensions:
	print(dimension)

