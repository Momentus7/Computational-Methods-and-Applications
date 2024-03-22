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
    
    def Aberth(self):
        p = Polynomial(self.cof)
        # Extract the coefficients of the polynomial
        c = p.listCoefficient()
        # Determine the degree of the polynomial
        deg = len(c) - 1 
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
        q = p.derivative()
        # Apply the Aberth method
        while k < 1000:

            for i in range(len(roots)):
                # Calculate p(roots[i]) / p'(roots[i])
                p_by_dp = p[roots[i]] / q[roots[i]]
                # Calculate the sum of 1 / (roots[i] - j) for j != roots[i]
                sum1=0;
                for j in (roots):
                    if j != roots[i]:
                        sum1=sum1+(1 / (roots[i] - j))
                # Calculate the new value of the root
                s = p_by_dp / (1 - (p_by_dp*sum1))

                roots[i] -= s
            k += 1
        #print(p)
        #print("The approximated roots are :", roots)
        return roots
    def find_root(self,f, a, b,esp):
        # Create an array of x values between a and b
        x = np.linspace(a, b, 10)
        # Evaluate the function f at each x value to get an array of y values
        y = []
        for i in x:
            y.append(f(i))
        # Fit a polynomial to the points (x[i], y[i])
        poly = np.polyfit(x, y, len(y) - 1)
        # Create a polynomial object using the coefficients of the fitted polynomial
        p = Polynomial(list(poly))
        # Use the Aberth method to find the roots of the polynomial
        roots = p.Aberth() 
        # Find the real roots within a small tolerance
        index = []
        for i in range(len(roots)):
            if round(roots[i].imag, 5) == 0:
                index.append(i)
        # Sort the real roots in increasing order
        l = []
        for i in range(len(roots)):
            for j in index:
                if j == i:
                    l.append(roots[i].real)
        l.sort()
        # Divide the interval [a, b] into subintervals that contain the roots
        l1 = [a]
        for i in range(len(l)):
            if (i == len(l) - 1):
                break
            l1.append((l[i] + l[i + 1]) / 2)
        l1.append(b)
        root_f = []
        for i in range(len(l1) - 1):
            if (f(l1[i]) * f(l1[i + 1]) < 0):
                r = round(self.bisection_method(f, l1[i], l1[i + 1],esp), 5)
                root_f.append(r)
        if len(root_f)==0:
            print("No roots found in the interval")
        else :
            print("Roots in the interval[",a,b,"] are :\n",root_f)

    # Bisection method
    def bisection_method(self,f,x,y,esp):
        k=int(1/esp)
        for i in range(0, k):
            m = (x+y) / 2
            fm = f(m)
            if f(x) * fm < 0:
                y = m
            elif f(y) * fm < 0:
                x = m
        return (x + y) / 2


p=Polynomial([0])
p.find_root(lambda x: np.cos(x), -np.pi,np.pi,0.001)

    

