import numpy as np
import math
import matplotlib.pyplot as plt
import random

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
    def listCoefficient(self):
        """
        Returns list of coefficient by finding the coeffecients of the polynomial
        """
        c=[]
        for i in self.cof:
            c.append(i)
        return c;
    
    def Aberth(self, l,eps):
        p = Polynomial([1])
        for i in l:
            p = p * Polynomial([-i, 1])

        c = p.listCoefficient()
        deg = len(c) - 1  
        dp = p.derivative()
        # Find the upper limit for the Aberth method 
        max1=0;
        for x in range(deg):
            max1=max(abs(c[x]),max1)
        upper_limit=1+1/abs(c[-1])*max1;
        # Find the lower limit for the Aberth method 
        max2=0
        for x in range(1, deg + 1):
            max2=max(abs(c[x]),max2)
        lower_limit = abs(c[0]) / (abs(c[0]) + max2);
            
        # Apply Aberth method by randomly choosing an estiamate for the roots within the lower and upper limit
        roots = []

        for i in range(deg):
            r = random.uniform(lower_limit, upper_limit)
            theta = random.uniform(0, 2*math.pi)
            root = complex(r * math.cos(theta), r * math.sin(theta))
            roots.append(root)
        k = 0
        while k < 1/eps:

            for i in range(len(roots)):
                p_by_dp = p[roots[i]] / dp[roots[i]]
                sum1=0;
                for j in (roots):
                    if j != roots[i]:
                        sum1=sum1+(1 / (roots[i] - j))
                s = p_by_dp / (1 - (p_by_dp*sum1))

                roots[i] -= s
            k += 1
        print(p)
        print("The approximated roots are :", roots)


q = Polynomial([0])
q.Aberth([1, 3, 5, 7, 9],0.001)