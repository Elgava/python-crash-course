import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(0,10)
y = 0.05*x*x
#Y1 = 0.05*x*x
#Y2 = 0.03*x*x

plt.ylim(0, 5)
plt.plot(x, y)
#plt.plot(x, Y2, color='red')
#plt.fill_between(x, Y1, Y2, color='red', alpha=0.5)
plt.fill_between (x, y, color = 'blue', alpha =0.5)
plt.show()