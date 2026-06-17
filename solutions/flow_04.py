"""Solution for flow_04: Dinic's Max Flow.


            Compute the max s-t flow in a directed capacitated
            graph. Dinic's algorithm: BFS from s builds a level
            graph (distance in edges, ignoring saturated
            edges); then DFS sends blocking flows along
            level-monotone paths; when BFS can't reach t, stop.
            O(E * sqrt(V)) for unit capacities, O(V^2 * E) worst
            case. Source = node 0, sink = node n-1.
            Source: https://www.geeksforgeeks.org/dsa/dinics-algorithm-maximum-flow/
            

Inputs passed to solve():
    n: number of nodes (small in tests, n <= 6).
    edges: list of (u, v, capacity) tuples; u, v in [0, n).

Goal:
    the max s-t flow as a non-negative int (s=0, t=n-1).

Samples:
Sample 1 input:  n = 2, edges = [(0,1,5)]
Sample 1 output: 5

Sample 2 input:  n = 4, edges = [(0,1,10),(0,2,8),(1,3,10),(2,3,8)]
Sample 2 output: 18

Sample 3 input:  n = 4, edges = [(0,1,10),(1,2,5),(2,3,8),(0,3,7)]
Sample 3 output: 15

"""

def solve(n, edges):
    # Write your code here.
    return None
