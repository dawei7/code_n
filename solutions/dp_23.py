"""
Description
-----------
Minimum cost to reach the top of a staircase where you
may climb 1 or 2 steps at a time. cost[i] is the cost of
step i. dp[i] = cost[i] + min(dp[i-1], dp[i-2]). The
answer is min(dp[n-1], dp[n-2]) - either of the last two.
Source: https://www.geeksforgeeks.org/min-cost-climbing-stairs/

Examples
--------
Example 1:
Input:  cost = [10, 15, 20], n = 3
Output: 15 (start at step 1)

Example 2:
Input:  cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], n = 10
Output: 6
"""

def solve(cost, n):
    # Write your code here.
    return None
