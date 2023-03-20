import numpy as np
import matplotlib.pyplot as plt

D = np.loadtxt('data.csv', delimiter=',')

F = D[:, 0]
V = D[:, 1]

plt.title('RLC')
plt.plot(np.log(F), V, label='U_R')
plt.legend()
plt.xlabel('Frequency log(Hz)')
plt.ylabel('Tension mV')
plt.savefig('out.jpg')
