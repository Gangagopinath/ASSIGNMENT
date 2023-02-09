import numpy as np
import matplotlib.pyplot as plt

# Sample size
simlen = 10000
# Possible outcomes
n = np.arange(2, 13)

# Generate X1 and X2
y = np.random.randint(1, 7, size=(2, simlen))

# Generate X
X = np.sum(y, axis=0)

# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
# Simulated probability
psim = counts / simlen

# Theoretical probability
n1 = np.arange(2, 8)
n2 = np.arange(8, 13)
panal1 = (n1 - np.ones((1, 6))) / 36
panal2 = (13 * np.ones((1, 5)) - n2) / 36
panal = np.concatenate((panal1, panal2), axis=None)

# Convolution
p_x1 = np.ones((1, 6)) / 6
p_x2 = np.ones((1, 6)) / 6
P_px = np.convolve(p_x1[0], p_x2[0])

# Plotting
plt.stem(n, psim, markerfmt='o', linefmt='C0-', label='Simulation')
plt.stem(n, P_px, markerfmt='o', linefmt='C1-', label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()
plt.savefig('./1.1.2.pdf')
plt.show()
