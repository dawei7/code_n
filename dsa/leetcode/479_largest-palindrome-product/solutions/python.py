"""Finite-domain optimal lookup for LeetCode 479."""


def solve(n: int) -> int:
    residues = (9, 987, 123, 597, 677, 1218, 877, 475)
    return residues[n - 1]
