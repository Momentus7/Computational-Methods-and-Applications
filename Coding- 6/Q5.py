import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation


def solveODE(init_r, init_v,start_time,end_time, number_of_points):
    def findnorm(p1, p2):
        #Calculate the norm of the vector   
        return max(np.linalg.norm(p2 - p1),10)

    def double_derivative(p1, p2, p3):
        #Solve  double derivative  of the system of ODEs
        
        r_double_derivative = ((p2 - p1) / (findnorm(p2, p1) ** 3)) + ((p3 - p1) / (findnorm(p3, p1) ** 3))
        r_double_derivative=list(r_double_derivative)
        return r_double_derivative

    def vdp_derivatives(t, y):

        #Solve derivatives  differential equations
        
        pos1x, pos1y, pos2x, pos2y, pos3x, pos3y, velocity1x, velocity1y, velocity2x, velocity2y, velocity3x, velocity3y = y
        pos1 = np.array([pos1x, pos1y])
        pos2 = np.array([pos2x, pos2y])
        pos3 = np.array([pos3x, pos3y])
        velocity1 = [velocity1x, velocity1y]
        velocity2 = [velocity2x, velocity2y]
        velocity3 = [velocity3x, velocity3y]
        velocity1d = double_derivative(pos1, pos2, pos3)
        velocity2d = double_derivative(pos2, pos3, pos1)
        velocity3d = double_derivative(pos3, pos1, pos2)
        return [*velocity1, *velocity2, *velocity3, *velocity1d, *velocity2d, *velocity3d]

    t = np.linspace(start_time,end_time, number_of_points) #Time intervals

    sol = solve_ivp(fun=vdp_derivatives, t_span=[start_time,end_time], y0=[*init_r, *init_v], t_eval=t) #Solve System of ODE

    
    pos1x, pos1y, pos2x, pos2y, pos3x, pos3y, *vs = sol.y # Points's value of  curve

    fig = plt.figure() 
    ax = fig.add_subplot()

    bob_radius = 0.2 # Add bob radius for 3 bobs
    bob1 = ax.add_patch(
        plt.Circle((pos1x[0], pos1y[0]), bob_radius, fc="g", label="Bob 1")
    )
    bob2 = ax.add_patch(
        plt.Circle((pos2x[0], pos2y[0]), bob_radius, fc="r", label="Bob 2")
    )
    bob3 = ax.add_patch(
        plt.Circle((pos3x[0], pos3y[0]), bob_radius, fc="y", label="Bob 3")
    )

    # Plotting the trajectories
    bobpos = [bob1, bob2, bob3]

    def Animation_fun():
        
        #function for  animation.
    
        ax.set_title("Stimulation of Three Body Problem")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        # Set the plot limits
        ax.set_xlim(-4, 6)
        ax.set_ylim(-6, 6)

        # # updated each bob at the start of the animation
        return bobpos

    def animate(i):
        
        # Update the current position of  bobs
        bob1.set_center((pos1x[i], pos1y[i]))
        bob2.set_center((pos2x[i], pos2y[i]))
        bob3.set_center((pos3x[i], pos3y[i]))

        # updated each bob at each frame
        return bobpos

    # Animation
    anim = FuncAnimation(fig,animate,init_func=Animation_fun,frames=len(pos1x),repeat=True,interval=1,blit=True,)

    plt.legend()
    plt.show()

    return anim

#Initial position
pos1 = [0, 0]
pos2 = [3, 2]
pos3 = [3, -4]
#Initial velocity
velocity1 = [0, 0]
velocity2 = [0, 0]
velocity3 = [0, 0]
solveODE([*pos1, *pos2, *pos3], [*velocity1, *velocity2, *velocity3], 0, 300,2000)