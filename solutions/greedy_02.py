"""
Description
-----------
Items with weight and value, a knapsack of capacity W. Take fractions
of items. Maximize total value.
Greedy: sort by value/weight ratio descending; take as much of each
item as fits.
Requirement: O(n log n). Unlike 0/1 knapsack, the fractional version
is exactly solvable by a simple greedy.
Source: https://www.geeksforgeeks.org/fractional-knapsack-problem/

Examples
--------
Example 1:
Input:  values = [60, 100, 120], weights = [10, 20, 30], capacity = 50, n = 3
Output: 240.0

Example 2:
Input:  values = [500], weights = [30], capacity = 10, n = 1
Output: 166.66666666666666

Example 3:
Input:  values = [10, 20, 30], weights = [5, 10, 15], capacity = 100, n = 3
Output: 60.0
"""

def solve(values, weights, capacity, n):
    # Write your code here.
    return None
