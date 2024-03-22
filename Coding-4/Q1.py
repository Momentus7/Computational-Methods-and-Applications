import math
import matplotlib.pyplot as plt
import numpy as np
n=int(input("Enter number of points for viaulaisation of derivation of sin(x^2)   :   "))
x=np.linspace(0,1,n); # Generate n points between 0 and 1
y=[]
z=[]
h=0.01  # step size h for forward difference approximation
for i in x:
    # Compute actual derivative using the chain rule 
    y.append(math.cos(i**2)*2*i)
    # Compute approximated derivative using forward finite difference approximation
    z.append((math.sin((i+h)**2)-math.sin(i**2))/h)   
plt.plot(x,y,color="red",label="Actual Derivative value")
plt.plot(x,z,color="green",label="Forward finte difference approximation")
plt.xlabel("Value of x")
plt.ylabel("Derivation of sin(x^2)")
plt.title("viaulaisation of derivation of sin(x^2)")
plt.grid()
plt.legend()
plt.show()