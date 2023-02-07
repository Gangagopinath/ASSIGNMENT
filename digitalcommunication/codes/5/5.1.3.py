import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

# Function to calculate Q-function (related to error function)
def qfunc(x):
    return 0.5*mp.erfc(x/mp.sqrt(2))

# Set up range of SNR values in dB
snr_dB = np.linspace(0, 9, 10)

# Number of bits to simulate
simlen = int(1e5)

# Initialize arrays for BER values
ber_analytic = []
ber_simulated = []

# Generate two sets of normally distributed random numbers
n1 = np.random.normal(0, 1, simlen)
n2 = np.random.normal(0, 1, simlen)

# Loop over SNR values
for snr_dB_val in snr_dB:
    # Convert SNR from dB to linear scale
    snr = 10**(0.1*snr_dB_val)
    
    # Calculate received signals
    y1 = np.sqrt(2*snr) + n1
    y2 = n2
    
    # Calculate number of errors
    err_n = np.size(np.nonzero(y1 < y2))
    
    # Calculate simulated BER
    ber_sim = err_n/simlen
    
    # Calculate analytic BER
    ber_analytic.append(qfunc(np.sqrt(snr)))
    
    # Add simulated BER to list
    ber_simulated.append(ber_sim)

# Plot BER values on semi-log scale
plt.semilogy(snr_dB, ber_analytic, label='Analysis')
plt.semilogy(snr_dB, ber_simulated, 'o', label='Simulated')

# Label plot and add legend
plt.xlabel('SNR (A/sqrt(2))')
plt.ylabel('BER')
plt.legend()
plt.grid()
plt.savefig('./5.1.3.pdf')
# Show plot
plt.show()

