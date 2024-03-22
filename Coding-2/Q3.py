import matplotlib.pyplot as plt
import random
import numpy as np
class UndirectedGraph:
    # Initialize the graph with optional number of nodes
    def __init__(self, num_nodes=None):
        """Initialize the graph with optional number of nodes"""
        self.adj_list = {} # dictionary to store the adjacency list of the graph
        self.num_nodes = num_nodes # number of nodes in the graph
        self.num_edges = 0 # number of edges in the graph
        if num_nodes: # if number of nodes is provided, initialize the adjacent list
            for i in range(1, num_nodes + 1):
                self.adj_list[i] = []
    
    def addNode(self, node):
        '''Add a new node to the graph'''
        # raise an exception if node index is greater than number of nodes
        if self.num_nodes and node > self.num_nodes:
            raise Exception("Node index cannot exceed number of nodes")
        # add the node if it's not already present in the graph
        if node not in self.adj_list:
            self.adj_list[node] = []
    
    def addEdge(self, node1, node2):
        # add the nodes if nodes not already present in the graph
        self.addNode(node1)
        self.addNode(node2)
        # add the edge by updating the adjacency list
        if node2 in self.adj_list[node1]: # Check for duplicate edges
            pass;
        else:
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)
            self.num_edges += 1 # Increase number of edges
    
    def __add__(self, other):
        ''' Overload the '+' operator to add a node or an edge to the graph '''
        # add an edge if 'other' is a tuple
        if type(other) == tuple:
            self.addEdge(other[0], other[1])
        # add an edge if 'other' is a int
        elif(isinstance(other,int)):
            self.addNode(other)
        # raises an exception for any other type
        else:
            raise Exception("Operation not possible")
            
        return self
    
    def __str__(self):
        ''' Override the 'print' function to print the details of the graph '''
        s = "Graph with {} nodes and {} edges. Neighbours of the nodes are belows:\n".format(len(self.adj_list), self.num_edges)
        for node, neighbours in self.adj_list.items():
            s += "Node {}: {{{}}}\n".format(node, ", ".join([str(n) for n in neighbours]))
        return s
    def isConnected(self):
        """Return True if the graph is connected, and False otherwise"""
        # Initialize a queue and a visited list to keep track of nodes we have visited
        l = []
        isvisited = [False] * (self.num_nodes+1) # Initialise isvisited flag to false for evey node
        # Start the BFS from the first node
        l.append(1)
        isvisited[0] = True #start with 1 as first node
	isvisited[1] = True;
    
        # Run BFS
        while l:
            k = l.pop(0)
            #print(self.adj_list.keys())
            for i in self.adj_list[k]:
                if not isvisited[i]:
                    l.append(i)
                    isvisited[i] = True
    
        # Check if all nodes have been visited
        #print(isvisited)
        for node in isvisited:
            if not node:
                return False
        return True
    def plotDegDist(self):
        ''' Plot the degree distribution of the graph '''
        #print(self.adj_list.values())
        # create the degree sequence (number of neighbours for each node)
        degree_sequence = [len(i) for i in self.adj_list.values()]
        #print(degree_sequence)
        # count the number of nodes with each degree
        degree_count = {}
        for degree in degree_sequence:
            if degree in degree_count:
                degree_count[degree] += 1
            else:
                degree_count[degree] = 1
        # Create zero values in degree_count for nodes with degree 0
        for i in range(len(degree_sequence)):
            if i in degree_count:
                pass;
            else:
                degree_count[i]=0;
        # convert the degree count to fractions
        degrees = list(degree_count.keys())
        fractions = [degree_count[d]/len(degree_sequence) for d in degrees]
        # calculate average degree
        avg_degree = sum(degree_sequence) / len(degree_sequence)
        # plot the degree distribution
        plt.plot(degrees,fractions,'bo',markersize=1,label='Actual degree dist.') # blue circle
        plt.title("Node Degree Distribution")
        plt.grid()
        #plt.grid(True)
        plt.xlabel("Node degree")
        plt.ylabel("Fraction of nodes")
        # plot average degree
        plt.axvline(avg_degree, color='r',label='Avg. node Degree')
        plt.legend(loc='upper right')
        plt.show()
class ERRandomGraph(UndirectedGraph):
    def __init__(self, num_nodes):
        """Initialize the graph with given number of nodes"""
        super().__init__(num_nodes)
    def sample(self, p):
        """Create a Erdos-Renyi random graph G(n, p)"""
        for i in range(1, self.num_nodes + 1):
            for j in range(i+1, self.num_nodes + 1):
                if random.random() < p:
                    self.addEdge(i, j)
                                        
def plotConnectedness():
    # Threshold value calculated using log(n)/n, where n = 100 in this case
    threshold = np.log(100)/100
    # Initialize the connectedness to 0
    connectedness = 0
    # Range of values for p
    x = np.arange(0.0, 0.15, 0.02)
    # Dictionary to store the probability of a G(n, p) graph being connected
    prob_dict = {i: 0 for i in x}
    # Number of runs for each value of p
    run = 100

    # Loop through all values of p
    for p in x:
        # Loop for each run for the same p value
        for i in range(run):
            # Create a G(n, p) graph
            g = ERRandomGraph(100)
            # Generate the random graph with given p
            g.sample(p)
            # Check if the graph is connected
            r = g.isConnected()
            # If the graph is connected, increment the connectedness value
            if r == True:
                connectedness = connectedness + 1
    
        # Store the connectedness for the current p value
        prob_dict[p] = connectedness    
        # Reset the connectedness for the next p value
        connectedness = 0
    # Calculate the ratio proportion for each p value
    ratio_proportion = [int(prob_dict[i])/run for i in prob_dict.keys()]
    # Plot the graph for connectedness vs p
    plt.plot(x, ratio_proportion, color="b")
    # Add a vertical line for the theoritical threshold
    plt.axvline(threshold, color='r', linestyle='-', label='Theoritical threshold')
    # Set the x-axis label as "p"
    plt.xlabel("p")
    # Set the x-axis range
    plt.xlim(0.0, 0.1)
    # Set the y-axis range
    plt.ylim([0, 1])
    # Show grid lines
    plt.grid()
    # Set the y-axis label 
    plt.ylabel("Fraction of runs G(n, p) is connected")
    # Set the plot title 
    plt.title("Connectedness of a G(n, p) as function of p")
    # Show the legend
    plt.legend()
    # Show the plot
    plt.show()

plotConnectedness()

g = UndirectedGraph(5)
g = g + (1, 2)
g = g + (2, 3)
g = g + (3, 4)
g = g + (3, 5)
print(g.isConnected())

g = UndirectedGraph(5)
g = g + (1, 2)
g = g + (2, 3)
g = g + (3, 5)
print(g.isConnected())
