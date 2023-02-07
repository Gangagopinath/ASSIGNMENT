import numpy as np
import matplotlib.pyplot as plt

# Sample size
simlen = 10000

# Possible outcomes
n = range(2,13)

# Generate X1 and X2
X = np.zeros(simlen)
for i in range(simlen):
    X[i] = np.random.randint(1,7) + np.random.randint(1,7)

# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)

# Simulated probability
psim = counts/simlen

theoretical_prob = np.zeros(11)
for i in range(2, 7):
    theoretical_prob[i-2] = (i-1)/36
for i in range(8, 13):
    theoretical_prob[i-2] = (13-i)/36

# Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,theoretical_prob, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()
plt.show()
