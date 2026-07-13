"""Optimal app-local solution for LeetCode 445."""


def solve(l1: list[int], l2: list[int]) -> list[int]:
    first = list(l1)
    second = list(l2)
    reversed_result: list[int] = []
    carry = 0

    while first or second or carry:
        total = carry
        if first:
            total += first.pop()
        if second:
            total += second.pop()
        reversed_result.append(total % 10)
        carry = total // 10

    return reversed_result[::-1]
