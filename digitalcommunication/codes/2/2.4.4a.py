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
	
# Calculate the CDF for a triangular distribution with a=0, b=1, c=2
cdft = np.where(x < 0, 0, np.where(x < 1, x**2/2, np.where(x < 2, 2*x - x**2/2 - 1, 1)))


plt.plot(x,err,'o')     # plotting estimated CDF
plt.plot(x,cdft) 	# plotting theoretical CDF
plt.grid()          #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.savefig('./tri_cdf.pdf')
plt.show()
plt.close()


plt.show()

