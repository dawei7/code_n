from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        modulus = 1_000_000_007
        levels = sorted(inventory, reverse=True) + [0]
        profit = 0

        for index in range(len(inventory)):
            colors = index + 1
            high = levels[index]
            low = levels[index + 1]
            band_size = (high - low) * colors

            if orders >= band_size:
                profit += colors * (high + low + 1) * (high - low) // 2
                orders -= band_size
            else:
                full_levels, remainder = divmod(orders, colors)
                cutoff = high - full_levels
                profit += colors * (high + cutoff + 1) * full_levels // 2
                profit += remainder * cutoff
                break

        return profit % modulus
