from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        original = sum(action * price for action, price in zip(strategy, prices))
        half = k // 2
        gain = sum(-strategy[index] * prices[index] for index in range(half)) + sum(
            (1 - strategy[index]) * prices[index] for index in range(half, k)
        )
        best_gain = max(0, gain)

        for left in range(1, len(prices) - k + 1):
            outgoing = left - 1
            midpoint = outgoing + half
            entering = outgoing + k
            gain += strategy[outgoing] * prices[outgoing]
            gain -= prices[midpoint]
            gain += (1 - strategy[entering]) * prices[entering]
            best_gain = max(best_gain, gain)

        return original + best_gain
