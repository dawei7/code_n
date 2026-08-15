"""Project Euler Problem 676: Matching Digit Sums.

Find sum_{k=3}^6 sum_{l=1}^{k-2} M(10^16, 2^k, 2^l) mod 10^16, where M(n, b1, b2) is the sum
of natural numbers i <= n with d(i, b1) = d(i, b2).
"""

from typing import Dict, Tuple

_MOD = 10**16


def _m_power2_bases(n: int, k: int, l: int) -> int:
    """Return M(n, 2^k, 2^l) using binary digital dynamic programming."""
    if n <= 0:
        return 0

    bits = [int(c) for c in bin(n)[2:]]
    num_bits = len(bits)

    tight: Dict[int, Tuple[int, int]] = {0: (1, 0)}
    loose: Dict[int, Tuple[int, int]] = {}

    for idx, lim in enumerate(bits):
        p = num_bits - 1 - idx
        c = (1 << (p % k)) - (1 << (p % l))
        w = 1 << p

        new_tight: Dict[int, Tuple[int, int]] = {}
        new_loose: Dict[int, Tuple[int, int]] = {}

        for diff, (cnt, sm) in loose.items():
            a, b = new_loose.get(diff, (0, 0))
            new_loose[diff] = (a + cnt, b + sm)

            d1 = diff + c
            a, b = new_loose.get(d1, (0, 0))
            new_loose[d1] = (a + cnt, b + sm + w * cnt)

        for diff, (cnt, sm) in tight.items():
            if lim == 0:
                a, b = new_tight.get(diff, (0, 0))
                new_tight[diff] = (a + cnt, b + sm)
            else:
                a, b = new_loose.get(diff, (0, 0))
                new_loose[diff] = (a + cnt, b + sm)

                d1 = diff + c
                a, b = new_tight.get(d1, (0, 0))
                new_tight[d1] = (a + cnt, b + sm + w * cnt)

        tight, loose = new_tight, new_loose

    ans = 0
    if 0 in tight:
        ans += tight[0][1]
    if 0 in loose:
        ans += loose[0][1]
    return ans


def solve(n: int = 10_000_000_000_000_000, mod: int = _MOD) -> int:
    """Find the sum of M(n, 2^k, 2^l) over 3 <= k <= 6 and 1 <= l <= k - 2."""
    total = 0
    for k in range(3, 7):
        for l in range(1, k - 1):
            total = (total + _m_power2_bases(n, k, l)) % mod
    return total


if __name__ == "__main__":
    print(solve())
