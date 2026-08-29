"""Project Euler 269: Polynomials with at Least One Integer Root

Find Z(10^16), the number of positive integers n <= 10^16 for which
the polynomial P_n(x) whose coefficients are the digits of n has at least one integer root.
"""

from __future__ import annotations

import itertools
import math


def solve(max_len: int = 16) -> str:
    """Calculates Z(10^max_len) using the Principle of Inclusion-Exclusion over all valid

    root subsets in {-1, ..., -9} combined with dynamic programming over digit prefixes.
    """
    # Find all subsets S of {1, ..., 9} whose LCM divides at least one non-zero decimal digit
    valid_subsets: list[tuple[tuple[int, ...], int]] = []
    for r in range(1, 10):
        for s in itertools.combinations(range(1, 10), r):
            l = 1
            for x in s:
                l = (l * x) // math.gcd(l, x)
            if any(d % l == 0 for d in range(1, 10)):
                valid_subsets.append((s, l))

    total_pie = 0

    # DP over prefix polynomial evaluations for each subset S
    for s, l in valid_subsets:
        sign = (-1) ** (len(s) - 1)
        count_s = 0

        # Maximum possible value bounds for intermediate polynomial values
        bounds: dict[int, int] = {}
        for k in s:
            bounds[k] = 9 // (k - 1) + 2 if k > 1 else 100

        # Initialize DP with the leading non-zero digit
        dp: dict[tuple[int, ...], int] = {}
        for d in range(1, 10):
            st = tuple(d for _ in s)
            dp[st] = dp.get(st, 0) + 1

        for length in range(2, max_len + 1):
            # Check terminal states (transition to final digit a_0 != 0)
            for a0 in range(1, 10):
                if a0 % l == 0:
                    req_st = tuple(a0 // k for k in s)
                    if req_st in dp:
                        count_s += dp[req_st]

            # Intermediate digit transitions
            if length < max_len:
                next_dp: dict[tuple[int, ...], int] = {}
                for st, count in dp.items():
                    for d in range(10):
                        valid = True
                        new_st_list = []
                        for k, val in zip(s, st):
                            nv = -k * val + d
                            if abs(nv) > bounds[k]:
                                valid = False
                                break
                            new_st_list.append(nv)
                        if valid:
                            new_st = tuple(new_st_list)
                            next_dp[new_st] = next_dp.get(new_st, 0) + count
                dp = next_dp

        total_pie += sign * count_s

    # Add all numbers <= 10^max_len ending in 0 (root r = 0)
    ends_in_zero = 10 ** (max_len - 1)
    ans = total_pie + ends_in_zero

    return str(ans)


if __name__ == "__main__":
    print(solve())
