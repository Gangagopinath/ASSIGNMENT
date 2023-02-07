import numpy as np
import matplotlib.pyplot as plt

# Load data from file
randvar = np.loadtxt('tri.dat', dtype='double')

# Compute the CDF
x = np.linspace(-4, 4, 30)
cdf = np.array([np.count_nonzero(randvar < x_i)/randvar.size for x_i in x])

# Plot the CDF
plt.plot(x, cdf)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical"])
# Save and show the plot
plt.savefig('tri_cdf1.pdf')
plt.show()
