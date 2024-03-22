import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

class Lattice:
    def __init__(self, n):
        # Create instance variables for the size of the grid and the graph itself
        self.n = n
        self.G = nx.grid_2d_graph(n, n) # Create 2D grid graph
        self.pos = dict( (i, i) for i in self.G.nodes() ) # Position of nodes

    def show(self):
        # Show the initial graph
        nx.draw_networkx_nodes(self.G, self.pos, node_size=1)
        plt.show()
        
    def percolate(self, p):
        # Randomly remove edges with probability p
        for (u, v) in self.G.edges():
            if random.uniform(0, 1) > p:
                self.G.remove_edge(u, v)
        # Draw remaining edges in red
        plt.figure(figsize=(10, 10))
        nx.draw_networkx_edges(self.G, self.pos,edge_color='r')
        
    def percolate1(self, p):
        # Same function as percolate without drawing edges
        for (u, v) in self.G.edges():
            if random.uniform(0, 1) > p:
                self.G.remove_edge(u, v)
                
    def existsTopDownPath(self):
        # Check if a path exists between top and bottom nodes
        top_nodes = [ (i,self.n-1) for i in range(self.n) ] # Top nodes
        bottom_nodes = [ (i,0) for i in range(self.n) ] # Bottom nodes
        for u in top_nodes:
            for v in bottom_nodes:
                if nx.has_path(self.G, u, v):
                    return True
        return False
    
    def showPaths(self):
        # Get a list of top nodes, which are all nodes in the top row
        top_nodes = [ (i,self.n-1) for i in range(self.n) ]
        # Get a list of bottom nodes, which are all nodes in the bottom row
        bottom_nodes = [ (i,0) for i in range(self.n) ]
        # Get a list of all nodes in the lattice except top and bottom nodes
        all_nodes = []
        for i in range(self.n):
            for j in range(i+1,self.n):
                all_nodes.append((i,j))
        # For each top node, check if there is a path to any bottom node
        for u in top_nodes:
            path_exists = False
            for v in bottom_nodes:
                if nx.has_path(self.G, u, v):
                    path_exists = True
                    break
            if path_exists:
                # If there is a path, find the shortest path and draw it in green
                shortest_path = nx.shortest_path(self.G, u, v)
                shortest_path_edges = [(shortest_path[i],shortest_path[i+1]) for i in range(len(shortest_path)-1)]
                nx.draw_networkx_edges(self.G,pos=self.pos,edgelist=shortest_path_edges,edge_color='g', width=2)
            else:
                # If there is no path to a bottom node, find the longest path to any node in the lattice except top and bottom nodes
                largest_shortest_path = [u]
                max_length = 0
                for v in all_nodes:
                    if nx.has_path(self.G, u, v):
                        shortest_path = nx.shortest_path(self.G, u, v)
                        if len(shortest_path) > max_length:
                            max_length = len(shortest_path)
                            largest_shortest_path = shortest_path
                largest_shortest_path_edges = [(largest_shortest_path[i],largest_shortest_path[i+1]) for i in range(len(largest_shortest_path)-1)]
                nx.draw_networkx_edges(self.G, pos=self.pos, edgelist=largest_shortest_path_edges,edge_color='g', width=2)
        # Draw all nodes in the lattice
        nx.draw_networkx_nodes(self.G, pos=self.pos, node_size=1)
        # Show the graph
        plt.show()
def percolation_verification(n, trials):
        #This function performs percolation verification on a 2D grid graph with size nxn.
        p_values = []
        percolation_fraction = []
        for p in range(1, n+1):
            # Normalize the probability value
            p /= n
            percolation_count = 0
            # Perform percolation for 'trials' number of times
            for i in range(trials):
                l = Lattice(n)
                l.percolate1(p)
                # Check if there exists a top-down path
                if l.existsTopDownPath():
                    percolation_count += 1
            # Calculate the percolation fraction
            percolation_fraction.append(percolation_count / trials)
            p_values.append(p)

        # Plot the critical cut-off in 2-D bond percolation
        plt.plot(p_values, percolation_fraction)
        plt.xlabel("Probability")
        plt.ylabel("Fraction of runs with end-to-end percolation")
        plt.title("Critical cut-off in 2-D bond percolation")
        plt.show()





percolation_verification(20, 15)       
