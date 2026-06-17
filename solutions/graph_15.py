"""Solution for graph_15: Tarjan's SCC.

Find all strongly connected components of a directed graph
using Tarjan's algorithm. Each SCC is a maximal set of
nodes where every node can reach every other.
Return a list of SCCs; each SCC is sorted internally; the
outer list is sorted by smallest element.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v) tuples for directed edges.

Goal:
    a list of SCCs (each a sorted list of node indices; outer list sorted).

Samples:
Sample 1 input:  num_nodes = 5, edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)]
Sample 1 output: [[0, 1, 2], [3], [4]]

Sample 2 input:  num_nodes = 3, edges = [(0, 1), (1, 2)]
Sample 2 output: [[0], [1], [2]]


"""

def solve(num_nodes, edges):
    # Write your code here.
    return None
