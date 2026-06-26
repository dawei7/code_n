"""
Description
-----------
Given a complete graph with edge costs that satisfy
            the triangle inequality, return the cost of a TSP
            tour produced by the MST-based 2-approximation.
            Build a minimum spanning tree rooted at node 0
            (Prim's algorithm), do a preorder DFS walk to list
            vertices, and append 0 at the end. The returned
            tour cost is guaranteed to be at most 2x optimal
            for metric instances.
            Source: https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/

Examples
--------
Example 1:
Input:  cost = [[0, 111], [112, 0]], n = 2
Output: 223

Example 2:
Input:  cost = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]], n = 3
Output: 3000 (or up to 2x optimal)
"""

def solve(cost, n):
    # Write your code here.
    return None
