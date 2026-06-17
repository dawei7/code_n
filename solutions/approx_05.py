"""Solution for approx_05: Fractional Knapsack (Greedy).


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
            

Inputs passed to solve():
    values: list of n item values.
    weights: list of n item weights (all > 0).
    n: number of items.
    capacity: knapsack capacity (originally W in the GfG notation).

Goal:
    the maximum total value achievable (a float).

Samples:
Sample 1 input:  values = [60, 100, 120], weights = [10, 20, 30], n = 3, capacity = 50
Sample 1 output: 240.0

Sample 2 input:  values = [500], weights = [30], n = 1, capacity = 10
Sample 2 output: 166.666... (500 * 10/30)


"""

def solve(values, weights, n, capacity):
    # Write your code here.
    return None
