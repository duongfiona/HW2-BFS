import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # if graph is empty
        if len(self.graph.nodes()) == 0:
            raise Exception("Graph has no nodes")
    
        # if given start node does not exist in graph
        if start not in self.graph:
            raise KeyError(f"\'{start}\' node does not exist in graph")
        
        # if given end node does not exist in graph
        if end is not None and end not in self.graph:
            raise KeyError(f"\'{end}\' node does not exist in graph")

        Q = deque()
        visited = set()
        Q.append(start)
        visited.add(start)

        traversal_list = []
        predecessor = {start: None} # for shortest path reconstruction

        while Q:
            v = Q.popleft()
            traversal_list.append(v)

            # if end node has been reached, reconstruct and return shortest path 
            if v == end:
                path = []
                while v is not None:
                    path.append(v)
                    v = predecessor[v]
                return path[::-1]

            # if end node has not been reached, continue exploring neighbors
            N = self.graph.neighbors(v)
            for neighbor in N:
                if neighbor not in visited:
                    predecessor[neighbor] = v
                    visited.add(neighbor)
                    Q.append(neighbor)
        
        # if there is no end node input, return BFS traversal list
        if end is None:
            return traversal_list
        # if end node was given but no path was returned above, return None
        else:
            return None