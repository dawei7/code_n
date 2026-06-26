"""
Description
-----------
Solve the traveling salesman problem using the
            reduced-matrix branch-and-bound method. Each node
            in the search tree is a state (current path, cost
            so far, the reduced cost matrix). Branching:
            include or exclude the next unvisited city's edge.
            Bounding: subtract the row and column minimums to
            produce a 'reduced' matrix; the cost of the
            reduction is the lower bound. The algorithm uses
            a priority queue (min-heap) of live nodes keyed by
            their lower bound; the goal is to find a complete
            tour with the minimum total cost. Return the
            minimum tour cost.
            Source: https://www.geeksforgeeks.org/dsa/travelling-salesman-problem-tsp-using-reduced-matrix-method/

Examples
--------
Example 1:
Input:  cost = [[INF, 10, 15, 20], [10, INF, 35, 25], [15, 35, INF, 30], [20, 25, 30, INF]], n = 4
Output: 80 (the optimal tour)
"""

def solve(cost, n):
    # Write your code here.
    return None
