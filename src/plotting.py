import matplotlib.pyplot as plt
from simulation import r


# set variables using data from simulation.py
x = r[0, :]
y = r[1, :]
z = r[2, :]

# plotting curves on a 3D axis

ax = plt.figure().add_subplot(projection='3d')              ## initialize axes

ax.plot(x, y, z, label='Orbital Path')
ax.scatter(0, 0, 0, c='blue', s=1000)
ax.legend()

plt.show()

