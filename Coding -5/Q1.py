import numpy as np
import matplotlib.pyplot as plt
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
    def best_fit(self,points,deg):
        """∑y=an+b∑x+c∑x2
            ∑xy=a∑x+b∑x2+c∑x3
            ∑x2y=a∑x2+b∑x3+c∑x4"""
        if type(deg)!=int and deg<0:
            raise Exception("Expect a non-negative integer")
        no_of_points=len(points); # Number of points
        x_points=[] # Separates x_axis points
        y_points=[] # Separates y_axis points
        for i in range(no_of_points):
            x_p=points[i][0]
            y_p=points[i][1]
            if isinstance(x_p, (int, float)) and deg>=0: # Checks if coordinate is of form int or float
                x_points.append(x_p)
            else:
                raise Exception("Point coordinates in x not possible") # Raise Exception if not of form int or float
            
            if isinstance(y_p, (int, float)) and deg>=0: # Checks if coordinate is of form int or float
                y_points.append(y_p)
            else:
                raise Exception("Point coordinates in y not possible")# Raise Exception if not of form int or float
        A=[[0 for i in range(deg+1)]for j in range(deg+1)] # (deg+1)*(deg+1) matrix
        B=[0 for i in range(deg+1)] # (1)*(deg+1) matrix
        for i in range(deg+1):
            for j in range(deg+1):
                #Update A[i][j] value as per equation
                if i==0 and j==0:
                    A[i][j]=no_of_points;
                else:
                    A[i][j]=sum([x**(i+j) for x in x_points])
        print(A)
        for i in range(deg+1):
            #Update B matrix
            B[i]=sum([j[1]*(j[0])**i for j in points])
        print(B)
        x = np.linalg.solve(A, B) #Solve for X in AX=B 
        p=Polynomial(x) # Pass the x as an argument coefficent to Polynimial object
        x_min=min(x_points)
        x_max=max(x_points)
        x1=np.linspace(x_min,x_max,200)
        y1=[]
        for i in x1:
            y1.append(p[i])
        plt.plot(x1,y1,label="Best-fit polynomial")
        plt.plot(x_points,y_points,"yo",label="Actual Points")
        plt.grid()
        plt.title("Best-fit Polynomial Approximation")
        plt.legend()
        plt.show()           
p=Polynomial([0])
p.best_fit([(1,-5),(2,-2),(3,5),(4,16),(5,31),(6,50),(7,73)],2)