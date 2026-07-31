from functools import lru_cache
from math import gcd


def solve(n):
    allowed_masks = []
    for position in range(1, n + 1):
        allowed = 0
        for value in range(1, n + 1):
            if gcd(value, position) == 1:
                allowed |= 1 << (value - 1)
        allowed_masks.append(allowed)

    @lru_cache(maxsize=None)
    def count(used):
        position = used.bit_count()
        if position == n:
            return 1

        choices = allowed_masks[position] & ~used
        total = 0
        while choices:
            bit = choices & -choices
            choices -= bit
            total += count(used | bit)
        return total

    return count(0)
