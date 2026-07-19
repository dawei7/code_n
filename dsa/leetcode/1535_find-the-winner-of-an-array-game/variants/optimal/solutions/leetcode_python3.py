from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        champion = arr[0]
        streak = 0
        for challenger in arr[1:]:
            if champion > challenger:
                streak += 1
            else:
                champion = challenger
                streak = 1
            if streak == k:
                return champion
        return champion
