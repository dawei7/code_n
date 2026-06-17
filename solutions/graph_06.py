"""Solution for graph_06: Floyd-Warshall.

Compute all-pairs shortest paths using the Floyd-Warshall
algorithm. The graph has directed, weighted edges (positive
weights). Return the N x N distance matrix where entry [i][j]
is the shortest distance from i to j, or -1 if j is
unreachable from i. The diagonal [i][i] is 0.
Requirement: O(V^3).
Source: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v, weight) tuples for directed edges.

Goal:
    an N x N matrix of shortest distances; -1 for unreachable pairs.

Samples:
Sample 1 input:  num_nodes = 3, edges = [(0, 1, 1), (1, 2, 1), (0, 2, 5)]
Sample 1 output: [[0, 1, 2], [999, 0, 1], [999, 999, 0]] (replace 999 with -1)

Sample 2 input:  num_nodes = 2, edges = []
Sample 2 output: [[0, -1], [-1, 0]]


"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
