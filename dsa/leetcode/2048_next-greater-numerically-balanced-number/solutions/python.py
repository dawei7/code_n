from bisect import bisect_right
from itertools import permutations


def _balanced_values() -> list[int]:
    values: set[int] = set()

    for mask in range(1, 1 << 7):
        digits = "".join(
            str(digit) * digit
            for digit in range(1, 8)
            if mask & (1 << (digit - 1))
        )
        if len(digits) <= 7:
            values.update(int("".join(order)) for order in permutations(digits))

    return sorted(values)


BALANCED_VALUES = _balanced_values()


def solve(n: int) -> int:
    return BALANCED_VALUES[bisect_right(BALANCED_VALUES, n)]
