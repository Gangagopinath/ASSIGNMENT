import numpy as np
import matplotlib.pyplot as plt

# Sample size
simlen = 10000
# Possible outcomes
n = range(2,13)
# Generate X1 and X2
y = np.random.randint(1,7, size=(2, simlen))
# Sum of X1 and X2
X = np.sum(y, axis=0)
# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
# Simulated probability
psim = counts/simlen
# Theoretical probability
n1 = range(2,8)
n2 = range(8,13)
panal1 = (n1 - np.ones((1,6)))
panal2 = (13*np.ones((1,5)) - n2)
panal = np.concatenate((panal1, panal2), axis=None)/36

# Z-transform
ts = np.arange(1,12,1)
panal_z = np.zeros(11)
for i, n_i in enumerate(n):
    for t in ts:
        if t == 1:
            panal_z[i] += (n_i-1)/36
        elif t == 7:
            panal_z[i] -= 2*(n_i-7)/36
        elif t == 13:
            panal_z[i] += (n_i-13)/36

# Plotting
plt.stem(n, psim, markerfmt='o', label='Simulation')
plt.stem(n, panal, markerfmt='o', label='Analysis')
plt.xlabel('n')
plt.ylabel('p_X(n)')
plt.legend()
plt.grid()
plt.savefig('./1.1.3.pdf')
plt.show()
