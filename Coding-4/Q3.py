import math
import matplotlib.pyplot as plt
import numpy as np

n=100 #Number of intervals
def derivative(x): 
    # Derivative of function
    return math.cos(x**2)*2*x
    
def double_derivative(x):
    #Double Derivative of function
    return 2*math.cos(x**2) -  4*(x**2)*math.sin(x**2)


def triple_derivative(x):
    #Triple Derivative of function
    return -12*x *math.sin(x**2) - 8 *(x**3)* math.cos(x**2)

x=np.linspace(0,1,n); # Generate n points between 0 and 1
y=[]
h_value=np.linspace(0.0001,1,n) # Removing h=0 to handle divided by zero warning
y_forward_app = []
y_centered_app = []
y_forward_thr = []
y_centered_thr = []

for h in h_value:
    max_fa = 0 
    max_ca = 0 
    max_ft = 0
    max_ct = 0
    for i in x:
        #absolute error for  forward finite difference approximation
        max_fa = max(max_fa, abs((math.sin((i+h)**2)-math.sin(i**2))/h - derivative(i))) 
        #absolute error for  centered finite difference approximation
        max_ca = max(max_ca, abs((math.sin((i+h)**2)-math.sin((i-h)**2))/(2*h) - derivative(i)))

        max_double_derivative_value = 0
        max_triple_derivative_value = 0
        m=np.linspace(i, i + h, n) # Generate n points between i and i+h 
        for j in m:
            #Take maximum double derivative for each i
            max_double_derivative_value = max(max_double_derivative_value, abs(double_derivative(j)))
            #Take maximum triple derivative for each i
            max_triple_derivative_value = max(max_triple_derivative_value, abs(triple_derivative(j)))
        #Maximum absolute error for Theoretical forward approximation
        max_ft = max(max_ft, (h / 2) * max_double_derivative_value)
        #Maximum absolute error for Theoretical centered approximation
        max_ct = max(max_ct, ((h**2) / 6) * max_triple_derivative_value )

    y_forward_app.append(max_fa)
    y_centered_app.append(max_ca)
    y_forward_thr.append(max_ft)
    y_centered_thr.append(max_ct)

    
plt.xlabel("Value of h")
plt.ylabel("Maximum absolute error")
    

plt.plot(h_value, y_forward_app, color="red", label="Forward approximation")
plt.plot(h_value, y_centered_app, color="blue", label="Centered approximation")
plt.plot(h_value, y_forward_thr, color="yellow", label="Theoretical forward approximation")
plt.plot(h_value, y_centered_thr, color="green", label="Theoretical centered approximation")

plt.legend(loc="upper left")
plt.grid()
plt.show()