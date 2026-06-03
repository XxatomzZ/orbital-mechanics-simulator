
'''
I will source these rather than manually entering eventually

all initial positions and velocities are sourced from NASA's Horizons System
'''
bodies = {
    "sun":  {"m":1.98842e30, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'orange'},
    "mercury":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'grey'},
    "venus":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'yellow'},
    "earth": {"m":5.97219e24, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'lime'},
    "mars":  {"m":6.41693e23,"r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'red'},
    "jupiter":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'orange'},
    "saturn":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'brown'},
    "uranus":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'light blue'},
    "neptune":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'blue'},
    "pluto":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'dark red'},
    "moon":  {"m":7.34581e22, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'grey'}
    }
'''
m: mass of object
r: radius of object
d: distance from  orbiting body
'''

# mu = G*M                          ## G=const.     ##M = m_1 + m_2
# note this is for m_1 >> m_2 (as MOST problems are)
