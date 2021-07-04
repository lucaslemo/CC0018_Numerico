import matplotlib.pyplot as plt
import numpy as np
delta = np.float64(2**-53)
x = np.linspace(0, 24)
y = np.linspace(0, 24)
y = y - delta
plt.axis([0, 30*delta, 0, 30*delta])
plt.plot(x, x, label = "reta da parede")
plt.plot(y, x, label = "reta do robô")
