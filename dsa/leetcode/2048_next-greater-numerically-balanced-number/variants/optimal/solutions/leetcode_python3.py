from bisect import bisect_right
from itertools import permutations


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        values = set()

        for mask in range(1, 1 << 7):
            digits = "".join(
                str(digit) * digit
                for digit in range(1, 8)
                if mask & (1 << (digit - 1))
            )
            if len(digits) <= 7:
                values.update(int("".join(order)) for order in permutations(digits))

        balanced = sorted(values)
        return balanced[bisect_right(balanced, n)]
