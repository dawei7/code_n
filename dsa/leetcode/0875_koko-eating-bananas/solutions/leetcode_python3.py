from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            speed = (low + high) // 2
            required_hours = 0
            for pile in piles:
                required_hours += (pile + speed - 1) // speed
                if required_hours > h:
                    break

            if required_hours <= h:
                high = speed
            else:
                low = speed + 1

        return low
