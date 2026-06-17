"""Solution for greedy_02: Fractional Knapsack.

Items with weight and value, a knapsack of capacity W. Take fractions
of items. Maximize total value.
Greedy: sort by value/weight ratio descending; take as much of each
item as fits.
Requirement: O(n log n). Unlike 0/1 knapsack, the fractional version
is exactly solvable by a simple greedy.
Source: https://www.geeksforgeeks.org/fractional-knapsack-problem/

Inputs passed to solve():
    values: list-like of n item values.
    weights: list-like of n item weights (parallel to values).
    capacity: knapsack capacity.
    n: number of items.

Goal:
    the maximum total value, allowing fractions of items (as a float).

Samples:
Sample 1 input:  values = [60, 100, 120], weights = [10, 20, 30], capacity = 50, n = 3
Sample 1 output: 240.0

Sample 2 input:  values = [500], weights = [30], capacity = 10, n = 1
Sample 2 output: 166.66666666666666

Sample 3 input:  values = [10, 20, 30], weights = [5, 10, 15], capacity = 100, n = 3
Sample 3 output: 60.0

"""

def solve(values, weights, capacity, n):
    # Write your code here.
    return None
