from typing import List


class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def parity_counts(values: List[int]) -> tuple[int, int]:
            odd = sum(value.bit_count() & 1 for value in values)
            return len(values) - odd, odd

        a_even, a_odd = parity_counts(a)
        b_even, b_odd = parity_counts(b)
        c_even, c_odd = parity_counts(c)

        return a_even * b_even * c_even + a_even * b_odd * c_odd + a_odd * b_even * c_odd + a_odd * b_odd * c_even
