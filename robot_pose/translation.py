import numpy as np
import matplotlib.pyplot as plt

scale = 2
u = np.matrix([[1],
               [0],
               [0]])
v = np.matrix([[0],
               [1],
               [0]])
w = np.matrix([[0],
               [0],
               [1]])

u = u*scale
v = v*scale
w = w*scale
origin = np.matrix([[0],[0],[0]])
t = np.matrix([ [2],
                [1],
                [3]])
dx = np.matrix([[t[0,0]],[0],[0]])
dy = np.matrix([[0],[t[1,0]],[0]])
dz = np.matrix([[0],[0],[t[2,0]]])

u2 = u+dx
v2 = v+dy
w2 = w+dz

origin2 = origin+t
print("new origin",origin2)
print("t00",t[0,0])
print("u",u)
print("u2",u2)

fig = plt.figure()
ax = plt.axes(projection = '3d')

ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.set_zlim([-5,5])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')




ax.quiver(origin[0],origin[1],origin[2],u[0],u[1],u[2], color = 'r',linestyle = 'dashed')
ax.quiver(origin[0],origin[1],origin[2],v[0],v[1],v[2], color = 'g',linestyle = 'dashed')
ax.quiver(origin[0],origin[1],origin[2],w[0],w[1],w[2], color = 'b',linestyle = 'dashed')
ax.quiver(origin2[0],origin2[1],origin2[2],u2[0],u2[1],u2[2], color = 'r')
ax.quiver(origin2[0],origin2[1],origin2[2],v2[0],v2[1],v2[2], color = 'g')
ax.quiver(origin2[0],origin2[1],origin2[2],w2[0],w2[1],w2[2], color = 'b')
plt.show()
