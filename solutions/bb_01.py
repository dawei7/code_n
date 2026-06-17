"""Solution for bb_01: 0/1 Knapsack.

Given a list of items (each with a value and a weight) and
a knapsack with a weight capacity, return the maximum total
value of items you can fit. Each item is either in the
knapsack or not. Exhaustive recursive search (a real solver
would use DP or branch-and-bound with a fractional relaxation).
Source: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

Inputs passed to solve():
    values: list of n values.
    weights: list of n weights (parallel to values).
    capacity: maximum total weight.
    n: number of items.

Goal:
    the maximum total value of items that fit in the knapsack.

Samples:
Sample 1 input:  values = [60, 100, 120], weights = [10, 20, 30], capacity = 50, n = 3
Sample 1 output: 220 (items 1+2)

Sample 2 input:  values = [10, 20, 30], weights = [1, 1, 1], capacity = 2, n = 3
Sample 2 output: 50 (items 1+2)


"""

def solve(values, weights, capacity, n):
    # Write your code here.
    return None
