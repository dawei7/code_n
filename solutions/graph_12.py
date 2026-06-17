"""Solution for graph_12: Bipartite Check.

Return True iff the undirected graph is bipartite
(2-colorable). Equivalent: the graph contains no odd
cycles. BFS-based 2-coloring is the standard approach.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/bipartite-graph/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v) tuples for undirected edges.

Goal:
    True iff the graph is 2-colorable (no odd cycles).

Samples:
Sample 1 input:  num_nodes = 4, edges = [(0, 1), (0, 3), (1, 2), (2, 3)]
Sample 1 output: True (color 0: 0,2; color 1: 1,3)

Sample 2 input:  num_nodes = 3, edges = [(0, 1), (1, 2), (0, 2)]
Sample 2 output: False (triangle)

Sample 3 input:  num_nodes = 2, edges = []
Sample 3 output: True

"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
