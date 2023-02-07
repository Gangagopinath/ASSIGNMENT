import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

maxrange=50
maxlim=3.0
minlim=-1.0
# Define the range of x values
x = np.linspace(minlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
randvar = np.loadtxt('tri.dat',dtype='double') 

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	

pdf = np.gradient(err, x, edge_order=2)

# Calculate the PDF for a triangular distribution with a=0, b=1, c=2
#pdft = np.where(x < 0, 0, np.where(x < 1, x, np.where(x < 2, 2 - x, 0)))	
plt.plot(x,pdf,'o')             # plotting estimated PDF
#plt.plot(x,pdft)    # plotting theoretical PDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('./figs/tri_pdf.pdf')

plt.show()

