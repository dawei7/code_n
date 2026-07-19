from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def feasible(distance: int) -> bool:
            placed = 1
            last = position[0]
            for point in position[1:]:
                if point - last >= distance:
                    placed += 1
                    last = point
                    if placed == m:
                        return True
            return False

        low = 1
        high = (position[-1] - position[0]) // (m - 1)

        while low <= high:
            middle = (low + high) // 2
            if feasible(middle):
                low = middle + 1
            else:
                high = middle - 1

        return high

