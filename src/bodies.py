
'''
I will source these rather than manually entering eventually

all initial positions and velocities are sourced from NASA's Horizons System
'''
bodies = {
    "sun":  {"m":1.98842e30, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'orange', "size":100},
    "mercury":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'grey', "size":5},
    "venus":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'yellow', "size":5},
    "earth": {"m":5.97219e24, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'lime', "size":10},
    "mars":  {"m":6.41693e23,"r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'red', "size":10},
    "jupiter":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'orange', "size":50},
    "saturn":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'brown', "size":30},
    "uranus":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'light blue', "size":40},
    "neptune":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'blue', "size":40},
    "pluto":  {"m":0, "r_x":1, "r_y":0, "r_z":1, "v_x":1, "v_y":1, "v_z":1, "color":'dark red', "size":5},
    "moon":  {"m":7.349e22, "r_x":-2.411525875402620e5, "r_y":-3.232324513039968e5, "r_z":-3.462418964601953e4, 
              "v_x":7.719468739232185e-1, "v_y":-5.951965931163530e-1, "v_z":-1.668873195866993e-2, 
              "color":'grey', "size":5}
    }
# may need to add unique dt and nt for each body
'''
m: mass of object
r: position vector (r_x, r_y, r_z)
v: velocity (v_x, v_y, v_z)
note: color and size used only for plotting
'''

# mu = G*M                          ## G=const.     ##M = m_1 + m_2 ~ m_1
# note this is for m_1 >> m_2 (as MOST problems are)
