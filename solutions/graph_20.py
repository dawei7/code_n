"""Solution for graph_20: Travelling Salesman (Held-Karp DP).

Given a distance matrix, find the minimum-cost
Hamiltonian cycle (visit every city exactly once,
return to start). Held-Karp DP: dp[mask][i] = min
cost to visit exactly the cities in ``mask`` and end
at city i. Recurrence adds one city at a time.
Source: https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/

Inputs passed to solve():
    dist: n x n distance matrix.
    n: number of cities.

Goal:
    the minimum Hamiltonian cycle cost.

Samples:
Sample 1 input:  dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]], n = 4
Sample 1 output: 80 (0->1->2->3->0 or 0->3->2->1->0)


"""

def solve(dist, n):
    # Write your code here.
    return None
