import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *


import sys                                          #for path to external scripts
sys.path.insert(0,'/home/ganga/matrix/CoordGeo')       #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

def p(l):
	return  280+180*(l+4/l)


#Gradient Descent
cur_p = .5# The algorithm starts at x=2
gamma = 0.001 # step size multiplier
precision = 0.00000001
learn_rate = 1 #step s
max_iters = 100000000 # maximum number of iterations
iters = 0 #iteration counter

df = lambda l: 180*(1-4/l**2)


while (learn_rate > precision) & (iters < max_iters):
    prev_p = cur_p
    cur_p -= gamma * df(prev_p)
    previous_step_size = abs(cur_p - prev_p)
    iters+=1
min_val=p(cur_p,)
print("Minimum value of f(p) is ", min_val, "at","l =",cur_p)

label_str = "$4p^3 - 22p^2 + 24p$"
#Plotting f(x)
x=np.linspace(0.1,10,100)
y=p(x)
plt.plot(x,y)
#Labelling points
plt.plot(cur_p,min_val,'o')


plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
#plt.legend()

#if using termux
plt.savefig('/home/ganga/matrix/figs/opt1.pdf')  
#subprocess.run(shlex.split("termux-open /sdcard/Download/matrice/opt/opt1.pdf"))
#else
plt.show() 
