import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0, 2*np.pi)
x = 2 * np.cos(t)
y = np.sin(t)

plt.plot(x,y)

plt.axis("equal")
plt.show()