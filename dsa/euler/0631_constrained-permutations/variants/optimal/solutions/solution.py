"""Project Euler Problem 631: Constrained Permutations.

Find f(10^18, 40) mod 1000000007, where f(n, m) is the number of permutations of length
at most n avoiding pattern 1243 with at most m inversions.
"""

from typing import Dict, Tuple

_MOD = 1_000_000_007


def solve(n: int = 10**18, m: int = 40) -> int:
    """Compute f(n, m) modulo 1000000007 using pattern-avoidance state stabilization DP."""
    layer: Dict[Tuple[int, int, int], int] = {(m, 0, 0): 1}
    total = 1
    explicit_limit = min(n, m + 2)

    for length in range(1, explicit_limit + 1):
        next_layer: Dict[Tuple[int, int, int], int] = {}

        for (remaining, lower, threshold), count in layer.items():
            upper = min(remaining + 1, length)
            for inversions in range(lower, upper):
                if inversions < threshold:
                    next_state = (
                        remaining - inversions,
                        inversions + 1,
                        threshold + 1,
                    )
                else:
                    next_state = (remaining - inversions, lower, inversions)

                next_layer[next_state] = (
                    next_layer.get(next_state, 0) + count
                ) % _MOD

        layer = next_layer
        total = (total + sum(layer.values())) % _MOD

    if n > m + 2:
        stable_count = sum(layer.values()) % _MOD
        total = (total + ((n - (m + 2)) % _MOD) * stable_count) % _MOD

    return total


if __name__ == "__main__":
    print(solve())
