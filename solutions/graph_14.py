"""
Description
-----------
Find all bridges (cut edges) in an undirected graph. An
edge (u, v) is a bridge iff its removal disconnects the
graph. Tarjan-style DFS: (u, v) is a bridge iff
low[v] > disc[u].
Return the sorted list of (u, v) tuples (u < v).
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/bridge-in-a-graph/

Examples
--------
Example 1:
Input:  num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4)]
Output: [(0, 3), (3, 4)]

Example 2:
Input:  num_nodes = 4, edges = [(0, 1), (1, 2), (2, 3)]
Output: [(0, 1), (1, 2), (2, 3)]
"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
