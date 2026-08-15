"""Project Euler Problem 538: Maximum Quadrilaterals.

Find sum_{n=4..3_000_000} f(U_n), where f(U_n) is the perimeter of the maximum-area
quadrilateral formed by 4 distinct elements from the prefix U_n.
"""

from bisect import bisect_left, insort
from typing import List, Set, Tuple


def _generate_u_and_uniques(limit_n: int) -> Tuple[List[int], List[int]]:
    pow3 = [1] * 25
    for k in range(1, 25):
        pow3[k] = pow3[k - 1] * 3

    u = [0] * (limit_n + 1)
    uniq: Set[int] = set()
    for n in range(1, limit_n + 1):
        val = (
            (1 << ((3 * n).bit_count()))
            + pow3[n.bit_count()]
            + (n + 1).bit_count()
        )
        u[n] = val
        uniq.add(val)

    return u, sorted(uniq)


def solve(limit_n: int = 3_000_000) -> int:
    """Compute sum_{n=4..limit_n} f(U_n) using online local window maintenance."""
    u, uniq_vals = _generate_u_and_uniques(limit_n)
    idx_of = {v: i for i, v in enumerate(uniq_vals)}

    counts = [0] * len(uniq_vals)
    active: List[int] = []

    best_prod = -1
    best_per = 0
    total = 0

    for n in range(1, limit_n + 1):
        v = u[n]
        idx = idx_of[v]
        c_before = counts[idx]

        if c_before == 0:
            insort(active, idx)
        counts[idx] = c_before + 1

        pos = bisect_left(active, idx)

        left = []
        t = 3 if c_before >= 3 else c_before
        for _ in range(t):
            left.append(v)

        q = pos - 1
        while len(left) < 3 and q >= 0:
            idx2 = active[q]
            v2 = uniq_vals[idx2]
            take = min(counts[idx2], 3 - len(left))
            for _ in range(take):
                left.append(v2)
            q -= 1

        right = []
        q = pos + 1
        while len(right) < 3 and q < len(active):
            idx2 = active[q]
            v2 = uniq_vals[idx2]
            take = min(counts[idx2], 3 - len(right))
            for _ in range(take):
                right.append(v2)
            q += 1

        around = left[::-1]
        around.append(v)
        around.extend(right)

        p = len(around) - len(right) - 1

        for start in (p - 3, p - 2, p - 1, p):
            if start < 0 or start + 4 > len(around):
                continue
            a = around[start]
            b = around[start + 1]
            c = around[start + 2]
            d = around[start + 3]

            if d >= a + b + c:
                continue

            perim = a + b + c + d
            prod = (
                (perim - 2 * a)
                * (perim - 2 * b)
                * (perim - 2 * c)
                * (perim - 2 * d)
            )

            if prod > best_prod or (prod == best_prod and perim > best_per):
                best_prod = prod
                best_per = perim

        if n >= 4:
            total += best_per

    return total


if __name__ == "__main__":
    print(solve())
