import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2], [3, 4]])
s0 = np.array([[1], [0]])
s1 = np.array([[0], [1]])

num_points = 100
n1 = np.random.normal(0, 1, (num_points, 1))
n2 = np.random.normal(0, 1, (num_points, 1))
n = np.hstack((n1, n2))

y_s0 = A @ s0 + n
y_s1 = A @ s1 + n

plt.scatter(y_s0[:,0], y_s0[:,1], c='red', label='$\mathbf{y}|\mathbf{s}_0$')
plt.scatter(y_s1[:,0], y_s1[:,1], c='blue', label='$\mathbf{y}|\mathbf{s}_1$')
plt.legend()
plt.xlabel('$y_1$')
plt.ylabel('$y_2$')
plt.savefig('./5.1.1.pdf')
plt.show()


