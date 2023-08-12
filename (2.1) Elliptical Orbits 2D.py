# Importing the relevant modules
import matplotlib.pyplot as plt
import math
from numpy import *

plt.style.use('rose-pine')

# Data

planets = [
    # ['Planet', Semi-Major Axis, Semi-Minor Axis ]
    ['Mercury', 0.387, 0.37870],
    ['Venus', 0.723, 0.72298],
    ['Earth', 1.00, 0.99986],
    ['Mars', 1.523, 1.51740],
    ['Jupiter', 5.20, 5.19820],
    ['Saturn', 9.58, 9.56730],
    ['Uranus', 19.29, 19.19770],
    ['Neptune', 30.25, 30.10870],
    ['Pluto', 39.51, 39.482]
]


# Calculations

# Functions

def eccentricity_calc(s_major, s_minor): # Calculates the Eccentricity of the Ellipse
    s_minor = s_minor ** 2
    s_major = s_major ** 2
    ecc = (1 - s_minor/s_major) ** 0.5
    return(ecc)

def polar_equation_ellipse_calc(planet, theta): # Self explanatory
    from math import cos
    semi_major = planets[planet][1]
    ecc = eccentricity_of_ellipse[planet]
    top_eq = semi_major * (1 - (ecc ** 2))
    bottom_eq = 1 - (ecc * cos(theta))

def planet_ylimit(): # Defining Graph Y-Axis Limit
    temp_list = []
    for i in range(0, 4):
        temp_list.append(planets[i][2])
    return(max(temp_list))

def planet_xlimit(): # Defining Graph X-Axis Limit
    temp_list = []
    for i in range(0, 4):
        temp_list.append(planets[i][1])
        planet = i
    return([max(temp_list), i])


eccentricity_of_ellipse = [] # Calculating all Eccentricities
for planet in range(len(planets)):
    ecc_temp = eccentricity_calc(planets[planet][1], planets[planet][2])
    eccentricity_of_ellipse.append(ecc_temp)

## Plotting Both Axis



# Ellipses of First 5 Planets
for planet in range(0, 4):
    t = linspace(0, 360, 180)
    x = planets[planet][1] * cos(radians(t)) + eccentricity_of_ellipse[planet]
    y = planets[planet][2] * sin(radians(t))
    plt.plot(x,y, label=planets[planet][0])
    

plt.plot(width = 2, edgecolor="black")

# Constant/Fixed Sun 
Sun=[0]
plt.plot(Sun, c= "Yellow", marker="o")

# Defining Graph Limits
ylimit = planet_ylimit()
xlimit = planet_xlimit()

# Plotting Graph
plt.ylim(-ylimit, ylimit)
plt.xlim(- (xlimit[0] - eccentricity_of_ellipse[xlimit[1]]), xlimit[0] + eccentricity_of_ellipse[xlimit[1]])
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.title('Solar System')
plt.legend()
plt.grid()
plt.show()


