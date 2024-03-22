import math
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return x + math.exp(x)

# Define the derivative of f(x)
def df(x):
    return 1 + math.exp(x)

# Define the Secant method
def secant_method(f, x0, x1, tol):
    x = x1
    x_prev = x0
    l=[]
    i=0
    counter=[]
    while f(x_prev)>tol:
        fx = f(x)
        fx_prev = f(x_prev)
        dx = fx * (x - x_prev) / (fx - fx_prev)
        x_prev = x
        x = x - dx
        l.append(x)
        counter.append(i)
        i+=1
    return l,counter

# Define the Newton-Raphson method
def newton_raphson_method(f, df, x0, tol):
    x = x0
    l = []
    counter=[]
    i=0
    while f(x)>tol:
        fx = f(x)
        dfx = df(x)
        dx = fx / dfx
        x = x - dx
        l.append(x)
        counter.append(i)  
        i+=1
    return l,counter

# Set the initial values and tolerances
x0 = 0
x1 = 1
tol = 10**(-8)

# Apply the Secant method and Newton-Raphson method
secant, secant_iter = secant_method(f, x0, x1, tol)
newton, newton_iter = newton_raphson_method(f, df, x0, tol)
# Plot the convergence rates
plt.plot(secant_iter,secant,'g',label="Secant Method")
plt.plot(newton_iter,newton,'y--',label="Newton raphson method")
plt.legend()
plt.show()
