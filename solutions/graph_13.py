"""Solution for graph_13: Articulation Points.

Find all articulation points (cut vertices) in an undirected
graph. A node u is an articulation point iff its removal
disconnects the graph. Tarjan-style DFS: u is one iff it has
more than one DFS child (if root) or some child v has
``low[v] >= disc[u]``.
Return the sorted list of articulation point indices.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v) tuples for undirected edges.

Goal:
    a sorted list of articulation point indices.

Samples:
Sample 1 input:  num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4)]
Sample 1 output: [0, 3]

Sample 2 input:  num_nodes = 4, edges = [(0, 1), (1, 2), (2, 3)]
Sample 2 output: [1, 2]


"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
