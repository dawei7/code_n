from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def can_win(used: int, remaining: int) -> bool:
            for choice in range(maxChoosableInteger, 0, -1):
                bit = 1 << (choice - 1)
                if used & bit:
                    continue
                if choice >= remaining or not can_win(used | bit, remaining - choice):
                    return True
            return False

        return can_win(0, desiredTotal)
