"""
Description
-----------
Find a 2-approximate vertex cover. Greedy: while
edges remain, pick the vertex with the highest degree,
add it to the cover, remove all incident edges. The
result is at most 2x the optimal vertex cover. The
verify accepts any 2-approx (i.e., len(cover) <= 2 * OPT).
Source: https://www.geeksforgeeks.org/vertex-cover-problem-approximate-algorithm/

Examples
--------
Example 1:
Input:  n = 5, edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
Output: [0, 2] (or other 2-approx)
"""

def solve(n, edges):
    # Write your code here.
    return None
