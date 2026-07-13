import bisect
import math


def _build_prime_squares(limit: int = 1_000_000_000) -> list[int]:
    root = math.isqrt(limit)
    is_prime = [True] * (root + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, math.isqrt(root) + 1):
        if is_prime[p]:
            step_start = p * p
            is_prime[step_start : root + 1 : p] = [False] * (((root - step_start) // p) + 1)
    return [p * p for p in range(2, root + 1) if is_prime[p]]


_PRIME_SQUARES = _build_prime_squares()


def solve(l: int, r: int) -> int:
    left = bisect.bisect_left(_PRIME_SQUARES, l)
    right = bisect.bisect_right(_PRIME_SQUARES, r)
    return (r - l + 1) - (right - left)
