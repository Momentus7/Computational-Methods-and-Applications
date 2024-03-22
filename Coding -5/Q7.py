import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import math


# Fourier approximation of nth degree for the  function e^x
def Fourier_Approx(n):
    ak = []
    bk = []

    for k in range(n + 1):
        s = lambda x: np.exp(x) * np.cos(k * x)  # function for ak
        r = lambda x: np.exp(x) * np.sin(k * x)  # function for bk
        ak.append((1 / np.pi) * list(integrate.quad(s, -np.pi, np.pi))[0])  # storing integration value and ignoring error
        bk.append((1 / np.pi) * list(integrate.quad(r, -np.pi, np.pi))[0])  # storing integration value and ignoring error
    # printing the co-effecients ak and bk
    print("The co-effecients are as follows:")
    for i in range(len(ak)):
        print("a",i," : ",round(ak[i],8),"  b",i," : ",round(bk[i],8) )
    x = np.linspace(-np.pi,np.pi,400)
    s_n = []
    for i in x: # Compute Sn for all value in x
        s = ak[0] / 2 # First term is a0/2
        for j in range(1, n + 1): # For each value in x compute summation from 1 to n
            s = s + (ak[j] * np.cos(i * j)) + (bk[j] * np.sin(j * i))
        s_n.append(s)
    y = [np.exp(i) for i in x]
    plt.plot(x, y,"r",label="Actual")
    plt.plot(x, s_n,"y",label="Fourier approximation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Actual plot vs Fourier approximation of e^x")
    plt.grid()
    plt.legend()
    plt.show()


Fourier_Approx(10)
