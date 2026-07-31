"""Optimal app-local solution for LeetCode 991."""


def solve(startValue, target):
    operations = 0

    while target > startValue:
        if target % 2:
            target += 1
        else:
            target //= 2
        operations += 1

    return operations + startValue - target
