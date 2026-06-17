"""Solution for graph_11: Cycle Detection.

Return True iff the undirected graph has a cycle.
Uses iterative DFS with parent tracking.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v) tuples for undirected edges.

Goal:
    True iff the graph has at least one cycle.

Samples:
Sample 1 input:  num_nodes = 4, edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
Sample 1 output: True (0-1-2-0)

Sample 2 input:  num_nodes = 4, edges = [(0, 1), (1, 2), (2, 3)]
Sample 2 output: False (chain)

Sample 3 input:  num_nodes = 3, edges = [(0, 1), (1, 2)]
Sample 3 output: False

"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
