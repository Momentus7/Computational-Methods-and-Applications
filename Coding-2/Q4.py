import matplotlib.pyplot as plt
import random
import numpy as np
import math
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
    def oneTwoComponentSizes(self):
        
        l = []
        isvisited = [False] * (self.num_nodes+1) # Initialise isvisited flag to false for evey node
        #print(isvisited)
        # Start the BFS from the first node
        l.append(1)
        isvisited[0] = True #start with 1 as first node
	isvisited[1] = True;
        sizes=[] #To store the component size
    
        # Run BFS
        for i in range(1,self.num_nodes):
            if not isvisited[i]:
                count=0;
                l=[i];
                isvisited[i]=True;
                while l:
                    k = l.pop(0)
                    #print(self.adj_list.keys())
                    count+=1;
                    for i in self.adj_list[k]:
                        if not isvisited[i]:
                            l.append(i)
                            isvisited[i] = True
                sizes.append(count)
        sizes.sort(reverse=True) # Sort the sizes in decreasing  order
        return sizes[:2] # Return the top 2 size
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
                                        
def verify_erdos_renyi(n, p_min, p_max, num_runs):
    # Initialize variables to store the size of the largest and second largest
    # connected components for each value of p
    largest_cc_sizes = []
    second_largest_cc_sizes = []
    ps = []
    connected_threshold=math.log(n)/n;
    
    # Iterate over different values of p
    maximum=0;
    for p in np.linspace(p_min, p_max, num_runs):
        # Create an Erdos-Renyi random graph
        g = ERRandomGraph(n)
        # Sample the graph
        g.sample(p)
        # Get the size of the largest and second largest connected components
        result= g.oneTwoComponentSizes()
        #print(result)
        #To avoid the sitution when n==largest connected component size
        if len(result)==1:
            second_largest=0;
        else:
            second_largest=result[1]/n
        largest=result[0]/n
        maximum=max(maximum,largest)
        # Append the sizes to the corresponding lists
        largest_cc_sizes.append(largest)
        second_largest_cc_sizes.append(second_largest)
        ps.append(p)
    #print(maximum)
    # Plot the sizes of the largest and second largest connected components as a function of p
    plt.plot(ps, largest_cc_sizes, label='Largest CC')
    plt.plot(ps, second_largest_cc_sizes, label='2nd Largest CC')
    plt.axvline(connected_threshold, color='y', linestyle='-',label='Connectedness threshold')
    plt.axvline(maximum/n, color='r', linestyle='-',label='largest CC size threshold')
    plt.xlim(0.000,0.01)
    plt.title(f"Fraction of nodes in the largest and second-largest \nconnected components(CC) of G(1000, p) as function of p")
    plt.xlabel('p')
    plt.ylabel('Fraction of nodes')
    plt.grid()
    plt.legend()
    plt.show()
    
verify_erdos_renyi(1000, 0.0000, 0.01, 50)

    
g = UndirectedGraph(6)
g.addEdge(1, 2)
g.addEdge(3, 4)
g.addEdge(6, 4)
print(g.oneTwoComponentSizes()) # should return [3, 2]

g = ERRandomGraph(100)
g.sample(0.01)
print(g.oneTwoComponentSizes())