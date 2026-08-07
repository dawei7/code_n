from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        frequencies = [0] * (max(costs) + 1)
        for cost in costs:
            frequencies[cost] += 1

        bars = 0
        for cost in range(1, len(frequencies)):
            affordable = min(frequencies[cost], coins // cost)
            bars += affordable
            coins -= affordable * cost
            if affordable < frequencies[cost]:
                break
        return bars
