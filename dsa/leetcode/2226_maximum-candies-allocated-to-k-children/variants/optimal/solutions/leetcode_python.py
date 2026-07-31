from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 1
        high = min(max(candies), sum(candies) // k)
        answer = 0
        while low <= high:
            portion = (low + high) // 2
            children = sum(pile // portion for pile in candies)
            if children >= k:
                answer = portion
                low = portion + 1
            else:
                high = portion - 1
        return answer
