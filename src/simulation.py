import numpy as np
#from scipy.integrate import solve_ivp

from bodies import bodies
from physics import mu, orbiting_body, sun_orbits

# for one body
if orbiting_body in sun_orbits:
    # time step values
    dt = bodies[orbiting_body]['dt']                     ## size of time step
    nt = bodies[orbiting_body]['nt']                        ## final time

    # initialize arrays.   dim: 3 x nt
    r = np.zeros((3, nt))
    v = np.zeros((3, nt))

    # set ICs
    # values sourced from NASAs horizon system
    r[0, 0] = bodies[orbiting_body]['r_x']                  ## distance from center of mass (c.o.m at origin for simplicity)
    r[1, 0] = bodies[orbiting_body]['r_y']
    r[2, 0] = bodies[orbiting_body]['r_z']
    v[0, 0] = bodies[orbiting_body]['v_x']
    v[1, 0] = bodies[orbiting_body]['v_y']
    v[2, 0] = bodies[orbiting_body]['v_z']

    v_mag = np.sqrt(v[0,0]**2 + v[1,0]**2 + v[2,0]**2)
    print('v_mag:', v_mag)

    #print('r:', r)
    #print('v:', v)

    #print(np.abs(r[0,0]))
    #print(np.abs(r[1,0]))

    # simulate the time steps
    '''
    for now everything will be split into x,y,z components
    later I will condense this to store all components in a (3,nt) matrix
    '''
    def time_step(v, r, mu):
        for t in range(0, nt-1):
            # calculate vector magnitude |r|
            r_mag = np.sqrt(r[0,t]**2 + r[1,t]**2 + r[2,t]**2)
            # calculate accelerations
            a_grv_x = -(mu / r_mag**3) * r[0, t]        ## acc. due to gravity    (3 x nt)
            a_grv_y = -(mu / r_mag**3) * r[1, t]
            a_grv_z = -(mu / r_mag**3) * r[2, t]
            a_thr = 0                                               ## a_thr = 0 for natural bodies 
            
            # now calculate updated velocities and radii
            v[0, t+1] = v[0, t] + (a_grv_x + a_thr) * dt
            v[1, t+1] = v[1, t] + (a_grv_y + a_thr) * dt
            v[2, t+1] = v[2, t] + (a_grv_z + a_thr) * dt
            r[0, t+1] = r[0, t] + v[0, t+1] * dt
            r[1, t+1] = r[1, t] + v[1, t+1] * dt
            r[2, t+1] = r[2, t] + v[2, t+1] * dt

        return r

    r = time_step(v, r, mu)
    #print(r)
    '''
    later I can store data for use in plotting - reduce time complexity
    '''


# for multiple bodies
else:
    results = []
    for i in sun_orbits:
        dt = bodies[i]['dt']
        nt = bodies[i]['nt']

        r = np.zeros((3, nt))
        v = np.zeros((3, nt))

        r[0, 0] = bodies[i]['r_x']
        r[1, 0] = bodies[i]['r_y']
        r[2, 0] = bodies[i]['r_z']
        v[0, 0] = bodies[i]['v_x']
        v[1, 0] = bodies[i]['v_y']
        v[2, 0] = bodies[i]['v_z']

        v_mag = np.sqrt(v[0,0]**2 + v[1,0]**2 + v[2,0]**2)
        print('v_mag:', v_mag)

        #sim time steps
        def time_step(v, r, mu):
            for t in range(0, nt-1):
                # calculate vector magnitude |r|
                r_mag = np.sqrt(r[0,t]**2 + r[1,t]**2 + r[2,t]**2)
                # calculate accelerations
                a_grv_x = -(mu / r_mag**3) * r[0, t]        ## acc. due to gravity    (3 x nt)
                a_grv_y = -(mu / r_mag**3) * r[1, t]
                a_grv_z = -(mu / r_mag**3) * r[2, t]
                a_thr = 0                                               ## a_thr = 0 for natural bodies 
                
                # now calculate updated velocities and radii
                v[0, t+1] = v[0, t] + (a_grv_x + a_thr) * dt
                v[1, t+1] = v[1, t] + (a_grv_y + a_thr) * dt
                v[2, t+1] = v[2, t] + (a_grv_z + a_thr) * dt
                r[0, t+1] = r[0, t] + v[0, t+1] * dt
                r[1, t+1] = r[1, t] + v[1, t+1] * dt
                r[2, t+1] = r[2, t] + v[2, t+1] * dt
        
            return r
        
        r = time_step(v, r, mu)
        results.append(r)


#print(len(results))
