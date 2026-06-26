"""
Description
-----------
Given a complete metric graph, return the cost of
            a TSP tour produced by the Christofides 1.5-approx
            algorithm: (1) build an MST, (2) find the odd-
            degree vertices of the MST, (3) compute a minimum-
            weight perfect matching on those vertices, (4)
            unite matching + MST, (5) find an Eulerian circuit,
            and (6) shortcut to a Hamiltonian tour. The result
            is at most 1.5x the optimal tour cost.
            Source: https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/

Examples
--------
Example 1:
Input:  cost = [[0, 111], [112, 0]], n = 2
Output: 223

Example 2:
Input:  cost = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]], n = 3
Output: 3000 (Christofides is optimal for n = 3)
"""

def solve(cost, n):
    # Write your code here.
    return None
