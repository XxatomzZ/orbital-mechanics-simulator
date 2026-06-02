from scipy import constants
import numpy as np

from bodies import bodies


'''
User will select center of mass and orbiting body here
For now, I will just test out the interaction between the Moon and Earth
'''

# gravitational constant G
G = constants.G

# calculate M and subsequently mu
M = bodies['Earth']['m'] + bodies['Moon']['m']
mu = G * M

print(mu)

# set r_x                       ## NEED TO TIDY UP LATER 
E_r = bodies['Earth']['r']
M_r = bodies['Moon']['r']
M_d = bodies['Moon']['d']
r_x = E_r + M_r + M_d

#print('r_x:', r_x)
















'''
# two-body equations


#r = ||r_|| = sqrt[(r_x)^2 + (r_y)^2 + (r_z)^2]                  ##dist. to centre of mass
#a_ = r_tt =  - (mu / r^3) * r_


# def acceleration(mu, r, R):
    a = - (mu / r**2) * 1/r * R
    return a


# calc initial acceleration using ICs
# a1 = acceleration()                     ## body 1
# a2 = acceleration()                     ## body 2



# integrate with ICs to find velocity and position at the next time (time step)

## v1 = int [a1] dt + v1_0
## v2 = int [a2] dt + v2_0

## r1 = int [v1] dt + r1_0
## r2 = int [v2] dt + r2_0
'''