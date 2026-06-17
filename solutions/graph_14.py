"""Solution for graph_14: Bridges.

Find all bridges (cut edges) in an undirected graph. An
edge (u, v) is a bridge iff its removal disconnects the
graph. Tarjan-style DFS: (u, v) is a bridge iff
``low[v] > disc[u]``.
Return the sorted list of (u, v) tuples (u < v).
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/bridge-in-a-graph/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v) tuples for undirected edges.

Goal:
    a sorted list of (u, v) bridge tuples (u < v).

Samples:
Sample 1 input:  num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4)]
Sample 1 output: [(0, 3), (3, 4)]

Sample 2 input:  num_nodes = 4, edges = [(0, 1), (1, 2), (2, 3)]
Sample 2 output: [(0, 1), (1, 2), (2, 3)]


"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
