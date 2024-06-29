# uncomment above if installed
import pip
pip.main(['install', 'networkx'])

# Import the necessary libraries
import networkx as nx
from networkx.algorithms import tree

# Define the function for Kruskal's algorithm
def kruskal_mst(graph):
    # Sort the edges of the graph in ascending order based on their weights
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    
    # dictionary to keep track of the parent of each vertex
    parent = {v: v for v in graph.nodes}
    
    # empty list to store the edges of the minimum spanning tree
    mst = []
    
    # find the parent of a vertex
    def find_parent(v):
        if parent[v] != v:
            parent[v] = find_parent(parent[v])
        return parent[v]
    
    # merge two sets of vertices
    def merge_sets(u, v):
        parent[find_parent(u)] = find_parent(v)
    
    # Iterate over the sorted edges and stop once all the edges have been added to the minimum spanning tree
    for u, v, data in edges:
        # Check if adding the edge will create a cycle
        if find_parent(u) != find_parent(v):
            # Add the edge to the minimum spanning tree
            mst.append((u, v))
            # Merge the sets of vertices
            merge_sets(u, v)
    
    # Return the list of edges in the minimum spanning tree
    return mst

# Define the test driver function
def test_kruskal():
    # Create a new graph instance
    G = nx.Graph()
    
    # Add edges to the graph along with their weights
    # The weights represent the cost of the connection between the nodes
    G.add_edge('A', 'B', weight=1)
    G.add_edge('B', 'C', weight=2)
    G.add_edge('C', 'A', weight=3)
    G.add_edge('C', 'D', weight=1)
    
    # Assert that the minimum spanning tree found by the kruskal_mst function is as expected
    # The result of kruskal_mst(G) and the expected result are sorted before comparison
    # This is because the order of the edges in the minimum spanning tree can vary
    assert sorted(kruskal_mst(G)) == sorted([('A', 'B'), ('B', 'C'), ('C', 'D')])
    print("Test passed!")
    
# Call the test driver function
test_kruskal()