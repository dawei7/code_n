"""Solution for flow_02: Edmonds-Karp.

Max flow via Edmonds-Karp: BFS-based augmenting path
that finds the shortest (in edges) augmenting path. The
BFS guarantees O(V * E) augmentations, giving O(V * E^2)
total. Edge capacities are integers.
Source: https://www.geeksforgeeks.org/edmonds-karp-algorithm-for-max-flow-set-2-implementation/

Inputs passed to solve():
    n: number of nodes.
    edges: list of (u, v, capacity) tuples.

Goal:
    the maximum flow value from 0 to n-1.

Samples:
Sample 1 input:  n = 4, edges = [(0, 1, 10), (0, 2, 5), (1, 2, 15), (1, 3, 10), (2, 3, 10)]
Sample 1 output: 15


"""

def solve(n, edges):
    # Write your code here.
    return None
