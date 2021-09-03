import numpy as np
import matplotlib.pyplot as plt

scale = 3
u = np.matrix([[1, 0, 0],
               [0, 0, 0],
               [0, 0, 0]])
v = np.matrix([[0, 0, 0],
               [0, 1, 0],
               [0, 0, 0]])
w = np.matrix([[0, 0, 0],
               [0, 0, 0],
               [0, 0, 1]])

u = u*scale
v = v*scale
w = w*scale

fig = plt.figure()
ax = plt.axes(projection = '3d')

ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.set_zlim([-5,5])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


origin = [0,0,0]
ax.quiver(origin[0],origin[1],origin[2],u[0],u[1],u[2], color = 'r')
ax.quiver(origin[0],origin[1],origin[2],v[0],v[1],v[2], color = 'g')
ax.quiver(origin[0],origin[1],origin[2],w[0],w[1],w[2], color = 'b')
plt.show()
