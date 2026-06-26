"""
Description
-----------
Return the minimum number of trials needed in the worst
case to find the critical floor. dp[e][f] = min trials for
e eggs and f floors. Drop from floor x -> 1 + worst(
dp[e-1][x-1] (breaks), dp[e][f-x] (survives)).
Source: https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/

Examples
--------
Example 1:
Input:  eggs = 1, floors = 10
Output: 10

Example 2:
Input:  eggs = 2, floors = 6
Output: 3
"""

def solve(eggs, floors):
    # Write your code here.
    return None
