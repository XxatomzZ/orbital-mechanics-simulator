from scipy import constants
#import numpy as np

from bodies import bodies


'''
User will select center of mass and orbiting body here
For now, I will just test out the interaction between the Moon and Earth
'''
while True:
    orbiting_body = input('Which orbit would you like to see: (type all to see all planetary orbits)').casefold()
    if orbiting_body in bodies:
        break
    elif orbiting_body == 'all':
        break
    else:
        print("❗ Please enter a valid astronomical body:")
        print("Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon")         ## make this automatic ??

# ask user if they would like to add more orbits to the plot
# each orbit will need to store an individual orbiting_body, com, M, and r
# or plot line then run through next orbit and add to plot ??????
'''
while answer.upper() != 'N':
  play()
  answer = input('Add more orbital paths? (Y/N) ')


while True:
    additional_body = input('Would you like to plot anymore orbital paths?').casefold()
    if orbiting_body in bodies:
        break
    else:
        print("❗ Please enter a valid astronomical body:")
        print("Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon")
'''


# gravitational constant G
G = constants.G

# calculate M and subsequently mu
sun_orbits = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
earth_orbits = 'moon'
if orbiting_body in sun_orbits:
    com = 'sun'
    M = bodies['sun']['m']
elif orbiting_body == 'all':
    com = 'sun'
    M = bodies['sun']['m']
else:
    com = 'earth'
    M = bodies['earth']['m']



mu = G * M / 1e9               ## / 10e9 as we want in units km3/s2 rather than m3/s2

print(mu)

















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