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