"""Solution for greedy_10: Minimum Coins.

Given coin denominations and a target amount, return the minimum number
of coins to make the amount. Greedy (always take the largest coin that
fits) is optimal only for canonical denomination sets like 1, 5, 10, 25.
For non-canonical sets use the DP variant.
Requirement: O(n log n) for the sort, O(n) for the greedy.
Source: https://www.geeksforgeeks.org/greedy-algorithms-set-of-coin-change-problem/

Inputs passed to solve():
    coins: list of available coin denominations.
    amount: target amount to make.

Goal:
    the minimum number of coins needed, or -1 if the amount cannot be made.

Samples:
Sample 1 input:  coins = [1, 5, 10, 25], amount = 41
Sample 1 output: 4

Sample 2 input:  coins = [1, 5, 10, 25], amount = 11
Sample 2 output: 2

Sample 3 input:  coins = [1, 5, 10, 25], amount = 7
Sample 3 output: 3

"""

def solve(coins, amount):
    # Write your code here.
    return None
