# Importing the relevant modules
import matplotlib.pyplot as plt
import math
from numpy import *

plt.style.use('rose-pine')

# Data


planets = [
    # ['Planet', Semi-Major Axis, Semi-Minor Axis, Tilts, Orbital Period (Days)]
    ['Mercury', 0.387, 0.37870, 7.00, 88.0],
    ['Venus', 0.723, 0.72298, 3.39, 224.7],
    ['Earth', 1.00, 0.99986, 0.00, 365.2],
    ['Mars', 1.523, 1.51740, 1.85, 687.0],
    ['Jupiter', 5.20, 5.19820, 1.31, 4331],
    ['Saturn', 9.58, 9.56730, 2.49, 10,747],
    ['Uranus', 19.29, 19.19770, 0.77, 30,589],
    ['Neptune', 30.25, 30.10870, 1.77, 59,800],
    ['Pluto', 39.51, 39.482, 17.5, 90,560]
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
    for i in range(len(chosen_planets)):
        temp_list.append(chosen_planets[i][2])
    return(max(temp_list))

def planet_xlimit(): # Defining Graph X-Axis Limit
    temp_list = []
    for i in range(len(chosen_planets)):
        temp_list.append(chosen_planets[i][1])
        planet = i
    return([max(temp_list), i])





## Plotting Both Axis

# Constant/Fixed Sun 
Sun=[0]
plt.plot(Sun, c= "Yellow", marker="o")

chosen_planets = []


'''
for i in range(2):
    allow = False
    while allow == False:
        try:
            chosen_p = int(input("Choose Planets: "))
            allow = True
        except:
            print("Please Try Again.")
    chosen_planets.append([planets[chosen_p][0], planets[chosen_p][1], planets[chosen_p][2], planets[chosen_p][3]])
'''
### TEMPORARY
chosen_planets = [
    [planets[1][0], planets[1][1], planets[1][2], planets[1][3]],
    [planets[2][0], planets[2][1], planets[2][2], planets[2][3]]
]
###

eccentricity_of_ellipse = [] # Calculating all Eccentricities
for planet in range(len(chosen_planets)):
    ecc_temp = eccentricity_calc(planets[planet][1], planets[planet][2])
    eccentricity_of_ellipse.append(ecc_temp)


# Ellipses of Chosen Planets

N = 10 # Number of Orbits


if chosen_planets[0][3] > chosen_planets[1][3]: 
    max_num = chosen_planets[0][3]
else:
    max_num = chosen_planets[1][3]

change_in_time = N * max_num /1234

t = linspace(0, (N * 360), 360)


for planet in range(len(chosen_planets)):
    cur_t = linspace(0, 360, 180)
    x = chosen_planets[planet][1] * cos(radians(cur_t)) + eccentricity_of_ellipse[planet]
    y = chosen_planets[planet][2] * sin(radians(cur_t))

    plt.plot(x,y, label=chosen_planets[planet][0])
    del cur_t



for i in range(360):
    
    xvalue = []
    yvalue = []

    x = chosen_planets[0][1] * cos(radians(t)) + eccentricity_of_ellipse[0] 
    y = chosen_planets[0][2] * sin(radians(t))

    x2 = chosen_planets[1][1] * cos(radians(t)) + eccentricity_of_ellipse[1]
    y2 = chosen_planets[1][2] * sin(radians(t))
    
    xvalue.append(x[i])
    xvalue.append(x2[i])
    yvalue.append(y[i])
    yvalue.append(y2[i])
    plt.plot(xvalue, yvalue, color='white', linewidth=0.3)






# Defining Graph Limits
ylimit = planet_ylimit()
xlimit = planet_xlimit()

# Plotting Graph

'''
plt.ylim(-ylimit, ylimit)
plt.xlim(- (xlimit[0] - eccentricity_of_ellipse[xlimit[1]]), xlimit[0] + eccentricity_of_ellipse[xlimit[1]])
'''
plt.title(f'Spyrograph of {chosen_planets[0][0]}, and {chosen_planets[1][0]}')

# Circular Graph
fig = plt.gcf()
fig.gca().set_aspect('equal')

plt.legend()
plt.grid()
plt.show()
