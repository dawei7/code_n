"""
Description
-----------
Find the maximum flow from node 0 to node n-1 in a
directed, weighted graph. Ford-Fulkerson with DFS
augmenting paths: repeatedly find an augmenting path,
push the minimum-capacity edge's flow along it, and
update the residual graph. Stop when no path exists.
O(E * max_flow).
Source: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

Examples
--------
Example 1:
Input:  n = 4, edges = [(0, 1, 10), (0, 2, 5), (1, 2, 15), (1, 3, 10), (2, 3, 10)]
Output: 15 (0->1->3 and 0->2->3)
"""

def solve(n, edges):
    # Write your code here.
    return None
