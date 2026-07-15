"""Optimal app-local solution for LeetCode 1411."""


_MODULUS = 1_000_000_007


def solve(n: int) -> int:
    aba = abc = 6
    for _ in range(1, n):
        aba, abc = (3 * aba + 2 * abc) % _MODULUS, (2 * aba + 2 * abc) % _MODULUS
    return (aba + abc) % _MODULUS
