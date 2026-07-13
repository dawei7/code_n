import functools
import math


def solve(locks: list[int], k: int) -> int:
    n = len(locks)

    @functools.lru_cache(None)
    def dp(mask: int) -> int:
        broken = mask.bit_count()
        if broken == n:
            return 0

        factor = 1 + broken * k
        best = math.inf

        for index, strength in enumerate(locks):
            if mask & (1 << index):
                continue
            minutes = math.ceil(strength / factor)
            best = min(best, minutes + dp(mask | (1 << index)))

        return best

    return dp(0)
