"""Solution for graph_21: Hamiltonian Path Existence.

Return True iff there's a Hamiltonian path from 0 to
n-1 in the undirected graph. Backtracking: at each
step, try each unvisited neighbour. Stop at the first
path that visits every vertex and ends at n-1.
Source: https://www.geeksforgeeks.org/backtracking-set-7-hamiltonian-cycle/

Inputs passed to solve():
    n: number of nodes (capped at 6).
    edges: list of (u, v) tuples (undirected).

Goal:
    True iff a Hamiltonian path from 0 to n-1 exists.

Samples:
Sample 1 input:  n = 4, edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
Sample 1 output: True (0->1->3->2 or 0->2->3->1)

Sample 2 input:  n = 4, edges = [(0, 1), (1, 2), (2, 3)]
Sample 2 output: False (3 is only reachable from 2)


"""

def solve(n, edges):
    # Write your code here.
    return None
