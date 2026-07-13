"""Memoized interval dynamic programming for LeetCode 546."""

from functools import lru_cache


def solve(boxes: list[int]) -> int:
    @lru_cache(maxsize=None)
    def best(left: int, right: int, carried: int) -> int:
        if left > right:
            return 0

        while right > left and boxes[right] == boxes[right - 1]:
            right -= 1
            carried += 1

        answer = best(left, right - 1, 0) + (carried + 1) ** 2

        for index in range(left, right):
            if boxes[index] == boxes[right]:
                answer = max(
                    answer,
                    best(left, index, carried + 1)
                    + best(index + 1, right - 1, 0),
                )

        return answer

    return best(0, len(boxes) - 1, 0)

