"""
Description
-----------
Given an undirected unweighted graph (with
            potential parallel edges) as a list of (u, v)
            edges, find a minimum cut (the smallest set of
            edges whose removal disconnects the graph).
            Karger's randomized algorithm: contract a random
            edge until 2 vertices remain; the remaining
            edges form the cut. The cut produced may NOT be
            minimum, but the algorithm is run trials times
            and the minimum cut across all trials is
            returned. O(E * V * trials) total.
            Source: https://www.geeksforgeeks.org/dsa/introduction-and-implementation-of-kargers-algorithm-for-minimum-cut/

Examples
--------
Example 1:
Input:  edges = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)], n = 4, trials = 50
Output: 2 (the 4-cycle with the 2 cross-edges)
"""

def solve(edges, n, trials):
    # Write your code here.
    return None
