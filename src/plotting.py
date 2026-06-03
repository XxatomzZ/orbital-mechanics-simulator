import matplotlib.pyplot as plt
#import numpy as np

from simulation import r, nt
from bodies import bodies
from physics import orbiting_body, com

# set variables using data from simulation.py
x = r[0, :]
y = r[1, :]
z = r[2, :]
#y = np.zeros(nt)
#z = np.zeros(nt)

# plotting curves on a 3D axis
col1 = bodies[orbiting_body]['color']                       ## color of orbiting path
col2 = bodies[com]['color']                                 ## color of center of mass
size = bodies[com]['size']                                  ## size of center of mass

ax = plt.figure().add_subplot(projection='3d')              ## initialize axes

ax.plot(x, y, z, label='Orbital Path', c=col1)
ax.scatter(0, 0, 0, c=col2, s=size)
ax.legend()

plt.show()

#print(x)

