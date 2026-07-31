from typing import List


def solve(nums: List[int]) -> int:
    current = list(nums)

    while len(current) > 1:
        current = [
            (
                min(current[2 * index], current[2 * index + 1])
                if index % 2 == 0
                else max(current[2 * index], current[2 * index + 1])
            )
            for index in range(len(current) // 2)
        ]

    return current[0]
