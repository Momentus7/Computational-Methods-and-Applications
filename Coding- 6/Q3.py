import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

g = 9.8 # Acceleration due to gravity
length_of_pendulum = 1.25 # length of the pendulum
t = 200 # time

def d2_theta_d_t2(theta):
    return  -(g/length_of_pendulum)*math.sin(theta)

#Euler's forward method to solve the system
def theta(t):
    th = math.pi/2.5
    w = 0 #Omega=d_theta/dt
    dt = 0.001 # delta t increment
    m=np.arange(0,t,dt)
    for i in m:
        th=th+w*dt
        w=w+d2_theta_d_t2(th)*dt
    return th
# plot for the pendulum


fig, ax = plt.subplots()
plt.title("Stimulation of motion of a pendulum")
plt.plot([-1,1],[1,1],'k',linewidth=5) # Pendulum support horizental line
plt.xlim(-5,5)
plt.ylim(-5,5)
f,= plt.plot(0, 0,'k') # Base condition Pendulum returns to origin after a rotation
bob, = plt.plot(0, 0, 'o', markersize=10, color='red')

x = [0,0]
y = [1,1]

def pendulum(i):
    a = length_of_pendulum*math.sin(theta(i)) # L *sin(theta)
    b = -length_of_pendulum*math.cos(theta(i)) # -L *cos(theta)

    x[1] = a
    y[1] = b
    # add bob to the end of the pendulum
    bob_x = a
    bob_y = b - 0.1 # adjust the y-coordinate of the bob to make it below the pendulum stick

    # update the data for the bob
    bob.set_data([bob_x], [bob_y])

    f.set_xdata(x)
    f.set_ydata(y)

    return bob,f,
# Animation for the pendulum
m=FuncAnimation(fig, func=pendulum, frames=np.arange(0,100,0.03),interval = 10)

# Define the file location for the GIF
#d_loc = r"D:\IIT PKD\2nd Sem\Computational Methods\animation_Q3.gif"

# Define the writer object for the animation
#m = animation.PillowWriter(fps=5)

# Save the animation to the specified file location
#anim.save(d_loc, writer=m)
plt.show()