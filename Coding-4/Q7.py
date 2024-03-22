import numpy as np
import math
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
        
        #Returns the derivative of the polynomial

        # Calculating the coefficients of the derivative polynomial
        result_coff = []
        for i in range(1, len(self.cof)):
            result_coff.append(i * self.cof[i])
        return Polynomial(result_coff)

    def area(self, a, b): 
        #Returns the area under the polynomial in the interval [a, b]
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise Exception("Invalid input - Expected scalar")
        if a > b:
            raise Exception("for [a,b] interval b should be greater than equal to a")
        result_coff = [0] # in integration degree of polynomial increases by 1
        #Integrate the polynomial
        for i in range(len(self.cof)):
            result_coff.append(self.cof[i] / (i + 1))
        p=Polynomial(result_coff)
        return p[b]-p[a]
p = Polynomial([0,1,1,1/3,0,-1/30,-1/90,-1/630,0,1/22680,1/113400]) # Taking taylor's coefiicient
by_taylor =p.area(0,0.5)
by_int = (math.exp(1/2)*(math.sin(1/2)-math.cos(1/2))/2) - (math.exp(0)*(math.sin(0)-math.cos(0))/2) # Compute using integration
print("Area under the curve is using taylor's series :", by_taylor)
print("The actual area under the curve is:", by_int)
if(abs(by_int-by_taylor)<=(10**-6)): #Check for error tolerance
    print(f"Area computed using taylor's series is within a guaranteed error of 10^-6, error is: {(abs(by_int-by_taylor))} ")
else:
    print(" Not within guaranteed error of 10^-6")
    

