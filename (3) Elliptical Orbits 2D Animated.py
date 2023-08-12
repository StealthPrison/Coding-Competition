# Importing the relevant modules
from matplotlib import pyplot as plt, animation as  anim
import math
from numpy import *

plt.style.use('rose-pine')

# Data

planets = [
    # ['Planet', Semi-Major Axis, Semi-Minor Axis, Tilts, Orbital Frequencies]
    ['Mercury', 0.387, 0.37870, 7.00, 6],
    ['Venus', 0.723, 0.72298, 3.39, 3],
    ['Earth', 1.00, 0.99986, 0.00, 2],
    ['Mars', 1.523, 1.51740, 1.85, 1],
    ['Jupiter', 5.20, 5.19820, 1.31, 0.9],
    ['Saturn', 9.58, 9.56730, 2.49, 0.5],
    ['Uranus', 19.29, 19.19770, 0.77, 0.3],
    ['Neptune', 30.25, 30.10870, 1.77, 0.7],
    ['Pluto', 39.51, 39.482, 17.5, 0.9]
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


## Defining Figure

fig, ax = plt.subplots()


# Constant/Fixed Sun 
Sun=[0]
plt.plot(Sun, c= "Yellow", marker="o")

# Ellipses of First 5 Planets
for planet in range(0, 4):
    t = linspace(0, 360, 180) # Start point of revolution, End point, Num of points
    x = planets[planet][1] * cos(radians(t)) + eccentricity_of_ellipse[planet]
    y = planets[planet][2] * sin(radians(t))
    plt.plot(x,y, label=planets[planet][0])

plt.plot(width = 2, edgecolor="black")

# Defining Graph Limits
ylimit = planet_ylimit()
xlimit = planet_xlimit()

# Plotting Graph Limits

plt.ylim((-ylimit - 0.2), (ylimit + 0.2))
plt.xlim(- ( (xlimit[0] - eccentricity_of_ellipse[xlimit[1]]  + 0.2)), (xlimit[0] + eccentricity_of_ellipse[xlimit[1]]  + 0.2))

# Plotting Info & Misc

plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.title('Solar System')
plt.legend()
plt.grid()


## Animation


# Planet Artist

ani_planet,  = plt.plot([], [], marker='o')
ani_planet2, = plt.plot([], [], marker='o')
ani_planet3, = plt.plot([], [], marker='o')
ani_planet4, = plt.plot([], [], marker='o')
ani_planet5, = plt.plot([], [], marker='o')

orbits = [ani_planet, ani_planet2, ani_planet3, ani_planet4, ani_planet5]

# Animation Function

def update(i):
    theta = deg2rad(i)
    for i in range(4):
        x = planets[i][1] * cos(theta*planets[i][4]) + eccentricity_of_ellipse[i]
        y = planets[i][2] * sin(theta*planets[i][4])
        orbits[i].set_data(x, y)


an1 = anim.FuncAnimation(fig,  update, frames=1080, interval = 0)



# Displaying Graph

plt.show()
