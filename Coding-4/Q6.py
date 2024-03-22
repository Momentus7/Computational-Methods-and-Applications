import numpy as np
import matplotlib.pyplot as plt

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

    def area(self, a, b):
        """
        Returns the area under the polynomial in the interval [a, b]
        """
        # Checking input
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise Exception("Invalid input - Expected scalar")
        if a > b:
            raise Exception("for [a,b] interval b should be greater than equal to a")
        result_coff = [0]
        for i in range(len(self.cof)):
            result_coff.append(self.cof[i] / (i + 1))
        p=Polynomial(result_coff)
        return f"Area in the interval [{a}, {b}] is: {(p[b] - p[a]):.2f}"
p = Polynomial([1, 2, 3])
pd = p.derivative()
print(pd)

p = Polynomial([1, 2, 3])
print(p.area(1,2))
