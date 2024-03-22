import random
import math
import matplotlib.pyplot as plt

def estimatePi(n):
    inside = 0
    #Create 3 empty lists  
    x_points = []
    y_points = []
    fractions = []
    for i in range(1,n+1):
	#Taking 2 randomly number between -1 and 1
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        x_points.append(x)
        y_points.append(y)
        # Check if the point is inside the inscribed circle
        if x*x + y*y <= 1:
            inside += 1
        fractions.append(4*inside/i)
    # Calculate the estimated value of pi
    pi_estimate = 4 * inside/n
    print("Value of math.pi using Monte Carlo Method", pi_estimate)
    # Plot of Estimated Pi value using Monte Carlo Method
    plt.plot(range(1,n+1), fractions,label='Estimated Pi')
    #Adding horizental line corresponding to Actual Pi value
    plt.axhline(y=math.pi, color='r', label='Actual Pi')
    plt.title('Estimation of pi using Monte Carlo Method ')
    plt.xlabel('No. of points generated')
    plt.ylabel('4 * Fraction of points within the circle')
    plt.ylim([2.8,3.8])
    plt.legend()
    plt.show()
n=int(input("Enter the No. of points"))
estimatePi(n)