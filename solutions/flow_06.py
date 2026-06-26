"""
Description
-----------
Compute the max s-t flow using the Goldberg-Tarjan
            push-relabel algorithm. Maintain per-vertex 'height'
            labels and 'excess' flow. Initialize: height of s =
            n, others = 0, push full capacity from s to its
            neighbors. Then repeatedly: pick an overflowing
            vertex u; if any neighbor v with residual capacity
            has height[u] = height[v] + 1, push (relabel-to-fit).
            Otherwise relabel u to 1 + min height of neighbors
            with residual. When no vertex (except s, t) is
            overflowing, the excess at t is the max flow.
            O(V^3) generic, O(V^2 * sqrt(E)) with highest-label
            selection. Source = node 0, sink = node n-1.
            Source: https://www.geeksforgeeks.org/dsa/push-relabel-algorithm/

Examples
--------
Example 1:
Input:  n = 4, edges = [(0, 1, 16), (0, 2, 13), (1, 2, 10), (1, 3, 12), (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)]
Output: 23
"""

def solve(n, edges):
    # Write your code here.
    return None
