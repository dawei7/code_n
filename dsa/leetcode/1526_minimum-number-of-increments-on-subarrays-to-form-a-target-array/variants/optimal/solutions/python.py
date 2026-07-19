"""Optimal app-local solution for LeetCode 1526."""


def solve(target):
    answer = target[0]
    for previous, current in zip(target, target[1:]):
        if current > previous:
            answer += current - previous
    return answer
