from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = list(prices)
        unresolved = []

        for index, price in enumerate(prices):
            while unresolved and prices[unresolved[-1]] >= price:
                result[unresolved.pop()] -= price
            unresolved.append(index)

        return result
