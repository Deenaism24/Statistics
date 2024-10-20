import matplotlib.pyplot as plt
import numpy as np
import random
from math import pi

phi = (1 + np.sqrt(5)) / 2
n_points = 10000

x = np.zeros(n_points)
y = np.zeros(n_points)

for i in range(n_points):
    theta = 2 * pi * random.random()
    r = phi ** theta
    x[i] = r * np.cos(theta)
    y[i] = r * np.sin(theta)

plt.scatter(x, y, color='gold')
plt.axis('equal')
plt.title('Золотая спираль')
plt.show()
