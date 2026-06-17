"""Solution for graph_08: Kruskal's MST.

Find the minimum spanning tree of an undirected, weighted
graph using Kruskal's algorithm. Return the MST as a sorted
list of (u, v, weight) tuples, or [] if the graph is not
connected. The setup always produces a connected graph.
Requirement: O(E log E).
Source: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v, weight) tuples for undirected edges.

Goal:
    a sorted list of MST edges (u, v, w), or [] if the graph is disconnected.

Samples:
Sample 1 input:  num_nodes = 4, edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
Sample 1 output: [(2, 3, 4), (0, 3, 5), (0, 1, 10)]

Sample 2 input:  num_nodes = 3, edges = [(0, 1, 1), (1, 2, 2)]
Sample 2 output: [(0, 1, 1), (1, 2, 2)]


"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
