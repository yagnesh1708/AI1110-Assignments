#AKKASANI YAGNESH REDDY
#CS21BTECH11003
#ICSE 12 2019 question 16 a



import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


#generating points for plotting vectors
 


#vector a given a=i-2j+3k

a=np.array([1,-2,3])

#vector b given b=2i+3j-5k

b=np.array([2,3,-5])

#origin

o=np.array([0,0,0])

fig=plt.figure()
ax=plt.axes(projection='3d')

ax.set_xlim([-10,10])
ax.set_ylim([-10,15])
ax.set_zlim([-10,15])

# plotting aXb
axb=np.cross(a,b)

#plotting vectors 

ax.quiver(o[0],o[1],o[2],a[0],a[1],a[2],color='r')
ax.quiver(o[0],o[1],o[2],b[0],b[1],b[2],color='b')
ax.quiver(o[0],o[1],o[2],axb[0],axb[1],axb[2],color='g')
plt.grid()
plt.show()
   

#dot product of a and axbn and verification of angle

a_dot_axb=a @ axb

if(a_dot_axb==0):
    print('both are perpendicular and hence verified')
else:
    print('not perpendicular') 

    

