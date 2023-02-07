import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

gamma_dB = np.linspace(0, 10, 11)

def Pe(x):
    return 0.5 - 0.5 * (math.sqrt(x / (2 + x)))

vect_Pe = [Pe(10 ** (0.1 * x)) for x in gamma_dB]

sim_len = int(1e5)
N = np.random.normal(0, 1, sim_len)

prob = []
for gamma_dB_value in gamma_dB:
    gamma = 10 ** (0.1 * gamma_dB_value)
    A = np.random.rayleigh(scale=math.sqrt(gamma / 2), size=sim_len)
    below_zero = np.sum(A + N < 0)
    prob_sum = below_zero / sim_len
    prob.append(prob_sum)

plt.semilogy(gamma_dB, vect_Pe, '-')
plt.semilogy(gamma_dB, prob, 'o')
plt.xlabel(r'$\gamma$ in dB')
plt.ylabel(r'$P_e(\gamma)$')
plt.legend(["Theoretical", "Simulated"])
plt.grid()
plt.savefig('./4.2.4.pdf')
plt.show()
