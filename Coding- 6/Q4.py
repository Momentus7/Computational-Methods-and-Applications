import matplotlib.pyplot as plt
from numpy import linspace
from scipy.integrate import solve_ivp



def solve_ODE(initial_pos, velocity, mu, start_time, end_time, number_of_points):
    
    
    if isinstance(mu,(int,float))!=True or mu < 0: # μ should be positive real number
        try:
            raise Exception("The parameter needs to be a positive real number")
        except Exception as inst:
            print(type(inst))
            print(inst)
        return None
    

    def vdp_derivatives(k, z):
        """It takes two arguments: time t and state variable z=[x, y]"""
        # k: Time interval i.e t
        x=z[0]
        y=z[1]
        return [y, mu * (1 - x ** 2) * y - x]

    t = linspace(start_time,end_time,number_of_points)

    """ t_span: Interval of integration ,y0: Initial state , t_eval: Times at which to store the computed solution """
    res = solve_ivp(fun=vdp_derivatives, t_span=[start_time,end_time], y0=[initial_pos, velocity], t_eval=t)
    #print(res)
    #print(res.y[1])
    #print(res.y[0])
    #res.t contain time points and res.y : Values of the solution at t. y[0]=position over time and y[1]=velocity over time
    sol = res.y[0] # Extracting the position values from the solution

    # Plotting the curve
    plt.title(f"Van der Pol equation for μ = {mu}")
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.plot(t, sol)
    plt.grid()
    plt.show()

    
    p1 = -1 ## Check for 2nd crossing point
    for i in range(number_of_points - 1, 0, -1):
        if sol[i] <= 0 and sol[i - 1] >= 0: # Checking if the position changes sign from negative to positive
            p1 = i
            #print(p1)
            break

    p2 = -1 # Check for 2nd crossing point
    for i in range(p1 - 1, 0, -1): 
        if sol[i] <= 0 and sol[i - 1] >= 0: # Checking if the position changes sign again from negative to positive
            p2 = i
            #print(p2)
            break

    # Time period of the curve will be the difference in time values at the two crossing points
    timePeriod = abs(t[p1] - t[p2]) # Evaluating the Time Period
    print(f"The time period of above curve for μ = {mu} is {timePeriod:.2f}")

solve_ODE(0,10,3,0,30,10000)