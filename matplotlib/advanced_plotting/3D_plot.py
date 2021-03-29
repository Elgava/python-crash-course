import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection= '3d')

x1 = np.random.rand(10)
y1 = np.random.rand(10)
z1 = np.random.rand(10)

x2 = np.random.rand(10)
y2 = np.random.rand(10)
z2 = np.random.rand(10)

ax.scatter(x1,y1,z1, s=20, color = 'blue', marker='o')
ax.scatter(x1,y1,z1, s=20, color = 'red', marker='^')

plt.show()


import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection= '3d')

x = [1,2,3,4,5,6,7]
y = [1,1,1,1,1,1,1]
z = [2,4,6,8,10,12,14]

x2 = [0,1,2,3,4,5,6]
y2 = [1,1,1,1,1,1,1]
z2 = [1,3,5,7,9,11,13]

ax.plot(x,y,z, color='blue')
ax.plot(x2, y2, z2, color = 'red')

plt.show()