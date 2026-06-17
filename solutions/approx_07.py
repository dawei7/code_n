"""Solution for approx_07: 0/1 Knapsack FPTAS.


            Given n items with values and weights and capacity
            C, return a (1 - eps)-approximation of the maximum
            knapsack value. Standard FPTAS: scale all values
            by K / (eps * V_max) where V_max is the largest
            value; round to integers; run the O(nC') pseudo-
            polynomial DP (where C' is the scaled max weight);
            return the original-value best DP result. The
            scaled value is within (1 - eps) of the true OPT.
            Source: https://www.geeksforgeeks.org/dsa/fptas-fully-polynomial-time-approximation-scheme/
            

Inputs passed to solve():
    values: list of n item values.
    weights: list of n item weights (all > 0).
    n: number of items.
    capacity: knapsack capacity (originally W in the GfG notation).
    eps: approximation parameter (e.g. 0.1 for 10%).

Goal:
    an approximate maximum knapsack value (int or float).

Samples:
Sample 1 input:  values = [60, 100, 120], weights = [10, 20, 30], n = 3, capacity = 50, eps = 0.1
Sample 1 output: ~ 220 (within 10% of OPT 220)


"""

def solve(values, weights, n, capacity, eps):
    # Write your code here.
    return None
