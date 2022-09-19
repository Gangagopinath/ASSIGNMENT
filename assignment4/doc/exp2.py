import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/ganga/matrix/CoordGeo')  

#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
#PQR
#c =14
#b=16
A=np.array([[2,-1],[1,-1])
B=np.array(([18,2]))
X=np.linalg.inv(A)@ B
theta1= np.pi/3
r=int(X[0])
P = r*np.array(([np.cos(theta1),np.sin(theta1)]))
Q = np.array(([0,0]))
R = np.array(([6,0]))
#Distance between P&R and P&Q
d1 = np.linalg.norm(P-R)
d2 = np.linalg.norm(P-Q)
d3 = d2-d1
print(d3)




##Generating all lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)


#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:])#,label='$Diameter$')
plt.plot(x_QR[0,:],x_QR[1,:])#,label='$Diameter$')
plt.plot(x_RP[0,:],x_RP[1,:])#,label='$Diameter$')

#Labeling the coordinates
tri_coords = np.vstack((P,Q,R)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R']

for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/home/ganga/matrix/figs/ex2.pdf')

#subprocess.run(shlex.split("/home/ganga/matrix/figs/ex2.pdf"))
#else
plt.show()










