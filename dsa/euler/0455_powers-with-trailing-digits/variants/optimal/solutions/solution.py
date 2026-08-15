"""Project Euler Problem 455: Powers with Trailing Digits.

Find sum_{n=2..10^6} f(n), where f(n) is the largest integer x < 10^9
such that n^x = x (mod 10^9), or 0 if no such integer exists.
"""

MOD = 1_000_000_000


def _search(n: int, modulo: int = MOD) -> int:
    if n % 10 == 0:
        return 0
    exponent = n
    while True:
        next_value = pow(n, exponent, modulo)
        if next_value == 0 or next_value == exponent:
            return next_value
        exponent = next_value


def solve(limit: int = 1_000_000, modulo: int = MOD) -> int:
    """Compute sum_{n=2..limit} f(n) using 10-adic fixed-point iteration."""
    total = 0
    for i in range(2, limit + 1):
        total += _search(i, modulo)
    return total


if __name__ == "__main__":
    print(solve())
