import matplotlib.pyplot as plt
import numpy as np

#AKKASANI YAGNESH REDDY
#cs21btech1103

 # Question 11c


# As in the given question results does not change with radius lets
# assume radius to be 1 for simplicity 

fig,axes=plt.subplots(1)

axes.set_aspect(1)

#plotting circle

a=np.linspace(0,2*np.pi,1001)

x=np.cos(a)
y=np.sin(a)

axes.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')


O=[0,0]
A=[-1,0]
C=[1,0]
B=[-np.cos(4*np.pi/9),-np.sin(4*np.pi/9)]
E=[np.cos(4*np.pi/9),np.sin(4*np.pi/9)]
D=[np.cos(2*np.pi/9),np.sin(2*np.pi/9)]


#plotting points

axes.scatter(O[0],O[1])
axes.scatter(A[0],A[1])
axes.scatter(B[0],B[1])
axes.scatter(C[0],C[1])
axes.scatter(D[0],D[1])
axes.scatter(E[0],E[1])


#notating points


axes.text(O[0]+0.05,O[1]+0.05,'O')
axes.text(A[0]+0.05,A[1]+0.05,'A')
axes.text(B[0]+0.05,B[1]+0.05,'B')
axes.text(C[0]+0.05,C[1]+0.05,'C')
axes.text(E[0]+0.05,E[1]+0.05,'E')
axes.text(D[0]+0.05,D[1]+0.05,'D')


#plotting lines

axes.plot([O[0],A[0]],[O[1],A[1]],'b-')
axes.plot([O[0],C[0]],[O[1],C[1]],'b-')
axes.plot([O[0],B[0]],[O[1],B[1]],'b-')
axes.plot([O[0],E[0]],[O[1],E[1]],'b-')
axes.plot([B[0],A[0]],[B[1],A[1]],'b-')
axes.plot([E[0],A[0]],[E[1],A[1]],'b-')
axes.plot([B[0],C[0]],[B[1],C[1]],'b-')
axes.plot([C[0],D[0]],[C[1],D[1]],'b-')
axes.plot([E[0],D[0]],[E[1],D[1]],'b-')


plt.grid()
plt.show()





