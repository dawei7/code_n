"""Solution for approx_03: TSP via MST (2-Approx).


            Given a complete graph with edge costs that satisfy
            the triangle inequality, return the cost of a TSP
            tour produced by the MST-based 2-approximation.
            Build a minimum spanning tree rooted at node 0
            (Prim's algorithm), do a preorder DFS walk to list
            vertices, and append 0 at the end. The returned
            tour cost is guaranteed to be at most 2x optimal
            for metric instances.
            Source: https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/
            

Inputs passed to solve():
    cost: n x n cost matrix satisfying the triangle inequality.
    n: number of cities.

Goal:
    the total cost of the 2-approximate TSP tour as a non-negative int.

Samples:
Sample 1 input:  cost = [[0, 111], [112, 0]], n = 2
Sample 1 output: 223

Sample 2 input:  cost = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]], n = 3
Sample 2 output: 3000 (or up to 2x optimal)


"""

def solve(cost, n):
    # Write your code here.
    return None
