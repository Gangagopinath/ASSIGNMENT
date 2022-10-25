import numpy as np
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp

#if using termux
import subprocess
import shlex
#end if

# ax+by <= d
A = np.array(( [3, 3], [3, 2])).T  #
B = np.array([18,15]).reshape(2,1)  #Total available Floor & Fat

# objective function coeffs
c = np.array([30,25])             
x = cp.Variable((2,1),nonneg=True)

#Cost function
f = c@x     #P = max(30 25)x
obj = cp.Maximize(f)

#Constraints
constraints = [A@x <= B]

#solution
prob = cp.Problem(obj, constraints)
prob.solve()
print("Maximun :", f.value)
print("Number of type_1 :", x.value[0])
print("Number of type_2 :", x.value[1])

x1=np.linspace(0,8,200)
#print(len(x1))
y1=(18-3*x1)/3
y2=(15-3*x1)/2
plt.plot(x1,y1,label='3x+3y=18')
plt.plot(x1,y2,label='3x+2y=15')

y4=np.zeros(len(x1))
plt.plot(x1,y4,label='y=0')
plt.plot(y4,x1,label='x=0')
plt.title('')
plt.ylim([-2,8])
# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')
plt.legend()
plt.savefig('/sdcard/download/opt/opt1.pdf')  
subprocess.run(shlex.split("termux-open /sdcard/Download/opt/opt1.pdf"))
plt.show()
