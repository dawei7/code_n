"""
Description
-----------
Shortest path on a graph with edge weights in {0, 1}.
Use a deque: pop the left, push 0-weight neighbors to the
LEFT and 1-weight neighbors to the RIGHT. This makes the
algorithm O(V + E) - the same as BFS, but supports unit
weights too.
Return a dict mapping each node to its shortest distance from
start. Unreachable nodes get -1.
Requirement: O(V + E).
Source: https://www.geeksforgeeks.org/0-1-bfs-shortest-path-unit-weight-edges/

Examples
--------
Example 1:
Input:  num_nodes = 4, edges = [(0, 1, 0), (1, 2, 1), (0, 2, 1), (2, 3, 0)], start = 0
Output: {0: 0, 1: 0, 2: 1, 3: 1}
"""

def solve(num_nodes, edges, start):
    # Write your code here.
    return None
