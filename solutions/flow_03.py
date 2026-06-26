"""
Description
-----------
Given a bipartite graph (left_n left nodes, right_n
right nodes, edges connecting them), find the maximum
matching. Reduce to max flow: source->left (cap 1),
left->right (cap 1), right->sink (cap 1). The max flow
equals the max matching size. Run Edmonds-Karp.
Source: https://www.geeksforgeeks.org/maximum-bipartite-matching/

Examples
--------
Example 1:
Input:  left_n = 3, right_n = 3, edges = [(0, 0), (0, 1), (1, 0), (2, 1), (2, 2)]
Output: 3 (perfect matching)
"""

def solve(left_n, right_n, edges):
    # Write your code here.
    return None
