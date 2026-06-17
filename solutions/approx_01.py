"""Solution for approx_01: Vertex Cover (2-Approx).

Find a 2-approximate vertex cover. Greedy: while
edges remain, pick the vertex with the highest degree,
add it to the cover, remove all incident edges. The
result is at most 2x the optimal vertex cover. The
verify accepts any 2-approx (i.e., len(cover) <= 2 * OPT).
Source: https://www.geeksforgeeks.org/vertex-cover-problem-approximate-algorithm/

Inputs passed to solve():
    n: number of nodes.
    edges: list of (u, v) tuples (undirected).

Goal:
    a sorted list of node indices covering every edge (and 2-approx).

Samples:
Sample 1 input:  n = 5, edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
Sample 1 output: [0, 2] (or other 2-approx)


"""

def solve(n, edges):
    # Write your code here.
    return None
