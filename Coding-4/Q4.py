import matplotlib.pyplot as plt
import numpy as np
import math
a=1 # Interval start value
b=3 # Interval limit value
M=100 # Number of intervals
def fun(x):
    #Return function
    ans=(2*x)*math.exp(x**2)
    return ans
def integration(x):
    #Return Integration of function
    ans=math.exp(x**2)
    return ans

x_interval=[]
area_trap = []

for i in range(1,M+1):
    x_interval.append(i)
    delta_x=(b-a)/i; # Calculate Delta value
    x=np.linspace(a,b,i) # Generate i points between a nand b
    fx_value=0; # For each value in interval set f(x)=0
    for j in x:
        #Compute f(x) for each interval value i.e i
        if j==a or j==b: #For 1st and last f(x) its scalar multiple of 1
            fx_value+=fun(j) 
        else:
            fx_value+=2*fun(j)
    fx_value*= delta_x/2; #Final f(x)=individual f(x)*delta/2
    area_trap.append(fx_value)
plt.plot(x_interval,area_trap,label=" Estimate of area using Trapezoidal rule")
plt.grid(True)
plt.axhline(integration(b)-integration(a),color="r",label="Actual Area")
plt.xlabel("No of intervals")
plt.ylabel("Area")
plt.title("Area under the curve ")
plt.legend()
plt.show()
    