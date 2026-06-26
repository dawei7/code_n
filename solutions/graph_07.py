"""
Description
-----------
Compute a topological ordering of the directed acyclic graph
using Kahn's algorithm. Return the order as a list of node
indices, or -1 if a cycle is detected.
The spec guarantees a DAG (the setup uses u < v for every
edge), so the answer is always a list.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

Examples
--------
Example 1:
Input:  num_nodes = 4, edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
Output: [0, 1, 2, 3]

Example 2:
Input:  num_nodes = 3, edges = []
Output: [0, 1, 2]

Example 3:
Input:  num_nodes = 3, edges = [(0, 1), (0, 2)]
Output: [0, 1, 2]
"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
