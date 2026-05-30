import numpy as np
#from scipy.integrate import solve_ivp


# time step values
dt = 0.001                      ## size of time step
nt = 1000                        ## final time


# initialize arrays.   dim: 3 x nt
r = np.zeros((3, nt))
v = np.zeros((3, nt))


# set ICs
r[0] = (r_x, 0, 0)                  ## distance from center of mass (c.o.m at origin for simplicity)
v[0] = (v_x, v_y, v_z)              ## approx. circular velocity



# simulate the time steps
for t in range(1, nt-1):
    a_grv = - ((G * M) / (np.abs(r[t]) ** 3)) * r[t]        ## acc due to gravity
    a_thr = 0                                               ## a_thr = 0 for natural bodies 
    v[t+1] = v[t] + (a_grv + a_thr) * dt
    r[t+1] = r[t] + v[t+1] * dt

