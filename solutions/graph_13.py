"""
Description
-----------
Find all articulation points (cut vertices) in an undirected
graph. A node u is an articulation point iff its removal
disconnects the graph. Tarjan-style DFS: u is one iff it has
more than one DFS child (if root) or some child v has
low[v] >= disc[u].
Return the sorted list of articulation point indices.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/

Examples
--------
Example 1:
Input:  num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4)]
Output: [0, 3]

Example 2:
Input:  num_nodes = 4, edges = [(0, 1), (1, 2), (2, 3)]
Output: [1, 2]
"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
