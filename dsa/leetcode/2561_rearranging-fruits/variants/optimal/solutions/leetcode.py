from collections import Counter


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        difference = Counter(basket1)
        difference.subtract(basket2)
        minimum = min(min(basket1), min(basket2))
        misplaced = []

        for fruit, delta in difference.items():
            if delta % 2:
                return -1
            misplaced.extend([fruit] * (abs(delta) // 2))

        misplaced.sort()
        swaps = len(misplaced) // 2
        return sum(min(fruit, 2 * minimum) for fruit in misplaced[:swaps])
