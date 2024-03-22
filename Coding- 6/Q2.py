import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy.interpolate import barycentric_interpolate, lagrange

def solve_ode_backward_euler_method(h):
    if isinstance(h,(int,float)): # Check the type of h
        t0=0
        tf=10
        x0=5
        def f(x,t):
            return -2*x
        # f : the right-hand side of the ODE
        # x0: initial condition
        # t0: Initial time 
        # tf: final time
        # h : time step size
    
        n = int((tf-t0)/h) # No of points
        t = np.linspace(t0, tf, n+1)
        x = np.zeros(n+1)
        x[0] = x0
    
        # Update the solution values using backward euler method
        for i in range(n):
            x[i+1] = x[i] / (2*h+1) #x[i+1]=x[i]+f(x[i+1],t[i+1])
            #f(x[i+1],t[i+1])=-2x[i]
    
        # Compute a polynomial that passes through the discrete solution points
        coeffs = np.polyfit(t, x, n)
        poly = np.poly1d(coeffs)
        #poly=lagrange(t,x)
    
        return t, x, poly
    else:
        raise Exception("Time Step size should be either an integer or float")

# Exact solution of x'(t) = -2x(t) with x(0) = 5 is x(t) = 5 * exp(-2*t)
def exact_solution(t):
    return 5 * np.exp(-2*t)


h_size = [0.1, 0.5, 1, 2, 3]
#step_sizes = [0.1,0.5,1]
plt.figure(figsize=(10, 6))
x_exact=np.linspace(0, 10, 100)
# Computing exact solution
y_exact=exact_solution(x_exact)
plt.plot(x_exact,y_exact,'c',label='Exact Solution')
col=['g','r','y','b','k']
i=0;
for h in h_size:
    t, x, poly = solve_ode_backward_euler_method(h)
    plt.plot(t, poly(t),col[i], label=f'h={h}')
    i+=1
    
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()
