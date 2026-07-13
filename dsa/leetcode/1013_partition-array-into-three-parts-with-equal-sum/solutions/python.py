"""Optimal solution for LeetCode 1013: Partition Array Into Three Parts With Equal Sum."""


def solve(arr: list[int]) -> bool:
    total = sum(arr)
    if total % 3 != 0:
        return False

    target = total // 3
    parts = 0
    current = 0
    for value in arr:
        current += value
        if current == target:
            parts += 1
            current = 0
    return parts >= 3
