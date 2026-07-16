from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        streak = 0

        for value in arr:
            if value % 2:
                streak += 1
                if streak == 3:
                    return True
            else:
                streak = 0

        return False

