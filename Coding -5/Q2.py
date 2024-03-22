import numpy as np
imprt math
import matplotlib.pyplot as plt
from scipy import integrate

class Polynomial:
    # Constructor to initialize the object with coefficients of the polynomial
    def __init__(self, cof):
        self.cof = cof

    # Override string method to print the polynomial coefficients
    def __str__(self):
        s="coefficients of the polynomial are:\n"
        for i in self.cof:
            s+=f"{i}  ";
        return s;
    
    # Override add method to add two polynomials
    def __add__(self, other):
        size=max(len(self.cof),len(other.cof))
        sum=[0 for i in range(size)]
        for i in range(0,len(self.cof)):
             sum[i]=self.cof[i]
        for i in range(len(other.cof)):
            sum[i]+=other.cof[i]
        return Polynomial(sum)     

    # Override subtract method to subtract two polynomials
    def __sub__(self, other):
        n=max(len(self.cof),len(other.cof))
        new_coef=[0]*n
        for i in range(len(self.cof)):
            new_coef[i]=self.cof[i]-other.cof[i]
        if(n>len(self.cof)):
            for i in range(len(self.cof),n):
                new_coef[i]=-other.cof[i]    
        return Polynomial(new_coef)

    # Override multiply method to multiply two polynomials or a polynomial with a scalar
    def __mul__(self, other):
        new_coef = []
        if isinstance(other, (int, float)):
            for i in range(len(self.cof)):
                new_coef.append(other*self.cof)
            return Polynomial(new_coef)
        elif isinstance(other, Polynomial):
            n = (len(self.cof) + len(other.cof) - 1)
            result = [0]*n
            for i, c1 in enumerate(self.cof): #enurate index,value
                for j, c2 in enumerate(other.cof):
                    result[i+j] += c1 * c2
            return Polynomial(result)
        else:
            raise Exception("Multiplication is not possible")
    
    # Override reverse multiply method to multiply a scalar with a polynomial
    def __rmul__(self, other):
        new_coef = []
        for i in range(len(self.cof)):
                new_coef.append(other*self.cof[i])
        return Polynomial(new_coef)

    # Override getitem method to compute the polynomial for a given value of x
    def __getitem__(self, x):
        result = 0
        for i, coef in enumerate(self.cof):
            result += coef * x**i
        return result
    
    def best_fit(self,deg):
        if type(deg)==int and deg>=0:
            A = np.zeros((deg+1, deg+1)) # (deg+1)*(deg+1) matrix
            B = np.zeros(deg+1) # (1)*(deg+1) matrix

            for i in range(deg+1):
                for j in range(deg+1):
                    #Update A[i][j] value as per equation
                    A[i][j] = integrate.quad(lambda x: x**(i+j), 0, np.pi)[0] # select the estimated value of the integral and discard the error bound.
            
            for i in range(deg+1):
                #Update B matrix as y(x)^i
                B[i] = integrate.quad(lambda x: (np.sin(x) + np.cos(x))*(x**i), 0, np.pi)[0] # select the estimated value of the integral
    
            x = np.linalg.solve(A, B) #Solve for X in AX=B 
            p = Polynomial(x) # Pass the x as an argument coefficient to Polynimial object
            x1 = np.linspace(0, np.pi, 200)
            y1 = np.sin(x1) + np.cos(x1) # The actual function
            y2=[]
            for x_p in x1:
                y2.append(p[x_p]) # The approximated function
    
            plt.plot(x1, y1,'yo',label="Actual function")
            plt.plot(x1, y2, label="Best-fit polynomial")
            plt.grid()
            plt.title("Best-fit Polynomial Approximation")
            plt.legend()
            plt.show()
        else:
            raise Exception("Degree should be a integer and greater than equal to 0")
p=Polynomial([p])
p.best_fit(6)