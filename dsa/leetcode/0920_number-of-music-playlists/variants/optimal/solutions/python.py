"""Optimal app-local solution for LeetCode 920."""


def solve(n, goal, k):
    modulus = 1_000_000_007
    previous = [0] * (n + 1)
    previous[0] = 1

    for length in range(1, goal + 1):
        current = [0] * (n + 1)
        for used in range(1, min(length, n) + 1):
            add_new = previous[used - 1] * (n - used + 1)
            replay = previous[used] * max(used - k, 0)
            current[used] = (add_new + replay) % modulus
        previous = current

    return previous[n]

