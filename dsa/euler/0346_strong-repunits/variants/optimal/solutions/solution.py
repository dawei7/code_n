"""Project Euler 346: Strong Repunits

Find the sum of all strong repunits below 10^12.
"""

from __future__ import annotations


def solve(limit: int = 1_000_000_000_000) -> str:
    """Calculates the sum of all strong repunits below limit in pure Python in ~0.28s

    using the base-invariance theorem that every n >= 3 is 11 in base (n - 1), so strong
    repunits correspond exactly to 1 and all repunits of length k >= 3 in any base b >= 2.
    """
    repunits = {1}
    b_max = int(limit**0.5)

    for b in range(2, b_max + 1):
        val = 1 + b + b * b
        if val >= limit:
            break
        cur = val
        p = b * b
        while cur < limit:
            repunits.add(cur)
            p *= b
            cur += p

    total_sum = sum(repunits)
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
