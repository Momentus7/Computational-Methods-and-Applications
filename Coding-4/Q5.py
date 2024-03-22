import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
t=[]
s=[]
q=[]
actual=[]

fun=lambda x: 2*x*np.exp(x**2)

x=np.linspace(0,3,100)
for i in range(len(x)):
    m=np.linspace(0,x[i],100) # array to use in trapezoid and simpson
    y=fun(m)
    ti=scipy.integrate.trapz(y,m)
    si=scipy.integrate.simps(y,m)
    qi=scipy.integrate.quad(fun,0,x[i])
    actual.append(np.exp(x[i]**2)-np.exp(1)) # original value of the integration
    t.append(ti) # trapezoidal approximation
    s.append(si) # simpson's approximation
    q.append(qi[0]) # Quadrature rule
fig,ax=plt.subplots()
#Comment each method to see visualisation of each method as all curves gathers at nearly same value
ax.plot(x,s,"y",label="Simpson")
ax.plot(x,q,"r",label="Quadrature")
ax.plot(x,t,"b",label="Trapezoidal")
ax.plot(x,actual,"g",label="Real")
ax.axhline(np.exp(3**2)-np.exp(1),label="Actual")
ax.set_xlabel("Interval ")
ax.set_ylabel("Value of the integration")
ax.set_title("Numerical integration by different methods")
plt.grid()
ax.legend()
plt.show()