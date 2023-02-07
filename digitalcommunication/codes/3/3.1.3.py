import random
import numpy as np
import matplotlib.pyplot as plt
def generate_equiprobable_bpsk(n):
    symbols = []
    for i in range(n):
        random_number = random.random()
        if random_number > 0.5:
            symbols.append(1)
        else:
            symbols.append(-1)
    return symbols

def generate_received_signal(symbols, A_dB):
    A = 10**(A_dB/10)
    Y = []
    for i in range(len(symbols)):
        noise = random.gauss(0, 1)
        y = A*symbols[i] + noise
        Y.append(y)
    return Y

X = generate_equiprobable_bpsk(1000)
Y = generate_received_signal(X, 5)
plt.scatter(range(len(Y)), Y)
plt.xlabel('Symbol Index')
plt.ylabel('Received Signal')
plt.title('scatter plot of Y')
plt.savefig('./3.1.3.pdf')
plt.show()
