import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar1 = np.random.normal(0,1,simlen)
randvar2= np.random.normal (0,1,simlen)

V = randvar1**2 + randvar2**2
A = np.sqrt(V)
pdf = np.zeros(100)
for i in range(0,100):
    err_ind = np.nonzero(A < x[i]) #checking probability condition
    err_n = np.size(err_ind) #computing the probability
    err.append(err_n/simlen) #storing the probability values in a list
    pdf[i] = (np.sum(A < x[i]) - np.sum(A < x[i-1])) / (simlen * (x[i]-x[i-1]))
    
plt.plot(x.T, err ,marker='o')#plotting the CDF
plt.xlabel('$A$')
plt.ylabel('$F_A(A)$')
plt.title('CDF of A')
plt.grid() #creating the grid
plt.savefig('./4.1.3c.pdf')
plt.show()

plt.plot(x, pdf)
plt.xlabel('$A$')
plt.ylabel('$p_A(A)$')
plt.title('PDF of A')
plt.grid()
plt.savefig('./4.1.3p.pdf')
plt.show()

