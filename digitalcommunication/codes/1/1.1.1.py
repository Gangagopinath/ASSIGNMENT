import numpy as np
import matplotlib.pyplot as plt

simlen = 10000
dice_outcomes = np.arange(2, 13)

y = np.random.randint(1, 7, size=(2, simlen))
X = np.sum(y, axis=0)

unique, counts = np.unique(X, return_counts=True)
simulated_prob = counts/simlen

theoretical_prob = np.zeros(11)
for i in range(2, 13):
    theoretical_prob[i-2] = (6-abs(7-i))/36

plt.stem(dice_outcomes, simulated_prob, markerfmt='o', label='Simulation')
plt.stem(dice_outcomes, theoretical_prob, markerfmt='o', label='Theory')
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.legend()
plt.grid()
plt.savefig('./1.1.1.pdf')
plt.show()
