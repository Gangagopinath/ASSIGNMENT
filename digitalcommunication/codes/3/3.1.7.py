import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

#Number of SNR samples 
num_snr_samples = 10
#SNR values in dB
snrdb = np.linspace(0,9,10)
#Number of samples
num_samples = int(1e5)
#Simulated BER declaration
sim_ber = []
#Analytical BER declaration
ana_ber = []

#for SNR 0 to 10 dB
for i in range(0,num_snr_samples):
    #Generating AWGN, 0 mean unit variance
    noise = np.random.normal(0, 1,num_samples)
    #from dB to actual SNR
    snr = 10**(0.1*snrdb[i])
    #Received symbol in baseband
    rx = np.sqrt(snr) + noise
    #storing the index for the received symbol 
    #in error
    err_ind = np.where(rx < 0)
    #calculating the total number of errors
    err_n = np.size(err_ind)
    #calcuating the simulated BER
    sim_ber.append(err_n/num_samples)
    #calculating the analytical BER
    ana_ber.append(0.5*erfc(np.sqrt(snr)/np.sqrt(2)))

plt.semilogy(snrdb.T,ana_ber,label='Analysis')

for i in range(num_snr_samples):
    plt.semilogy(snrdb[i],sim_ber[i],'o',color='C'+str(i),label='simu='+str(snrdb[i]))
plt.xlabel('SNR (Eb/No)')
plt.ylabel('p_e')
plt.legend()
plt.grid()
plt.savefig('./3.1.7.pdf')
plt.title('p_e vs SNR ')
plt.show()

