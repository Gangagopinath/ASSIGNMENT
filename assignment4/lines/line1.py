
#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/home/ganga/matrix/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
A = np.array(([1,-3],[1,-2]))
b = np.array(([3,13]))
e1 = np.array(([1,0]))
n1 = A[0,:]
n2 = A[1,:]
c1 = b[0]
c2 = b[1]


#Solution vector
x = LA.solve(A,b)
print(x)
