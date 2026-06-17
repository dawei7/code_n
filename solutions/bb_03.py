"""Solution for bb_03: 0/1 Knapsack (Least-Cost B&B).


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
            

Inputs passed to solve():
    values: list of n item values.
    weights: list of n item weights (all > 0).
    capacity: knapsack capacity.
    n: number of items.

Goal:
    the maximum total value of items fitting in the knapsack (int).

Samples:
Sample 1 input:  values = [10, 10, 12, 18], weights = [2, 4, 6, 9], capacity = 15, n = 4
Sample 1 output: 38

Sample 2 input:  values = [18, 20, 14, 18], weights = [6, 3, 5, 9], capacity = 21, n = 4
Sample 2 output: 56


"""

def solve(values, weights, capacity, n):
    # Write your code here.
    return None
