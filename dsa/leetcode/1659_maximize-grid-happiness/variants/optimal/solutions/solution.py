from functools import lru_cache


class Solution:
    def getMaxGridHappiness(
        self,
        m: int,
        n: int,
        introvertsCount: int,
        extrovertsCount: int,
    ) -> int:
        rows, cols = max(m, n), min(m, n)
        states = 3**cols
        top_place = 3 ** (cols - 1)

        def interaction(first: int, second: int) -> int:
            if first == 0 or second == 0:
                return 0
            if first == 1 and second == 1:
                return -60
            if first == 2 and second == 2:
                return 40
            return -10

        @lru_cache(None)
        def dp(position: int, mask: int, introverts: int, extroverts: int) -> int:
            if position == rows * cols or (introverts == 0 and extroverts == 0):
                return 0

            column = position % cols
            above = mask // top_place
            left = mask % 3 if column else 0
            shifted = mask * 3 % states
            best = dp(position + 1, shifted, introverts, extroverts)

            if introverts:
                gain = 120 + interaction(1, above) + interaction(1, left)
                best = max(best, gain + dp(position + 1, shifted + 1, introverts - 1, extroverts))
            if extroverts:
                gain = 40 + interaction(2, above) + interaction(2, left)
                best = max(best, gain + dp(position + 1, shifted + 2, introverts, extroverts - 1))
            return best

        return dp(0, 0, introvertsCount, extrovertsCount)
