"""
Description
-----------
Find all strongly connected components of a directed graph
using Kosaraju's two-pass algorithm. Pass 1: DFS in the
original graph, pushing nodes onto a stack in finish time
order. Pass 2: pop the stack and DFS on the transpose
graph; each DFS tree is one SCC.
Return a list of SCCs sorted as in Tarjan's spec.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/strongly-connected-components/

Examples
--------
Example 1:
Input:  num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)]
Output: [[0, 1, 2], [3], [4]]

Example 2:
Input:  num_nodes = 3, edges = [(0, 1), (1, 2), (2, 0)]
Output: [[0, 1, 2]]
"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
