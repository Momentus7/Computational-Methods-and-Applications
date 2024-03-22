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
            new_coef[i]=self.cof[i]
        for i in range(len(other.cof)):
            new_coef[i]-=other.cof[i]
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
    def Chebyshev_polynomial(self,n):
        if type(n)!=int and n<=0:
            raise Exception("Expect a non-negetive integer")
        a=Polynomial([1]) # First element = 1 
        b=Polynomial([0,1]) # Second Element = x
        h=Polynomial([0,1]) # Polynomial x
        
        if(n==1):
            print(a)
        elif(n==2):
            print(b)
        else:
            k=Polynomial([0])
            for i in range(n-1):
                k=2*h*b-a # 2xTn(x) − Tn−1(x)
                a=b; # Update a
                b=k; # Update b
            print(k)
            
n=int(input("Enter the value of n  to compute the nth Chebyshev polynomial :  "))
p=Polynomial([0])
p.Chebyshev_polynomial(n)
            