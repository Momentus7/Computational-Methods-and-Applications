import numpy as np
import math
import matplotlib.pyplot as plt

# The given function
def F(x):
    l=[3 * x[0] - math.cos(x[1] * x[2]) - 3 / 2,4 * x[0] ** 2 - 625 * x[1] ** 2 + 2 * x[2] - 1, 20 * x[2] + np.exp(-x[0] * x[1]) + 9]
    return np.array(l)

# Jacobian  function
def J(x):
    l=[[3, x[2] * math.sin(x[1] * x[2]), x[1] * math.sin(x[1] * x[2])],[8 * x[0], -1250 * x[1], 2], [-x[1] * np.exp(-x[1] * x[0]), -x[0] * np.exp(-x[1] * x[0]), 20]]
    return np.array(l)
def newtonRaphson(F, J, x): #x_{k+1}= x_k -J(x_k)^{-1}*F(x_K)
    fx = F(x)
    f_norm = np.linalg.norm(fx, ord=2)  # Norm of order 2
    norm = []
    l = []
    k = 0
    eps=0.000001
    # calculation for the norm
    while abs(f_norm) > eps:
        delta_x = np.linalg.solve(J(x), -fx) # (x_k+1-x_k)*j(x_k) - f(x_k) = 0
        #print(delta_x)
        x = x + delta_x
        #print(x)
        fx = F(x)
        f_norm = np.linalg.norm(fx, ord=2)
        norm.append(f_norm)
        k += 1
        l.append(k)

    print(f" Final Solution vector is {x}  ")
    plt.plot(l, norm, "g", label="Convergence using Newton Raphson") # ploting no. of iterations vs norm value
    plt.xlabel("Number of iterations")
    plt.ylabel("Norm Values")
    plt.title("Norm values vs number of iterations")
    plt.grid()
    plt.legend()
    plt.show()

newtonRaphson(F, J, [1, 1, 1])