"""Solution for graph_19: M-Coloring Problem.

Return True iff the graph can be colored with m
colors such that no two adjacent vertices share a
color. Backtracking: assign colors to vertices one
at a time, picking only colors that don't conflict
with already-colored neighbours.
Source: https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/

Inputs passed to solve():
    n: number of nodes.
    edges: list of (u, v) tuples (undirected).
    m: number of available colors.

Goal:
    True iff a valid m-coloring exists.

Samples:
Sample 1 input:  n = 4, edges = [(0, 1), (1, 2), (2, 3), (3, 0)], m = 2
Sample 1 output: True (alternating)

Sample 2 input:  n = 3, edges = [(0, 1), (1, 2), (0, 2)], m = 2
Sample 2 output: False (triangle)


"""

def solve(n, edges, m):
    # Write your code here.
    return None
