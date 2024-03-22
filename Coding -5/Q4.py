import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import math

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

    
    
    def derivative(self):
        """
        Returns the derivative of the polynomial
        """
        # Calculating the coefficients of the derivative polynomial
        result_coff = []
        for i in range(1, len(self.cof)):
            result_coff.append(i * self.cof[i])
        return Polynomial(result_coff)
    
    def LegendrePolynomial(self,n):
        if type(n)==int:
            p = Polynomial([-1, 0, 1]) # defining (x^2-1)
            s = Polynomial([1])
            # Multiplying the polynomial n times
            for i in range(n):
                s = s * p
            #print(s)
            # Differentiating the polynomial n times
            for i in range(n):
                s = s.derivative()
            l = (1 / ((2 ** n) * math.factorial(n))) * s
            # Printing the nth legendre polynomial
            return l
        else:
            raise Exception("n Should be an integer")
    def legend_approx(self, degree):
        # To approximate using nth degree legendre polynomial
        if type(degree)!=int and degree<0:
            raise Exception("Degree should be non-negetive integer")
        p = Polynomial([0])
        lc = [] # creating a list of co-effecients
        for i in range(degree + 1):
            # function for calculating cj
            f1 = lambda x: p.LegendrePolynomial(i).calculate_value(x)**2
            # function for calculation of aj
            f2 = lambda x: p.LegendrePolynomial(i).calculate_value(x)*np.exp(x)
            cj = list(integrate.quad(f1, -1, 1))[0]
            aj = list(integrate.quad(f2, -1, 1))[0]
            # divding aj with cj
            ck = (1 / cj) * aj
            lc.append(ck)
        #print(lc)
        # estimating the polynomial
        p1 = Polynomial([0])
        for i in range(degree + 1):
            #e^x=summation(ck*pk(x))
            p1 = p1 + lc[i] * p.LegendrePolynomial(i)
        #print(p1)

        x = np.linspace(-1, 1,500)
        # setting up a polynomial object to valuate a value at points and
        # using it in a plot
        y = [p1[i] for i in x] # Legendre y_value
        z = [np.exp(i) for i in x] # Actual y value

        plt.plot(x, z, 'yo', label="Actual")
        plt.plot(x, y, 'g', label="Legendre fit")
        plt.xlabel("x")
        plt.ylabel("f(x)")

        plt.title("Legendre Polynomial fit vs actual plot")
        plt.legend()
        plt.grid()
        plt.show()

    #convert [c1,c2,c3] as c1+c2*x+c3*x^2
    def calculate_value(self, x):
        value = 0
        for i in range(len(self.cof)):
            value += (x**i)*self.cof[i]
        return value
p = Polynomial([0])
p.legend_approx(10)