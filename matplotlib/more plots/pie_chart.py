import matplotlib.pyplot as plt 

values = [16,18,4,8]
pielabels = ['Python', 'Ruby', 'Java', 'Perl']
piecolors = ['red', 'blue', 'purple', 'lightblue']
pieexplode = [0.1,0.1,0.1,0.1]

plt.pie(values, labels=pielabels, startangle= 0, shadow = 4, colors=piecolors, explode=pieexplode)
plt.title('pie chart')
plt.xlabel("Horizontal title")
plt.ylabel("Vertical title")
plt.legend(loc='best')
plt.show()