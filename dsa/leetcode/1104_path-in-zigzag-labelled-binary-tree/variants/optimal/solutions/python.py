"""Optimal app-local solution for LeetCode 1104."""


def solve(label: int) -> list[int]:
    reversed_path = []
    while label:
        reversed_path.append(label)
        depth = label.bit_length() - 1
        start = 1 << depth
        end = (1 << (depth + 1)) - 1
        label = (start + end - label) // 2
    return reversed_path[::-1]
