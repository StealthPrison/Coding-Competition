from numpy import *
from matplotlib import pyplot as plt


plt.style.use('rose-pine')

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

# Prerequisites

P = 248.348    
times = []
ecc_0_times = []

# Simpson Integraion Function (t / Time) | y-axis

def simpsonintegration(theta, ecc):
    global times
    a = 0
    n = 10
    
    h = (theta - a) / (n - 1) # h = dtheta
    
    x = linspace(a, theta, n) # Creates n evenly spaced values betwixt a and theta

    f = (1-ecc*cos(x))**2

    I_simp = ( # Pseudo Integration Portion
        (h/3) * 
        (
            f[0] + 2*sum(f[:n-2:2]) + 
            4*sum(f[1:n-1:2]) + f[n-1]
            )
        )


    time = (P * (1 - ecc ** 2) ** (3 / 2)) * I_simp * (1 / (2 * pi)) # Entire / Rest of Function
    
    # Determines which line it should be in

    if ecc == -0.25:
        times.append(time)
    elif ecc == 0:
        ecc_0_times.append(time)


thetas = [] 

for i in range(0, 19, 1): # Theta values creation for planet
    thetas.append(i)

for i in range(len(thetas)): # Determining Orbit Polar Angle / Radians
    simpsonintegration(thetas[i], -0.25) 

plt.plot(times, thetas, label = 'e = 0.25', color="green") # Planet's Line


thetas = []

for i in range(0, 190, 1): # Theta values creation for 0 Ecc Line
    thetas.append((i/10))


for i in range(len(thetas)): # Determining Orbit Polar Angle / Radians
    simpsonintegration(thetas[i], 0)

plt.plot(ecc_0_times, thetas, label = 'Circular e = 0', color="blue") # Line of 0 Eccentricity

# Plotting Graph

plt.xlim(0, 800)
plt.ylim(0, 20)
plt.legend()
plt.grid()
plt.show()