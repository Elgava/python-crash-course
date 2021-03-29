import matplotlib.pyplot as plt 

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

colors = ['green', 'red', 'blue', 'orange', 'lightgreen']

plt.bar(x1, y1, edgecolor='black', color = colors, linewidth = 3)
plt.title("title")
plt.xlabel("horizontal title")
plt.ylabel("vertical title")
plt.show()