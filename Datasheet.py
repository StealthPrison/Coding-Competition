planets = [
    # ['Planet', Semi-Major Axis, Semi-Minor Axis, Orbital Period]
    ['Mercury', 0.387, 0.37870, 0.241],
    ['Venus', 0.723, 0.72298, 0.615],
    ['Earth', 1.00, 0.99986, 1.000],
    ['Mars', 1.523, 1.51740, 1.881],
    ['Jupiter', 5.20, 5.19820, 11.859],
    ['Saturn', 9.58, 9.56730, 29.428],
    ['Uranus', 19.29, 19.19770, 83.760],
    ['Neptune', 30.25, 30.10870, 163.746],
    ['Pluto', 39.51, 39.482, 247.974]# 248.348
]
# Calculations

# Functions

def eccentricity_calc(s_major, s_minor): # Calculates the Eccentricity of the Ellipse
    s_minor = s_minor ** 2
    s_major = s_major ** 2
    ecc = (1 - s_minor/s_major) ** 0.5
    return(ecc)

eccentricity_of_ellipse = [] # Calculating all Eccentricities



for planet in range(len(planets)):
    ecc_temp = eccentricity_calc(planets[planet][1], planets[planet][2])
    eccentricity_of_ellipse.append(ecc_temp)

