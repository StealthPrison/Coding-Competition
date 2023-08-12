# Importing the Relevant Modules
import matplotlib.pyplot as plt

# Data

planets = [
    # ['Planet', Semi-Major Axis, Orbital Period (Years) ]
    ['Mercury', 0.387, 0.24],
    ['Venus', 0.723, 0.62],
    ['Earth', 1.00, 1],
    ['Mars', 1.523, 1.88],
    ['Jupiter', 5.20, 11.86],
    ['Saturn', 9.58, 29.63],
    ['Uranus', 19.29, 84.75],
    ['Neptune', 30.25, 166.34],
    ['Pluto', 39.51, 248.35]
]

# Semi-Major Axis Cube & Orbital Period List
sunAUCube = []
orbitalperiodYears = []
for planet in range(len(planets)):
   value = planets[planet][1]
   value = value ** (3/2)
   sunAUCube.append(value)
   orbitalperiodYears.append(planets[planet][2])


# Plotting Both Axis

plt.plot(sunAUCube, orbitalperiodYears, label = 'Keplar\'s III law relationship', color="red")
plt.plot(sunAUCube, orbitalperiodYears, c="red", linewidth=2, marker="o", markerfacecolor="black")

plt.xlim(0, 300)
plt.ylim(0, 300)
plt.xlabel('(a/AU)^3/2')
plt.ylabel('Time/Yr')
plt.title('Kepler\'s Third Law')
plt.show()