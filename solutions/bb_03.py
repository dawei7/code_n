"""
Description
-----------
Solve 0/1 knapsack via Least-Cost (LC) branch and
            bound. Sort items by value/weight ratio descending.
            Maintain a priority queue of live nodes ordered by
            their lower bound (LC = min cost). For each node
            popped, compute a fractional-knapsack upper bound
            for both children (include / exclude the current
            item); discard any child whose UB exceeds the
            current best lower bound. Stop when the priority
            queue is empty. The setup keeps n small (n <= 8)
            so brute-force verification is fast.
            Source: https://www.geeksforgeeks.org/dsa/0-1-knapsack-using-least-count-branch-and-bound/

Examples
--------
Example 1:
Input:  values = [10, 10, 12, 18], weights = [2, 4, 6, 9], capacity = 15, n = 4
Output: 38

Example 2:
Input:  values = [18, 20, 14, 18], weights = [6, 3, 5, 9], capacity = 21, n = 4
Output: 56
"""

def solve(values, weights, capacity, n):
    # Write your code here.
    return None
