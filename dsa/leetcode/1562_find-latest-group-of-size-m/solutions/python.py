"""Optimal app-local solution for LeetCode 1562."""


def solve(arr: list[int], m: int) -> int:
    """Merge adjacent one-runs and track the count of target-sized groups."""
    n = len(arr)
    length = [0] * (n + 2)
    groups_of_size_m = 0
    answer = -1

    for step, position in enumerate(arr, 1):
        left = length[position - 1]
        right = length[position + 1]
        merged = left + 1 + right
        if left == m:
            groups_of_size_m -= 1
        if right == m:
            groups_of_size_m -= 1
        if merged == m:
            groups_of_size_m += 1
        length[position - left] = merged
        length[position + right] = merged
        if groups_of_size_m:
            answer = step

    return answer
