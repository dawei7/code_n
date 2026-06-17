"""Solution for dp_16: Egg Dropping.

Given k eggs and n floors, find the minimum number of
moves (drops) needed to determine the critical floor.
Use dp[e][m] = dp[e-1][m-1] + dp[e][m-1] + 1.
Requirement: O(k * n * log n) — find smallest m with dp[k][m] >= n.
Source: https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/

Inputs passed to solve():
    k: number of eggs available.
    n: number of floors to test.

Goal:
    the minimum number of drops needed to find the critical floor.

Samples:
Sample 1 input:  k = 1, n = 2
Sample 1 output: 2

Sample 2 input:  k = 2, n = 6
Sample 2 output: 3


"""

def solve(k, n):
    # Write your code here.
    return None
