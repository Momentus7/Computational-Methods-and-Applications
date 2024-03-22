import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import CubicSpline, Akima1DInterpolator, BarycentricInterpolator
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

#%matplotlib ipympl

# Create a new figure
fig = plt.figure()

# Add a subplot to the figure
ax = fig.add_subplot(1, 1, 1)

# Define the update function for the animation
def update(frame):
    # Clear the current plot
    plt.clf()

    # Generate the x and y data for the current frame
    x = np.linspace(-np.pi, np.pi, frame+10)
    y = np.tan(x)*np.sin(30*x)*np.exp(x)

    # Calculate the different interpolations
    y_cs = CubicSpline(x, y)
    y_ak = Akima1DInterpolator(x, y)
    y_bc = BarycentricInterpolator(x, y)

    # Generate x values for the interpolated data
    x_int = np.linspace(-math.pi, math.pi, 1000)

    # Plot the different interpolations and the true function
    plt.plot(x_int, y_cs(x_int), 'r', label='Cubic Spline')
    plt.plot(x_int, y_ak(x_int), 'g', label='Akima')
    plt.plot(x_int, y_bc(x_int), 'b', label='Barycentric')
    plt.plot(x, y, 'k', label='True Function')

    # Set the x and y limits for the plot
    plt.xlim(0.0,1.0)
    plt.ylim(-4,4)

    # Add a legend to the plot
    plt.legend()

    # Add a title to the plot with the current iteration number
    plt.title(f'Iteration {frame}')
    plt.show()
    # Return the axis object
    return ax

# Create the animation
anim = animation.FuncAnimation(fig, update,frames = 51,blit = True)

# Define the file location for the GIF
d_loc = r"D:\IIT PKD\2nd Sem\Computational Methods\Assignment -3\animation3_Q5.gif"

# Define the writer object for the animation
m = animation.PillowWriter(fps=5)

# Save the animation to the specified file location
anim.save(d_loc, writer=m)

# Show the final plot
plt.show()
