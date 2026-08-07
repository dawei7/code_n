from typing import List


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        maximum_price = max(prices)

        def update(tree: List[int], index: int, value: int) -> None:
            while index < len(tree):
                tree[index] = max(tree[index], value)
                index += index & -index

        def query(tree: List[int], index: int) -> int:
            best = 0
            while index > 0:
                best = max(best, tree[index])
                index -= index & -index
            return best

        tree = [0] * (maximum_price + 2)
        best_left = [0] * len(prices)

        for index, (price, profit) in enumerate(zip(prices, profits)):
            best_left[index] = query(tree, price - 1)
            update(tree, price, profit)

        tree = [0] * (maximum_price + 2)
        answer = -1

        for index in range(len(prices) - 1, -1, -1):
            reverse_price = maximum_price - prices[index] + 1
            best_right = query(tree, reverse_price - 1)
            if best_left[index] and best_right:
                answer = max(answer, best_left[index] + profits[index] + best_right)
            update(tree, reverse_price, profits[index])

        return answer
