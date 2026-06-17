"""Solution for dp_23: Min Cost Climbing Stairs.

Minimum cost to reach the top of a staircase where you
may climb 1 or 2 steps at a time. cost[i] is the cost of
step i. dp[i] = cost[i] + min(dp[i-1], dp[i-2]). The
answer is min(dp[n-1], dp[n-2]) - either of the last two.
Source: https://www.geeksforgeeks.org/min-cost-climbing-stairs/

Inputs passed to solve():
    cost: list of n step costs.
    n: length of cost.

Goal:
    the minimum total cost to reach the top.

Samples:
Sample 1 input:  cost = [10, 15, 20], n = 3
Sample 1 output: 15 (start at step 1)

Sample 2 input:  cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], n = 10
Sample 2 output: 6


"""

def solve(cost, n):
    # Write your code here.
    return None
