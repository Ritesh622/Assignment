import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

##ax.plot(1,2,3,label='Given Point')


ax.plot([-1, 5], # x
        [1, 7], # y
        [-1, 1],label=" Line 1") # z
ax.plot([0, 4], # x
       [4, 0], # y
     [-1, 1],label=" Line 2") # z
ax.legend()
plt.show()
Axes3D.plot()
plt.savefig("intersection of lines.png")
