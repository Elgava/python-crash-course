import matplotlib.pyplot as plt 

plt.style.use('ggplot')
print(plt.style.available)

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

plt.bar(x1, y1)
plt.title("title")
plt.xlabel('horizontal title')
plt.ylabel('Vertical title')
plt.show()


import matplotlib.pyplot as plt 
import seaborn as sns

sns.set_style("darkgrid")

x = [1,2,3,4, 5, 6, 7, 8]
y=  [2,4,6,8, 7, 5, 3, 2]

plt.plot(x, y, 'r-o', linewidth  = 2.0)
plt.axis([0,10,0,10])
plt.xlabel("horizontal title")
plt.ylabel("vertical title")
plt.title("title")
plt.show()