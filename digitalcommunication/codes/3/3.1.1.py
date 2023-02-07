import numpy as np
import matplotlib.pyplot as plt
import random

def generate_equiprobable_bpsk(n):
    symbols = []
    for i in range(n):
        random_number = random.random()
        if random_number > 0.5:
            symbols.append(1)
        else:
            symbols.append(-1)
    return symbols

# Generate 10 equiprobable symbols
print(generate_equiprobable_bpsk(10))
