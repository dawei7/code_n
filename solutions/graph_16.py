"""Solution for graph_16: Kosaraju's SCC.

Find all strongly connected components of a directed graph
using Kosaraju's two-pass algorithm. Pass 1: DFS in the
original graph, pushing nodes onto a stack in finish time
order. Pass 2: pop the stack and DFS on the transpose
graph; each DFS tree is one SCC.
Return a list of SCCs sorted as in Tarjan's spec.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/strongly-connected-components/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v) tuples for directed edges.

Goal:
    a list of SCCs (each a sorted list of node indices; outer list sorted).

Samples:
Sample 1 input:  num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)]
Sample 1 output: [[0, 1, 2], [3], [4]]

Sample 2 input:  num_nodes = 3, edges = [(0, 1), (1, 2), (2, 0)]
Sample 2 output: [[0, 1, 2]]


"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
