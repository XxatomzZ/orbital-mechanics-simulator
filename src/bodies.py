
'''
I will source these rather than manually entering eventually

all initial positions and velocities are sourced from NASA's Horizons System
'''
# barycenter (so we can have sun's orbit too)       -->        plot from pov of barycenter, etc.
bodies = {
    "sun":  {"m":1.98842e30, "r_x":1, "r_y":0, "r_z":1, 
             "v_x":1, "v_y":1, "v_z":1, 
             "color":'orange', "size":100},
    "mercury":  {"m":3.302e23, "r_x":-4.240067150782017e7, "r_y":2.816182514120559e7, "r_z":6.245104674515469e6, 
             "v_x":-3.756240413032418e1, "v_y":-3.810548670744638e1, "v_z":3.316009847293184e-1, 
             "dt":60.0, "nt":150000, "color":'lightsteelblue', "size":5},
    "venus":  {"m":48.685e23, "r_x":-9.809179266732852e7, "r_y":4.349512116129568e7, "r_z":6.267566451483713e6, 
               "v_x":-1.459698264119512e1, "v_y":-3.206251753253267e1, "v_z":4.021224499123015e-1, 
               "dt":60.0, "nt":1000000, "color":'gold', "size":5},
    "earth": {"m":5.97219e24, "r_x":-5.647732691439635e7, "r_y":-1.416456904119171e8, "r_z":2.578586764929444e4, 
              "v_x":2.718778638891806e1, "v_y":-1.113749515449470e1, "v_z":4.809465119892664e-4, 
              "dt":60.0, "nt":1000000, "color":'forestgreen', "size":10},
    "mars":  {"m":6.4171e23,"r_x":2.018061600153138e8, "r_y":5.952240891858152e7, "r_z":-3.674969756283928e6, 
              "v_x":-5.989213156053129e0, "v_y":2.529095227732117e1, "v_z":6.768596958448629e-1, 
              "dt":60.0, "nt":1000000, "color":'tomato', "size":10},
    "jupiter":  {"m":18.9819e26, "r_x":-4.078660583422423e8, "r_y":6.731700277625408e8, "r_z":6.335527333647251e6, 
                 "v_x":-1.133082433468032e1, "v_y":-6.154327289137208e0, "v_z":2.790723430461255e-1, 
                 "dt":6000.0, "nt":10000000, "color":'chocolate', "size":50},
    "saturn":  {"m":5.6834e26, "r_x":1.406227564064627e9, "r_y":1.614651792484778e8, "r_z":-5.879762085451436e7, 
                "v_x":-1.632154013301171e0, "v_y":9.575755458089246e0, "v_z":-1.017616045673719e-1, 
                "dt":6000.0, "nt":1000000, "color":'tan', "size":30},
    "uranus":  {"m":86.813e24, "r_x":1.400753339183652e9, "r_y":2.551651476705576e9, "r_z":-8.670405888163447e6, 
                "v_x":-6.019810831854246e0, "v_y":2.959691684983484e0, "v_z":8.914907518029813e-2, 
                "dt":6000.0, "nt":1000000, "color":'aquamarine', "size":40},
    "neptune":  {"m":102.409e24, "r_x":4.466132546147506e9, "r_y":1.471681934502637e8, "r_z":-1.059572628055010e8, 
                 "v_x":-2.151918829802196e-1, "v_y":5.464948384418276e0, "v_z":-1.068748811740947e-1, 
                 "dt":6000.0, "nt":1000000, "color":'dodgerblue', "size":40},
    "pluto":  {"m":1.307e22, "r_x":2.936444733916075e9, "r_y":-4.413939723602009e9, "r_z":-3.770756781061409e8, 
               "v_x":4.683891223894359e0, "v_y":1.789611831423461e0, "v_z":-1.567967875533711e0, 
               "dt":6000.0, "nt":3000000, "color":'maroon', "size":5},
    "moon":  {"m":7.349e22, "r_x":-2.411525875402620e5, "r_y":-3.232324513039968e5, "r_z":-3.462418964601953e4, 
              "v_x":7.719468739232185e-1, "v_y":-5.951965931163530e-1, "v_z":-1.668873195866993e-2, 
              "dt":600.0, "nt":100000, "color":'grey', "size":5}
    }
# may need to add unique dt and nt for each body                - EARTH ONWARDS
'''
m: mass of object
r: initial position vector w.r.t center of mass (r_x, r_y, r_z)
v: initial velocity (v_x, v_y, v_z)
note: color and size used only for plotting
'''

# mu = G*M                          ## G=const.     ##M = m_1 + m_2 ~ m_1
# note this is for m_1 >> m_2 (as MOST problems are)
