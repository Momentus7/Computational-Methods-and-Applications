import numpy as np
import matplotlib.pyplot as plt
import random

# Function to visualize_convergence for Gauss-Siedel method and Jacobi method 
def visualize_convergence(n, b, m):
    # create a diagonally row dominant square matrix
    A = [[0 for i in range(n)] for j in range(n)] # Create n*n matrix
    for i in range(n):
        s=0;
        for j in range(n):
            if(i!=j):
                rand1=random.uniform(0, 5)
                A[i][j] = rand1;
                s=s+rand1;
        A[i][i] = s+1 #To satisfy diagonally row dominant
    #For Jacobi method   
    x = [0] * (n); #Initially taking every value as 0 for 1st iteration
    err_j = [] #For storing Jacobi error
    for k in range(m):
        x_new = [0]*(n) # Creating a list of lenth self.n
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j] # Computed the value by taking Augumented matrix
            x_new[i] = (b[i] - s) / A[i][i] # Divide by dominant diagonal element
        x = x_new # New updated value of variables for next iteration
        err_j.append(np.linalg.norm(np.dot(A, x) - b)) # ||Ax⁽ᵏ⁾ - b||₂
        
    #Gauss-Siedel method
    x = [0]*(n); #Initially taking every value as 0 for 1st iteration
    err_gs = [] #For Storing Gauss-Siedel error
    for k in range(m):
        x_new = [0]*(n) # Creating a list of lenth self.n
        for i in range(n):
            s = 0
            for j in range(i):
                s += A[i][j] * x_new[j] #Use the already computed value for further computed
            for j in range(i + 1,n):
                s += A[i][j] * x[j]  # x_new is not calculated so use x[j]
            x_new[i] = (b[i] - s) / A[i][i]
        x = x_new # After each iteration append the copy computed value to x
        err_gs.append(np.linalg.norm(np.dot(A, x) - b)) # ||Ax⁽ᵏ⁾ - b||₂
    
    # plot the results
    #print(err_j)
    #print(err_gs)
    plt.plot(range(m), err_j, label='Jacobi')
    plt.plot(range(m), err_gs, label='Gauss-Siedel')
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.title('Rate of Convergence')
    #plt.ylim(0,100)
    plt.legend()
    plt.show()

b = [1, 2, 3, 4]
visualize_convergence(len(b),b,80)