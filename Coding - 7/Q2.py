import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
print("Message : It will take some time to get the animated output")
# Set up the parameters
h = 0.01  # Step size for position
k = 0.0005 # Step size for time
pos = np.arange(0, 1 + h, h)  # Array of position
t = np.arange(0, 10 + k, k)  # Array of time

# Define the initial and boundary conditions
u = np.zeros((len(pos), len(pos), len(t)))  # Function of position, position, and time
xc, yc = 0.5, 0.5  # Center of the heat source
f = np.exp(-np.sqrt((pos - xc)**2 + (pos[:, np.newaxis] - yc)**2))  # Heat source function
u[:, :, 0] = 0  # Initial condition
u[0, :, :] = 0  # Boundary condition at x = 0
u[-1, :, :] = 0  # Boundary condition at x = 1
u[:, 0, :] = 0  # Boundary condition at y = 0
u[:, -1, :] = 0  # Boundary condition at y = 1

# Apply the finite difference method
factor = k / h ** 2
for j in range(1, len(t)):
    for i in range(1, len(pos) - 1):
        for k in range(1, len(pos) - 1):
            u[i, k, j] = (1 - 4 * factor) * u[i, k, j - 1] + factor * (u[i - 1, k, j - 1] + u[i + 1, k, j - 1] + u[i, k - 1, j - 1] + u[i, k + 1, j - 1]) + k * f[i, k]

# Create the animation
fig, ax = plt.subplots()
im = ax.imshow(u[:, :, 0], cmap='hot', origin='lower', extent=[0, 1, 0, 1])

def update(t):
    im.set_data(u[:, :, t])
    return im,

plt.title("Heat Conduction in a 2D Sheet")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar(im)

anim = FuncAnimation(fig, update, frames=range(0,len(t)), interval=300)

plt.show()
