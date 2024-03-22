import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the parameters
h = 0.01  # Step size for position
k = 0.0005 # Step size for time
pos = np.arange(0, 1 + h, h)  # Array of position
t = np.arange(0, 10 + k, k)  # Array of time

# Define the initial and boundary conditions
init_cond = np.e ** (-pos)  # Initial condition
u = np.zeros((len(pos), len(t)))  # Function of position and time
u[0, :] = 0  # Boundary condition at pos = 0
u[-1, :] = 0  # Boundary condition at pos = len(pos)-1
u[:, 0] = init_cond  # Initial condition for the temperature at t = 0

# Apply the finite difference method
factor = k / h ** 2
for j in range(1, len(t)):
    for i in range(1, len(pos) - 1):
        u[i, j] = factor * u[i - 1, j - 1] + (1 - 2 * factor) * u[i, j - 1] + factor * u[i + 1, j - 1]

# Create the animation
fig, ax = plt.subplots()
line, = ax.plot(pos, u[:, 0])

def update(t):
    line.set_ydata(u[:, t])
    return line,

plt.title("Heat Conduction in a Rod")
plt.xlabel("Position")
plt.ylabel("Temperature")
anim = FuncAnimation(fig, update, frames=range(0,len(t)), interval=300)
plt.show()
