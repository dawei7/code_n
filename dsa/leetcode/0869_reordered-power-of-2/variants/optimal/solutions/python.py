"""Optimal app-local solution for LeetCode 869."""


def _digit_signature(value):
    counts = [0] * 10
    while value:
        counts[value % 10] += 1
        value //= 10
    return tuple(counts)


_POWER_OF_TWO_SIGNATURES = {
    _digit_signature(1 << exponent) for exponent in range(34)
}


def solve(n):
    return _digit_signature(n) in _POWER_OF_TWO_SIGNATURES
