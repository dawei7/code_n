"""Optimal app-local solution for LeetCode 967."""


def solve(n, k):
    frontier = list(range(1, 10))
    for _ in range(n - 1):
        next_frontier = []
        for number in frontier:
            last_digit = number % 10
            for next_digit in {last_digit - k, last_digit + k}:
                if 0 <= next_digit <= 9:
                    next_frontier.append(number * 10 + next_digit)
        frontier = next_frontier
    return frontier
