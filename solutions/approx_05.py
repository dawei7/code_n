"""
Description
-----------
Given n items each with a value and a weight, and a
            knapsack with capacity C, return the maximum total
            value of items (or fractions thereof) you can fit.
            The fractional variant allows taking partial items,
            so the greedy by value/weight ratio is OPTIMAL
            (not just an approximation). Sort items by value/
            weight ratio descending, take each whole item while
            capacity allows, then fill the remainder with a
            fraction of the next item.
            Source: https://www.geeksforgeeks.org/dsa/fractional-knapsack-problem/

Examples
--------
Example 1:
Input:  values = [60, 100, 120], weights = [10, 20, 30], n = 3, capacity = 50
Output: 240.0

Example 2:
Input:  values = [500], weights = [30], n = 1, capacity = 10
Output: 166.666... (500 * 10/30)
"""

def solve(values, weights, n, capacity):
    # Write your code here.
    return None
