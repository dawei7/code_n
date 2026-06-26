"""
Description
-----------
Given k eggs and n floors, find the minimum number of
moves (drops) needed to determine the critical floor.
Use dp[e][m] = dp[e-1][m-1] + dp[e][m-1] + 1.
Requirement: O(k * n * log n) — find smallest m with dp[k][m] >= n.
Source: https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/

Examples
--------
Example 1:
Input:  k = 1, n = 2
Output: 2

Example 2:
Input:  k = 2, n = 6
Output: 3
"""

def solve(k, n):
    # Write your code here.
    return None
