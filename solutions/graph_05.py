"""Solution for graph_05: Bellman-Ford.

Find the shortest distance from the start node to all other
nodes using the Bellman-Ford algorithm. The graph has
directed, weighted edges (weights can be negative, but the
spec guarantees no negative cycles).
Return a dict mapping each node to its shortest distance from
start. Unreachable nodes get -1.
Requirement: O(V * E).
Source: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

Inputs passed to solve():
    num_nodes: number of nodes in the graph.
    edges: list-like of (u, v, weight) tuples for directed edges.
    start: source node.

Goal:
    a dict mapping each node to its shortest distance. Unreachable nodes get -1.

Samples:
Sample 1 input:  num_nodes = 3, edges = [(0, 1, 5), (1, 2, 3)], start = 0
Sample 1 output: {0: 0, 1: 5, 2: 8}

Sample 2 input:  num_nodes = 2, edges = [], start = 0
Sample 2 output: {0: 0, 1: -1}

Sample 3 input:  num_nodes = 4, edges = [(0, 1, 1), (1, 2, 1), (0, 2, 5)], start = 0
Sample 3 output: {0: 0, 1: 1, 2: 2, 3: -1}

"""

def solve(num_nodes, edges, start):
    # Write your code here.
    return None
