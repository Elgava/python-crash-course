import random

health = 50
difficulty = 1

potion_health = int(random.randint(25, 50) / difficulty)

health = potion_health + health

print(health)
