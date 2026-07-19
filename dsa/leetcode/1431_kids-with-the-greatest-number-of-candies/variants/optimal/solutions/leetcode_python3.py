from typing import List


class Solution:
    def kidsWithCandies(
        self,
        candies: List[int],
        extraCandies: int,
    ) -> List[bool]:
        greatest = max(candies)
        return [candy + extraCandies >= greatest for candy in candies]
