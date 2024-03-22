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

    # Method to plot the polynomial in the given range
    def show(self, a, b):
        x = np.linspace(a, b, 100)
        y = [self[x_i] for x_i in x] # Call getitem and compute polynomial
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('P(x)')
        plt.grid()
        s=""
        for i, c in enumerate(self.cof):
            if(i!=0):
                s+=f"{c}x^{i} "
            else:
                s+=f"{c} "
        plt.title(f'Plot of the polynomial {s}')
        plt.show()

    # Method to plot the polynomial in the given range with interpolation points
    def show1(self, a, b):
        x = np.linspace(a, b, 100)
        y = [self[x_i] for x_i in x] #Call getitem and compute polynomial
        x1=[-1,0,1,2,3]
        y1=[self[x_i] for x_i in x1]
        plt.plot(x, y)
        plt.plot(x1,y1,'ro', markersize=5)
        plt.xlabel('x')
        plt.ylabel('P(x)')
        plt.grid()
        plt.title("Polynomial interpolation using matrix method")
        plt.show()
        
    # Method to fit the polynomial using Matrix Mehod    
    def fitViaMatrixMethod(self, points):
        if not isinstance(points, list):
            raise Exception("Invalid input - Expected list of tuples")
        n = len(points)
        A =[[0 for i in range(n)] for i in range(n)] # Create n*n zero Matrix
        B =[0]*n
        for p in points:
            x = [px[0] for px in points] #Separate x points
            y = [py[1] for py in points] #Separate y points
        for i in range(n):
            for j in range(n):
                #f(xi)=0+xi+xi^2+...for all xi 
                A[i][j] = x[i]**j #Putting value 0,1,2... and create n euation A[i][j] is ith equation j represents degree
        X = np.linalg.solve(A, y) #Solve for Ay=X and find X
        self.cof =X.tolist()
        self.show1(min(x),max(x))
    def fitViaLagrangePoly(self,point_val):
        self.p_val=point_val # Store the input points in the p_val instance variable
        # Initialize the x_value and y_value lists
        x_value = []
        y_value = []
        numer={} # Initialize the numer dictionary to store the numerator of the Lagrange method
        denom=[] # Initialize the denom list to store the denominator of the Lagrange method
        l=1
        # Extract the x and y values from the input points
        for i in range(len(self.p_val)):
            x_value.append(self.p_val[i][0])
            y_value.append(self.p_val[i][1])
        # Initialize the numer dictionary by passing 1 as the coefficient
        for i in range(len(self.p_val)):
            numer[i] = Polynomial([1])
        poly=Polynomial([1]) # Initialize the poly variable with a Polynomial object with 1 as the coefficient
        
        
        # Calculate the numerator and denominator of the Lagrange method
        for i in  range(len(self.p_val)):
            for j in range(len(x_value)):
                # If i and j are different
                if i!=j:
                    # Create a Polynomial object with -x_value[j] and 1 as cof
                    p=Polynomial([-x_value[j],1]) #coefficient 1 is added to represent the linear term x 
                    # Denominator Value
                    l=l*(x_value[i]-x_value[j])
                    poly=poly*p
            # Store the polynomials in the numer dictionary
            numer[i]=numer[i]*poly 
            # Add the denominator to the denom list
            denom.append(l)
            # Reset the poly variable with a Polynomial object with 1 as the coefficient
            poly=Polynomial([1])
            # Reset the l variable to 1
            l=1

        # Initialize the l variable with a Polynomial object with 0 as the coefficient
        l=Polynomial([0])
        # Estimate the polynomial using the Lagrange method P(x)=f(0)*y_0+f(1)*y_1+ ..
        for i in range(len(y_value)):
            l=l+y_value[i]*((1/denom[i])*numer[i]) 
    
        # Create a 100 evenly spaced samples between the minimum and maximum x values
        x=np.linspace(min(x_value),max(x_value),100)
        # Evaluate the polynomial for each x value
        y=[l[i] for  i in x]
        # Plot the polynomial
        plt.plot(x, y)
        # Plot the input points as red dots
        plt.plot(x_value,y_value,"ro",markersize=5)
        # Label the y axis as "p(x)"
        plt.ylabel("p(x)")
        # Label the x axis as "x"
        plt.xlabel("x")
        #Set title as "Polynomial interpolation using Lagrange method"
        plt.title("Polynomial interpolation using Lagrange method")
        #Plot within grid
        plt.grid()
        plt.show()

p = Polynomial([1, 2, 3])
print(p)
p1 = Polynomial([1, 2, 3])
p2 = Polynomial([3, 2, 1])
p3 = p1 + p2
print(p3)
p1 = Polynomial([1, 2, 3])
p2 = Polynomial([3, 2, 1])
p3 = p1 - p2
print(p3)
p1 = Polynomial([1, 2, 3])
p2 = (-0.5)*p1
print(p2)
p1 = Polynomial([-1, 1])
p2 = Polynomial([1, 1, 1])
p3 = p1 * p2
print(p3)
p = Polynomial([1, 2, 3])
print(p[2])
p = Polynomial([1, -1, 1, -1])
p.show(-1, 2)
p = Polynomial([])
p.fitViaMatrixMethod([(1,4), (0,1), (-1, 0), (2, 15), (3,12)])
p = Polynomial([])
p.fitViaLagrangePoly([(1,-4), (0,1), (-1, 4), (2, 4), (3,1)])