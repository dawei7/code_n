from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        total = 0
        for count, apple_weight in enumerate(sorted(weight)):
            if total + apple_weight > 5000:
                return count
            total += apple_weight
        return len(weight)
