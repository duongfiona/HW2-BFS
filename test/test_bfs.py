# write tests for bfs
import pytest
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    g = graph.Graph("data/tiny_network.adjlist")
    nodes = list(g.graph.nodes())
    test_start = nodes[0] # arbitrarily pick first node as test start

    test_output = g.bfs(start=test_start)
    correct_output = list(nx.bfs_tree(g.graph, source=test_start))

    # assert that right number of nodes returned
    assert len(test_output) == len(g)
    
    # assert that right order of nodes returned
    assert test_output == correct_output

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    g = graph.Graph("data/citation_network.adjlist")

    # assert that correct shortest path is returned for connected nodes
    test_start = "Nadav Ahituv"
    test_end = "Tony Capra"

    test_output = g.bfs(test_start, test_end)
    correct_output = nx.shortest_path(g.graph, test_start, test_end)

    assert test_output == correct_output

    # assert that nodes that are not connected returns None
    bad_start = "Reza Abbasi-Asl"
    bad_end = "Tony Capra"
    assert g.bfs(test_start, bad_end) is None

def test_bfs_empty():
    """
    Test case for when bfs traversal is run on an empty graph.  
    """
    g = graph.Graph("data/empty.adjlist")

    with pytest.raises(Exception):
        g.bfs("", "")

def test_bfs_nonexistent_node():
    """
    Test case for when bfs traversal is run from a start node or
    to an end node that does not exist in the graph. 
    """
    g = graph.Graph("data/citation_network.adjlist")
    valid_node = "Tony Capra"
    bad_node = "Fiona Duong"

    with pytest.raises(KeyError):
        g.bfs(valid_node, bad_node)
    
    with pytest.raises(KeyError):
        g.bfs(bad_node, valid_node)