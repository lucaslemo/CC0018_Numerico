import matplotlib.pyplot as plt
import numpy as np
delta = np.float64(2**-53)
x = np.linspace(0, 24)
y = np.linspace(6*delta+delta, 34*delta+delta)
y1 = np.linspace(6*delta+delta, 34*delta+delta)
y = y - delta
z = [0, 6*delta]
z1 = [17*delta, 7*delta]
plt.axis([0, 50*delta, 0, 50*delta])
plt.plot(x, x)
plt.plot(y, y1, color='green')
plt.plot(z,z1, color='green')
plt.legend(['reta da parede', 'reta do robô'], loc=9)
plt.show()
