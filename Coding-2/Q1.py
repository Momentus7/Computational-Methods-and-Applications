import matplotlib.pyplot as plt
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
        # return the updated graph   
        return self
    
    def __str__(self):
        ''' Override the 'print' function to print the details of the graph '''
        s = "Graph with {} nodes and {} edges. Neighbours of the nodes are belows:\n".format(len(self.adj_list), self.num_edges)
        for node, neighbours in self.adj_list.items():
            s += "Node {}: {{{}}}\n".format(node, ", ".join([str(n) for n in neighbours]))
        return s
    def plotDegDist(self):
import matplotlib.pyplot as plt
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
        # return the updated graph   
        return self
    
    def __str__(self):
        ''' Override the 'print' function to print the details of the graph '''
        s = "Graph with {} nodes and {} edges. Neighbours of the nodes are belows:\n".format(len(self.adj_list), self.num_edges)
        for node, neighbours in self.adj_list.items():
            s += "Node {}: {{{}}}\n".format(node, ", ".join([str(n) for n in neighbours]))
        return s
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
        plt.plot(degrees,fractions,'bo',label='Actual degree dist.') # blue circle
        plt.title("Node Degree Distribution")
        plt.grid()
        #plt.grid(True)
        plt.xlabel("Node degree")
        plt.ylabel("Fraction of nodes")
        # plot average degree
        plt.axvline(avg_degree, color='r',label='Avg. node Degree')
        plt.legend(loc='upper right')
        plt.show()
    

# Example usage:
g = UndirectedGraph(5)
print(g)
# Output: Graph with 5 nodes and 0 edges. Neighbours of the nodes are belows:
# Node 1: {}
# Node 2: {}
# Node 3: {}
# Node 4: {}
# Node 5: {}

g = UndirectedGraph()
g = g + 10
g = g + (11, 12)
print(g)
# Output: Graph with 3 nodes and 1 edges. Neighbours of the nodes are belows:
# Node 10: {}
# Node 11: {12}
# Node 12: {11}
k=UndirectedGraph()
print(k)
l=UndirectedGraph(4)
print(l)

g = UndirectedGraph(5)
g = g + (1, 2)
g = g + (3, 4)
g = g + (1, 4)
g = g + (4, 1)
print(g)
g.plotDegDist()


'''g = UndirectedGraph()
g = g + 100
g = g + (1, 2)
g = g + (1, 100)
g = g + (100, 3)
g = g + 20
g.plotDegDist()'''
