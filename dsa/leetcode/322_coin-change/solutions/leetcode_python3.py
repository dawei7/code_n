from typing import List


def _coin_change(coins: List[int], amount: int) -> int:
    unreachable = amount + 1
    minimum = [0] + [unreachable] * amount
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                minimum[total] = min(minimum[total], minimum[total - coin] + 1)
    return -1 if minimum[amount] == unreachable else minimum[amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return _coin_change(coins, amount)
