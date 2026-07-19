"""Reference solution for LeetCode 1359."""


MODULUS = 1_000_000_007


def solve(n):
    count = 1
    for orders in range(1, n + 1):
        count = count * orders * (2 * orders - 1) % MODULUS
    return count
