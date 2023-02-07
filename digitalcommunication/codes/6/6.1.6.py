import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf, erfc
def qfunc(x):
    return 0.5 * erfc(x / np.sqrt(2))

# Define the number of SNR samples
snr_len = 10
# Define the SNR values in dB
snr_db = np.linspace(0, 9, snr_len)
# Define the number of samples
sim_len = int(1e5)
# Declare an array to store the simulated BER
sim_ber = []
# Declare an array to store the analytical BER
ana_ber = []

# Iterate over the SNR range
for i in range(snr_len):
    # Generate additive white Gaussian noise with 0 mean and unit variance
    noise = np.random.normal(0, 1, sim_len)
    # Convert the SNR from dB to linear scale
    snr = 10**(0.1 * snr_db[i])
    # Calculate the received signal in baseband
    rx = np.sqrt(snr) + noise
    # Count the number of errors
    num_err = np.count_nonzero(rx < 0)
    # Calculate the simulated BER
    sim_ber.append(num_err / sim_len)
    # Calculate the analytical BER
    ana_ber.append(qfunc(np.sqrt(snr)))

# Plot the simulated and analytical BER on a semilog plot
plt.semilogy(snr_db, sim_ber, label='Simulation')
plt.semilogy(snr_db, ana_ber, '*', label='Analysis')
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.legend()
plt.grid()
plt.savefig('./6.1.6.pdf')
plt.show()
