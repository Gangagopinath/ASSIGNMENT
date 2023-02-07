import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Generate samples of X1 and X2
simlen = int(1e7) # number of samples
randvar1 = np.random.normal(0,1,simlen)
randvar2 = np.random.normal(0,1,simlen)

# Compute V for each sample
v = randvar1**2 + randvar2**2

# Plot the CDF
plt.figure(figsize=(10,5))
x = np.linspace(0, 20, 50)
err = []
for i in range(0,50):
    err_ind = np.nonzero(v < x[i])
    err_n = np.size(err_ind)
    err.append(err_n/simlen)
plt.plot(x, err, marker='o', label='Simulation')
plt.plot(x, chi2.cdf(x, df=2), label='Theory')
plt.xlabel('x')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function of V')
plt.legend()

# Plot the PDF
plt.figure(figsize=(10,5))
plt.hist(v, bins=100, density=True, label='Simulation',histtype='step')
plt.plot(x, chi2.pdf(x, df=2), label='Theory')
plt.xlabel('x')
plt.ylabel('PDF')
plt.title('Probability Density Function of V')
plt.legend()
plt.show()

