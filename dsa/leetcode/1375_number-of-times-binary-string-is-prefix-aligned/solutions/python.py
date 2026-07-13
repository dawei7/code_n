"""Optimal solution for LeetCode 1375: Number of Times Binary String Is Prefix-Aligned."""


def solve(flips: list[int]) -> int:
    answer = 0
    rightmost = 0
    for step, position in enumerate(flips, start=1):
        rightmost = max(rightmost, position)
        if rightmost == step:
            answer += 1
    return answer
