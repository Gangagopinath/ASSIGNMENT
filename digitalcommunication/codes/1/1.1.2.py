import numpy as np
import matplotlib.pyplot as plt

# Set number of simulations
num_simulations = 10000

# Create an array of possible outcomes
outcomes = np.arange(2, 13)

# Generate random rolls of two dice
dice_rolls = np.random.randint(1, 7, size=(2, num_simulations))

# Sum the dice rolls to get the total of each simulation
simulation_totals = np.sum(dice_rolls, axis=0)

# Count the frequency of each outcome in the simulation
simulation_counts, _ = np.histogram(simulation_totals, bins=range(2, 13))

# Calculate the simulated probability of each outcome
simulation_prob = simulation_counts / num_simulations

# Calculate the theoretical probability of each outcome
theoretical_prob = np.zeros(11)
for i in range(2, 7):
    theoretical_prob[i-2] = (i-1)/36
for i in range(8, 13):
    theoretical_prob[i-2] = (13-i)/36

# Plot the simulated and theoretical probabilities
plt.stem(outcomes, simulation_prob, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(outcomes, theoretical_prob, markerfmt='o', use_line_collection=True, label='Theory')
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.legend()
plt.grid()
plt.show()
