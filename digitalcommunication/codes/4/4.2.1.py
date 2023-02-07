import numpy as np
import matplotlib.pyplot as plt
#Set parameters for simulation

min_gamma = 0
max_gamma = 10
num_samples = 1000000
#Initialize arrays to store results

prob_error_num = []
prob_error_th = []
gamma_db = np.arange(min_gamma, max_gamma + 1)
#Simulate and calculate probability of error for each value of gamma

for i in gamma_db:
	gamma = 10**(0.1*i)
	A_samples = np.random.rayleigh(scale=(gamma/2)**0.5, size=num_samples)
	N_samples = np.random.normal(size=num_samples)
	X_samples = A_samples + N_samples
	X_samples_1 = A_samples[A_samples > 0] + N_samples[A_samples > 0]
	prob_error_num.append(np.count_nonzero(X_samples_1 < 0)/X_samples_1.shape[0])
	prob_error_th.append(0.5-0.5*np.sqrt(gamma)/np.sqrt(2+gamma))
#Plot results

plt.semilogy(gamma_db, prob_error_num, 'o')
plt.semilogy(gamma_db, prob_error_th)
plt.grid()
plt.xlabel('$\gamma$ (dB)')
plt.ylabel('$P_e(\gamma)$')
plt.legend(["Simulated","Theory"])
plt.savefig('4.2.1.pdf')
plt.show()
