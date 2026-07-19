"""Optimal solution for LeetCode 1109: Corporate Flight Bookings."""


def solve(bookings: list[list[int]], n: int) -> list[int]:
    diff = [0] * (n + 1)
    for first, last, seats in bookings:
        diff[first - 1] += seats
        diff[last] -= seats

    answer = []
    current = 0
    for i in range(n):
        current += diff[i]
        answer.append(current)
    return answer
