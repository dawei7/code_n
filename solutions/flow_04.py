"""
Description
-----------
Compute the max s-t flow in a directed capacitated
            graph. Dinic's algorithm: BFS from s builds a level
            graph (distance in edges, ignoring saturated
            edges); then DFS sends blocking flows along
            level-monotone paths; when BFS can't reach t, stop.
            O(E * sqrt(V)) for unit capacities, O(V^2 * E) worst
            case. Source = node 0, sink = node n-1.
            Source: https://www.geeksforgeeks.org/dsa/dinics-algorithm-maximum-flow/

Examples
--------
Example 1:
Input:  n = 2, edges = [(0, 1, 5)]
Output: 5

Example 2:
Input:  n = 4, edges = [(0, 1, 10), (0, 2, 8), (1, 3, 10), (2, 3, 8)]
Output: 18

Example 3:
Input:  n = 4, edges = [(0, 1, 10), (1, 2, 5), (2, 3, 8), (0, 3, 7)]
Output: 15
"""

def solve(n, edges):
    # Write your code here.
    return None
