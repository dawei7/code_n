"""Solution for dp_30: Coin Change (Count Ways).

Count the number of ways to make ``amount`` using the
given coin denominations (unlimited supply, order
doesn't matter). DP: dp[a] = number of ways to make a.
For each coin c, dp[a] += dp[a - c]. O(n * amount).
Source: https://www.geeksforgeeks.org/coin-change-dp-7/

Inputs passed to solve():
    coins: list of n coin denominations (unlimited supply).
    n: number of coin types.
    amount: target amount (always 1..12 in the setup).

Goal:
    the number of ways to make amount.

Samples:
Sample 1 input:  coins = [1, 2, 3], n = 3, amount = 4
Sample 1 output: 4 (1111, 112, 22, 13)

Sample 2 input:  coins = [1, 5, 6], n = 3, amount = 7
Sample 2 output: 2 (1111111, 16)


"""

def solve(coins, n, amount):
    # Write your code here.
    return None
