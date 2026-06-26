"""
Description
-----------
Compute all-pairs shortest paths using the Floyd-Warshall
algorithm. The graph has directed, weighted edges (positive
weights). Return the N x N distance matrix where entry [i][j]
is the shortest distance from i to j, or -1 if j is
unreachable from i. The diagonal [i][i] is 0.
Requirement: O(V^3).
Source: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

Examples
--------
Example 1:
Input:  num_nodes = 3, edges = [(0, 1, 1), (1, 2, 1), (0, 2, 5)]
Output: [[0, 1, 2], [999, 0, 1], [999, 999, 0]] (replace 999 with -1)

Example 2:
Input:  num_nodes = 2, edges = []
Output: [[0, -1], [-1, 0]]
"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
