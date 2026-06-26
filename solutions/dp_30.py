"""
Description
-----------
Count the number of ways to make amount using the
given coin denominations (unlimited supply, order
doesn't matter). DP: dp[a] = number of ways to make a.
For each coin c, dp[a] += dp[a - c]. O(n * amount).
Source: https://www.geeksforgeeks.org/coin-change-dp-7/

Examples
--------
Example 1:
Input:  coins = [1, 2, 3], n = 3, amount = 4
Output: 4 (1111, 112, 22, 13)

Example 2:
Input:  coins = [1, 5, 6], n = 3, amount = 7
Output: 2 (1111111, 16)
"""

def solve(coins, n, amount):
    # Write your code here.
    return None
