import numpy as np
import matplotlib.pyplot as plt

scale = 4 
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


def Rx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, np.cos(theta),-np.sin(theta)],
                   [ 0, np.sin(theta), np.cos(theta)]])
  
def Ry(theta):
  return np.matrix([[ np.cos(theta), 0, np.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-np.sin(theta), 0, np.cos(theta)]])
  
def Rz(theta):
  return np.matrix([[ np.cos(theta), -np.sin(theta), 0 ],
                   [ np.sin(theta), np.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])

def d2r(deg):
  return (deg*np.pi)/180

R = Rz(d2r(90))*Ry(d2r(89))*Rx(d2r(90)) #Fixed Angle order
#R = Rz(d2r(0))*Ry(d2r(0))*Rx(d2r(0))
#R = Rx(d2r(90))*Ry(d2r(90))*Rz(d2r(90)) #Euler Angle order
u2 = np.dot(R,u)
v2 = np.dot(R,v)
w2 = np.dot(R,w)

fig = plt.figure()
ax = plt.axes(projection = '3d')

ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.set_zlim([-5,5])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


origin = [0,0,0]
ax.quiver(origin[0],origin[1],origin[2],u[0],u[1],u[2], color = 'r',linestyle = 'dashed')
ax.quiver(origin[0],origin[1],origin[2],v[0],v[1],v[2], color = 'g',linestyle = 'dashed')
ax.quiver(origin[0],origin[1],origin[2],w[0],w[1],w[2], color = 'b',linestyle = 'dashed')
ax.quiver(origin[0],origin[1],origin[2],u2[0],u2[1],u2[2], color = 'r')
ax.quiver(origin[0],origin[1],origin[2],v2[0],v2[1],v2[2], color = 'g')
ax.quiver(origin[0],origin[1],origin[2],w2[0],w2[1],w2[2], color = 'b')
plt.show()
