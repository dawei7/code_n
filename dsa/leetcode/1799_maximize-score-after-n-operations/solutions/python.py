from functools import cache
from math import gcd


def solve(nums: list[int]) -> int:
    length = len(nums)
    pair_gcd = [
        [gcd(nums[i], nums[j]) for j in range(length)]
        for i in range(length)
    ]

    @cache
    def best(mask: int) -> int:
        operation = mask.bit_count() // 2 + 1
        answer = 0

        for i in range(length):
            if mask & (1 << i):
                continue
            for j in range(i + 1, length):
                if mask & (1 << j):
                    continue
                next_mask = mask | (1 << i) | (1 << j)
                answer = max(
                    answer,
                    operation * pair_gcd[i][j] + best(next_mask),
                )

        return answer

    return best(0)
