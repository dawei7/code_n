"""Optimal app-local solution for LeetCode 384: Shuffle an Array."""

from random import randrange


def solve(nums: list[int], operations: list[str]) -> list[list[int]]:
    original = nums.copy()
    results: list[list[int]] = []

    for operation in operations:
        if operation == "reset":
            results.append(original.copy())
        elif operation == "shuffle":
            shuffled = original.copy()
            for index in range(len(shuffled) - 1):
                swap_index = randrange(index, len(shuffled))
                shuffled[index], shuffled[swap_index] = shuffled[swap_index], shuffled[index]
            results.append(shuffled)
        else:
            raise ValueError(f"Unsupported shuffle operation: {operation}")

    return results
