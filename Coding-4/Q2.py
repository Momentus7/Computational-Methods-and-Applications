import math
import matplotlib.pyplot as plt
import numpy as np
n=int(input("Enter number of points   :   "))
x=np.linspace(0,1,n); # Generate n points between 0 and 1
y=[]
f=[]
b=[]
c=[]
h=0.01 # step size h for forward difference approximation
for i in x:
    y.append((math.cos(i**2))*2*i) # Compute actual derivative using the chain rule
    f.append((math.sin((i+h)**2)-math.sin(i**2))/h)  # Compute  forward finite difference approximation
    b.append((math.sin(i**2)-math.sin((i-h)**2))/h)  # Compute  Backward finite difference approximation
    c.append((math.sin((i+h)**2)-math.sin((i-h)**2))/(2*h)) # Compute  Centered finite difference approximation
error_fd=[]
error_bd=[]
error_cd=[]
for i in range(len(y)):
    error_fd.append(abs(y[i]-f[i])) # Compute absolute error for  forward finite difference approximation
    error_bd.append(abs(y[i]-b[i])) # Compute absolute error for  backward finite difference approximation
    error_cd.append(abs(y[i]-c[i])) # Compute absolute error for  centered finite difference approximation
plt.plot(x,error_fd,color="red",label="Forward Difference error")
plt.plot(x,error_cd,color="blue",label="Centered difference error")
plt.plot(x,error_bd,color="yellow",label="Backward difference error")
plt.ylim(0.000,0.014)
plt.xlabel("Value of x")
plt.ylabel("Error in estimation")
plt.grid()
plt.legend()
plt.show()