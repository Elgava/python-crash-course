import matplotlib.pyplot as plt 

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

plt.plot(x1, y1, 'r-o', label="students", color = 'purple')
plt.legend(loc='best')
plt.title("your title")
plt.xlabel('horizantal title')
plt.ylabel('vertical title')
#plt.grid(linewidth= 0.5, axis='y', which= 'major', linestyle = '-.', color = 'black')
plt.grid(which= 'major', linestyle = '-.', color = 'black')
plt.minorticks_on()
plt.grid(which = 'minor', linestyle= '--', color='darkblue', alpha = 0.2)
plt.show()