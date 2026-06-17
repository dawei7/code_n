"""Solution for dp_05: Coin Change.

Given a list of coin denominations and a target amount,
return the minimum number of coins needed to make the
amount. Return -1 if it is impossible.
The setup always includes coin 1, so the answer is always
finite (1 is the worst case).
Requirement: O(n * amount) where n is the number of coins.
Source: https://www.geeksforgeeks.org/coin-change-dp-7/

Inputs passed to solve():
    coins: list of positive integer coin denominations.
    amount: the target sum to make.

Goal:
    the minimum number of coins summing to amount, or -1.

Samples:
Sample 1 input:  coins = [1, 5, 10, 25], amount = 11
Sample 1 output: 2 (10+1)

Sample 2 input:  coins = [2], amount = 3
Sample 2 output: -1

Sample 3 input:  coins = [1, 2, 5], amount = 7
Sample 3 output: 2 (5+2)

"""

def solve(coins, amount):
    # Write your code here.
    return None
