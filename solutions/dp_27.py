"""Solution for dp_27: Floyd-Warshall Path.

Given a weighted graph, return the shortest path from
src to dest as a list of node indices. Floyd-Warshall
computes all-pairs shortest paths; we maintain a next[]
matrix to reconstruct the path.
Source: https://www.geeksforgeeks.org/printing-shortest-path-given-distance/

Inputs passed to solve():
    n: number of nodes.
    edges: list of (u, v, weight) directed edges.
    src: source node.
    dest: destination node.

Goal:
    the shortest path from src to dest as a list of node indices, or [] if unreachable.

Samples:
Sample 1 input:  n = 4, edges = [(0, 1, 5), (0, 2, 1), (1, 3, 2), (2, 1, 1), (2, 3, 4)], src = 0, dest = 3
Sample 1 output: [0, 2, 1, 3]


"""

def solve(n, edges, src, dest):
    # Write your code here.
    return None
