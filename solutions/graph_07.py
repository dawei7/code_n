"""Solution for graph_07: Topological Sort.

Compute a topological ordering of the directed acyclic graph
using Kahn's algorithm. Return the order as a list of node
indices, or -1 if a cycle is detected.
The spec guarantees a DAG (the setup uses u < v for every
edge), so the answer is always a list.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v) tuples for directed edges (u < v guarantees DAG).

Goal:
    a list of node indices in topological order, or -1 on a cycle.

Samples:
Sample 1 input:  num_nodes = 4, edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
Sample 1 output: [0, 1, 2, 3]

Sample 2 input:  num_nodes = 3, edges = []
Sample 2 output: [0, 1, 2]

Sample 3 input:  num_nodes = 3, edges = [(0, 1), (0, 2)]
Sample 3 output: [0, 1, 2]

"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
