from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        maximum_factor = max(factor for factor, _ in items)
        frequencies = [0] * (maximum_factor + 1)
        for factor, _ in items:
            frequencies[factor] += 1

        divisible_counts = [0] * (maximum_factor + 1)
        for factor in range(1, maximum_factor + 1):
            divisible_counts[factor] = sum(
                frequencies[multiple]
                for multiple in range(factor, maximum_factor + 1, factor)
            )

        dp = [0] * (budget + 1)
        for factor, price in items:
            first_value = divisible_counts[factor]
            previous = dp[:]
            for capacity in range(price, budget + 1):
                dp[capacity] = max(
                    dp[capacity],
                    previous[capacity - price] + first_value,
                    dp[capacity - price] + 1,
                )

        return dp[budget]
