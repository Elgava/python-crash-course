X = []
Y = []

with open('text.txt', 'r') as file:
	for line in file:
		Y.append( int(line) )

X = list(range(0, len(Y)+1))
print(X)
print(Y)