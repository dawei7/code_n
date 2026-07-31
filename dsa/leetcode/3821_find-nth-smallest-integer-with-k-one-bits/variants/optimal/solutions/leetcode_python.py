from math import comb


class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        answer = 0
        remaining_rank = n
        remaining_ones = k

        for position in range(49, -1, -1):
            if remaining_ones == 0:
                break

            with_zero = (
                comb(position, remaining_ones)
                if remaining_ones <= position
                else 0
            )

            if remaining_rank > with_zero:
                answer |= 1 << position
                remaining_rank -= with_zero
                remaining_ones -= 1

        return answer
