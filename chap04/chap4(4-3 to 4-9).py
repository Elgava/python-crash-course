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