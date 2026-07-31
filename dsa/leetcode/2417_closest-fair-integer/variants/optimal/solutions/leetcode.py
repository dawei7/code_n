from functools import lru_cache


class Solution:
    def closestFair(self, n: int) -> int:
        target = str(n)
        if len(target) % 2 == 1:
            target = "1" + "0" * len(target)

        digit_count = len(target)
        required_even = digit_count // 2

        @lru_cache(maxsize=None)
        def build(position: int, even_used: int, tight: bool):
            if position == digit_count:
                return "" if even_used == required_even else None

            lower = int(target[position]) if tight else 0
            if position == 0:
                lower = max(lower, 1)

            for digit in range(lower, 10):
                next_even = even_used + (digit % 2 == 0)
                remaining = digit_count - position - 1
                if next_even > required_even or next_even + remaining < required_even:
                    continue
                suffix = build(
                    position + 1,
                    next_even,
                    tight and digit == int(target[position]),
                )
                if suffix is not None:
                    return str(digit) + suffix
            return None

        result = build(0, 0, True)
        if result is None:
            digit_count += 2
            required_even = digit_count // 2
            target = "1" + "0" * (digit_count - 1)
            build.cache_clear()
            result = build(0, 0, True)
        return int(result)
