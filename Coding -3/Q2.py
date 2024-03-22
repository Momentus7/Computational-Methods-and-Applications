import random
import numpy as np
import math
class RowVectorFloat:
    # The __init__ method initializes the RowVectorFloat object with a vector
    def __init__(self,vector):
        self.vector=vector;

    # The __str__ method returns the string representation of the RowVectorFloat object
    def __str__(self):
        s=""
        for i in self.vector:
            s+=f"{i} ";
        return s;

    # The __len__ method returns the length of the vector in the RowVectorFloat object
    def __len__(self):
        l=len(self.vector);
        return l;

    # The __getitem__ method returns the element at the given index of the vector in the RowVectorFloat object
    def __getitem__(self, n): 
        return self.vector[n];

    # The __setitem__ method sets the element at the given index of the vector in the RowVectorFloat object to the given value
    def __setitem__(self, n,value):
        self.vector[n]=value;

    # The __add__ method overloads the '+' operator to allow vector addition of two RowVectorFloat objects
    def __add__(self, other):
        if len(self.vector)==len(other.vector):
            sol=[]
            for i,j in zip(self.vector,other.vector):
                sol.append(i+j);
            return RowVectorFloat(sol);
        else:
            raise Exception("Vector addition is not possible")

    # The __mul__ method overloads the '*' operator to allow scalar multiplication of a RowVectorFloat object
    def __mul__(self,scalar):
        sol=[]
        for i in self.vector:
            sol.append(scalar*i);
        return RowVectorFloat(sol)

    # The __rmul__ method overloads the '*' operator to allow scalar multiplication of a RowVectorFloat object in the reverse order
    def __rmul__(self,n):
        sol=[]
        for i in self.vector:
            sol.append(n*i);
        return RowVectorFloat(sol)
        
class SquareMatrixFloat:
    # Constructor to initialize the matrix with all zeros
    def __init__(self, n):
        self.n = n
        # Creating a list of n row vectors of length n and initializing it with all zeros
        self.matrix = [RowVectorFloat([0] * n) for i in range(n)]
    
    # Function to print the matrix as a string
    def __str__(self):
        s = "The matrix is:\n"
        # Iterating over each row and adding it to the string
        for i in range(self.n):
            s+="{k}\n".format(k=self.matrix[i])
        return s
    
    # Function to sample a symmetric matrix
    def sampleSymmetric(self):
        # Iterating over the matrix diagonally
        for i in range(self.n):
            for j in range(i, self.n):
                # If the diagonal element is being processed, generate a random number for it
                if i == j:
                    m=random.uniform(0, self.n)
                    self.matrix[i][j] = round(m,2)
                # If any other element is being processed, generate a random number and assign it to both symmetric elements
                else:
                    rand1 = random.uniform(0, 1)
                    self.matrix[i][j]=round(rand1,2)
                    self.matrix[j][i]=round(rand1,2)
    
    # Function to convert the matrix to row echelon form
    def toRowEchelonForm(self):
        # Iterating over each element of the matrix
        for k in range(self.n):
            for i in range(k+1, self.n):
                # Computing the factor by which the ith row has to be multiplied to eliminate the kth element in the ith row
                factor = self.matrix[i][k]/self.matrix[k][k]
                for j in range(k, self.n):
                    # Computing the term that is to be subtracted from the ith row to eliminate the kth element
                    m=factor * self.matrix[k][j]
                    self.matrix[i][j] =round(self.matrix[i][j]-m,2)
                    #print(self.matrix)
        # Replacing any -0.0 in the matrix with 0.00
        for i in range(self.n):
            for j in range(self.n):
                if(self.matrix[i][j]==0.0 or self.matrix[i][j]==-0.0):
                    self.matrix[i][j]=0.00;
    
    # Function to check if the matrix is diagonally dominant
    def isDRDominant(self):
        # Iterating over each row of the matrix
        for i in range(self.n):
            sum = 0
            # Iterating over each element of the ith row except the diagonal element
            for j in range(self.n):
                if i != j:
                    # Adding the absolute value of the element to the sum
                    sum += abs(self.matrix[i][j])
            # If the absolute value of the diagonal element is less than or equal to the sum of the absolute values of the other elements, the matrix is not diagonally dominant
            if abs(self.matrix[i][i]) <= sum:
                return False
        return True
    
    # Function to solve a system of equations using Jacobi method
    def jSolve(self, b, m): 
        if not self.isDRDominant(): #Requireed condition  diagonally row dominant.
            try:
                raise Exception("Not solving because convergence is not guaranteed.")
            except Exception as l:
                print(type(l))
                print(l)
        else:
            x = [0] * (self.n); #Initially taking every value as 0 for 1st iteration
            err = [] #For storing error
            for k in range(m):
                x_new = [0]*(self.n) # Creating a list of lenth self.n in Jacobi x_new is same as x
                for i in range(self.n):
                    s = 0
                    for j in range(self.n):
                        if i != j:
                            s += self.matrix[i][j] * x[j] # Computed the value by taking Augumented matrix
                    x_new[i] = (b[i] - s) / self.matrix[i][i] # Divide by dominant diagonal element
                x = x_new # New updated value of variables for next iteration
                err.append(np.linalg.norm(np.dot(self.matrix, x) - b)) # ||Ax⁽ᵏ⁾ - b||₂
            return (err, x) # Return error at each iteration with final updated value of x
        
        
    # Function to solve a system of equations using Gauss-Siedel method
    def gsSolve(self, b, m): 
        x = [0]*(self.n); #Initially taking every value as 0 for 1st iteration
        err = [] #For Storing error
        for k in range(m):
            x_new = [0]*(self.n) # Creating a list of lenth self.n
            for i in range(self.n):
                s = 0
                for j in range(i):
                    s += self.matrix[i][j] * x_new[j] #Use the already computed value for further computed
                for j in range(i + 1, self.n):
                    s += self.matrix[i][j] * x[j]  # x_new is not calculated so use x[j]
                x_new[i] = (b[i] - s) / self.matrix[i][i]
            x = x_new # After each iteration append the copy computed value to x
            err.append(np.linalg.norm(np.dot(self.matrix, x) - b)) # ||Ax⁽ᵏ⁾ - b||₂
        return (err, x) # Return error at each iteration with last updated value
    

s = SquareMatrixFloat(4)
print(s)
s.sampleSymmetric()
print(s)
(err, x) = s.gsSolve([1, 2, 3, 4], 10)
print("Gauss-Siedel method")
print(x)
print("Error")
print(err)

