"""Solution for flow_03: Bipartite Matching.

Given a bipartite graph (left_n left nodes, right_n
right nodes, edges connecting them), find the maximum
matching. Reduce to max flow: source->left (cap 1),
left->right (cap 1), right->sink (cap 1). The max flow
equals the max matching size. Run Edmonds-Karp.
Source: https://www.geeksforgeeks.org/maximum-bipartite-matching/

Inputs passed to solve():
    left_n: number of left-side nodes.
    right_n: number of right-side nodes.
    edges: list of (left_idx, right_idx) tuples.

Goal:
    the size of the maximum matching.

Samples:
Sample 1 input:  left_n = 3, right_n = 3, edges = [(0, 0), (0, 1), (1, 0), (2, 1), (2, 2)]
Sample 1 output: 3 (perfect matching)


"""

def solve(left_n, right_n, edges):
    # Write your code here.
    return None
