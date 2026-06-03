import matplotlib.pyplot as plt
import numpy as np
from simulation import r, nt


# set variables using data from simulation.py
x = r[0, :]
y = r[1, :]
z = r[2, :]
#y = np.zeros(nt)
#z = np.zeros(nt)

# plotting curves on a 3D axis

ax = plt.figure().add_subplot(projection='3d')              ## initialize axes

ax.plot(x, y, z, label='Orbital Path')
ax.scatter(0, 0, 0, c='lime', s=10)
ax.legend()

plt.show()

#print(x)

