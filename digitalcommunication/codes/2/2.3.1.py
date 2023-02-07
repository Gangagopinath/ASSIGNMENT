import numpy as np
import matplotlib.pyplot as plt

# Loading the data from file
V = np.loadtxt('v.dat')

# Defining the ecdf function
def ecdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n+1) / n
    return x, y

# Plotting the cumulative distribution function of V
x, y = ecdf(V)
plt.plot(x, y, marker='.', linestyle='none', label='Simulation')
plt.grid(True)
v = np.linspace(0, 15, 100)
plt.plot(v, 1 - np.exp(-v/2), label='Analysis')
plt.title("CDF of random variable V")
plt.xlabel("v")
plt.ylabel("F_V(v)")
plt.legend(loc='best')
plt.savefig('2.3.1.pdf')
plt.show()
