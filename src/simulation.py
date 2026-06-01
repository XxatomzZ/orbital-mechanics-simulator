import numpy as np
from physics import r_x
#from scipy.integrate import solve_ivp


# time step values
dt = 0.001                      ## size of time step
nt = 1000                        ## final time

# initialize arrays.   dim: 3 x nt
r = np.zeros((3, nt))
v = np.zeros((3, nt))

# set ICs
r[0, 0] = r_x                  ## distance from center of mass (c.o.m at origin for simplicity)
v[0, 0] = 1                    ## v_x (set as 1 as a placeholder)
v[1, 0] = 0                    ## v_y
v[2, 0] = 0                    ## v_z 


# simulate the time steps
'''
for now everything will be split into x,y,z components
later I will condense this to store all components in a (3,nt) matrix
'''
def time_step(v, r, mu):
    for t in range(1, nt-1):
        a_grv_x = - (mu / (np.abs(r[0, t]) ** 3)) * r[0, t]        ## acc. due to gravity    (3 x nt)
        a_grv_y = - (mu / (np.abs(r[1, t]) ** 3)) * r[1, t]
        a_grv_z = - (mu / (np.abs(r[2, t]) ** 3)) * r[2, t]
        a_thr = 0                                               ## a_thr = 0 for natural bodies 
        
        # now calculate updated velocities and radii
        v[0, t+1] = v[0, t] + (a_grv_x + a_thr) * dt
        v[1, t+1] = v[1, t] + (a_grv_y + a_thr) * dt
        v[2, t+1] = v[2, t] + (a_grv_z + a_thr) * dt
        r[0, t+1] = r[0, t] + v[0, t+1] * dt
        r[1, t+1] = r[1, t] + v[1, t+1] * dt
        r[2, t+1] = r[2, t] + v[2, t+1] * dt

    return r

