from functools import lru_cache


def solve(num1: int, num2: int) -> int:

    def prefix(bound: int) -> int:
        if bound <= 0:
            return 0
        digits = tuple(map(int, str(bound)))

        @lru_cache(None)
        def count(position: int, tight: bool, previous_previous: int, previous: int) -> tuple[int, int]:
            if position == len(digits):
                return (1, 0)
            limit = digits[position] if tight else 9
            ways = 0
            waviness = 0
            for digit in range(limit + 1):
                next_tight = tight and digit == limit
                if previous == -1 and digit == 0:
                    suffix_ways, suffix_waviness = count(position + 1, next_tight, -1, -1)
                    added = 0
                else:
                    suffix_ways, suffix_waviness = count(position + 1, next_tight, previous, digit)
                    added = int(
                        previous_previous != -1
                        and (
                            previous > previous_previous
                            and previous > digit
                            or (previous < previous_previous and previous < digit)
                        )
                    )
                ways += suffix_ways
                waviness += suffix_waviness + added * suffix_ways
            return (ways, waviness)

        return count(0, True, -1, -1)[1]

    return prefix(num2) - prefix(num1 - 1)
