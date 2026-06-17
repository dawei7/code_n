"""Solution for flow_05: Minimum s-t Cut.


            Find the minimum s-t cut in a directed flow network.
            Run any max-flow algorithm, then in the final residual
            graph do DFS/BFS from s; the set of reachable nodes
            is S, and every edge (u, v) in the ORIGINAL graph
            with u in S and v not in S is a min-cut edge. By the
            max-flow min-cut theorem, the min cut's capacity
            equals the max flow. Return the list of min-cut
            edges as a sorted list of (u, v) tuples.
            Source: https://www.geeksforgeeks.org/dsa/minimum-cut-in-a-directed-graph/
            

Inputs passed to solve():
    n: number of nodes (small in tests, n <= 6).
    edges: list of (u, v, capacity) tuples; u, v in [0, n).

Goal:
    a sorted list of (u, v) tuples that form a minimum s-t cut (s=0, t=n-1).

Samples:
Sample 1 input:  n = 4, edges = [(0,1,16),(0,2,13),(1,2,10),(1,3,12),(2,1,4),(2,4,14),(3,2,9),(3,5,20),(4,3,7),(4,5,4)]
Sample 1 output: edges of the min cut (e.g. [(1,3),(4,3),(4,5)] with capacity 23)


"""

def solve(n, edges):
    # Write your code here.
    return None
