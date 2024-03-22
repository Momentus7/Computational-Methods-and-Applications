import matplotlib.pyplot as plt
import random

class Dice:
    def __init__(self, numSides = 6):
        # Check if the number of sides is valid
        if isinstance(numSides, int) and numSides >= 4:
            self.numSides = numSides
            self.prob = [1/numSides for i in range(numSides)]
        else:
            raise Exception("Cannot construct the dice")
            
    def setProb(self, prob):
        if len(prob) != self.numSides:
            raise Exception("Invalid probability distribution")
        if sum(prob) != 1:
            raise Exception("Invalid probability distribution")
        self.prob = prob
        
    def __str__(self):
        '''convert object into a string'''
        return f"Dice with {self.numSides} faces and probability distribution {self.prob}"
        
    def roll(self, n):
        # Create a list of zeros with length equal to number of sides
        x=[]
        outcomes = [0 for i in range(self.numSides)]
        expected_outcomes = [self.prob[i]*n for i in range(self.numSides)]
        for i in range(n):
            # Generate a random number between 0 and 1
            randNum = random.random()
            # Use a cumulative probability to determine the outcome
            cumulativeProb = 0
            for j in range(self.numSides):
                cumulativeProb += self.prob[j]
                if randNum <= cumulativeProb:
                    outcomes[j] += 1
                    break
	# Plot a bar chart of the outcomes
        list1=[]
        list2=[]
        list3=[]
	#Created 2 lists to make the visualization more clear
        for i in range(1,self.numSides+1):
            list1.append(i-0.1)
            list2.append(i+0.1)
        for i in range(1,self.numSides+1):
            list3.append(i)
        x = np.arange(self.numSides)
        fig,ax = plt.subplots()
        ax.bar(list1 , expected_outcomes,0.2, label = 'Expected Outcomes')
        ax.bar(list2 , outcomes,0.2, label = 'Actual Outcomes')
        ax.set_xlabel("Sides")
        ax.set_ylabel("Occurrences")
        ax.set_xticks(list3)
        plt.legend()
        plt.show()


        
# The following code should create a 6 faced dice
d = Dice()
print(d)

# The following code should create a 10 faced dice
d = Dice(10)
print(d)

# The following code should throw an exception
#d = Dice(3)

# The following code should throw an exception
#d = Dice(4.5)

# The following code should throw an exception
#d = Dice('5')
'''d = Dice(4)
d.setProb((0.1, 0.2, 0.3, 0.4))
print(d)'''

'''d = Dice(4)
d.setProb((0.1, 0.2, 0.3))'''
d = Dice(4)
d.roll(100)


