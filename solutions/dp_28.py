"""Solution for dp_28: Bellman-Ford (SSSP).

Single-source shortest paths with possible negative
edges. Relax all edges n-1 times. O(V * E). Detects
negative cycles if the n-th iteration still relaxes.
Source: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

Inputs passed to solve():
    n: number of nodes.
    edges: list of (u, v, weight) tuples for directed edges.
    src: source node.

Goal:
    a list of n distances from src.

Samples:
Sample 1 input:  n = 4, edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 4)], src = 0
Sample 1 output: [0, 4, 1, 5]


"""

def solve(n, edges, src):
    # Write your code here.
    return None
