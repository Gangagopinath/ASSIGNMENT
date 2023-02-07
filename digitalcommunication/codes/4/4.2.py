import numpy as np
import matplotlib.pyplot as plt

# Define range of gamma values
gamma_range = np.linspace(0, 10, 100)

# Define conditional probability function
def Pe(gamma):
    A = np.random.rayleigh(np.sqrt(gamma))
    N = np.random.normal(0, 1, 10000)
    X = 1
    X_hat = A*X + N
    return np.mean(X_hat == -1)

# Calculate conditional probability for each gamma value
pe_values = [Pe(gamma) for gamma in gamma_range]

# Plot the results
plt.plot(gamma_range, pe_values)
plt.xlabel('Gamma (dB)')
plt.ylabel('Conditional Probability Pe')
plt.savefig('4.2.1.pdf')
plt.show()

