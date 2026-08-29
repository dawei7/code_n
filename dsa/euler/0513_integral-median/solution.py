"""Project Euler Problem 513: Integral Median.

Find F(100000), where F(n) is the number of integral-sided triangles with sides
a <= b <= c <= n such that the median m_C has integral length as well.
"""

from math import isqrt
from typing import Dict

_cache: Dict[int, int] = {}


def _trapezoid_floor_sum(
    slope: int,
    intercept: int,
    denominator: int,
    lower_x: int,
    upper_x: int,
    include_boundary: bool,
) -> int:
    total = 0
    while True:
        if abs(upper_x - lower_x) <= 8:
            adjustment = 0 if include_boundary else 1
            if upper_x > lower_x:
                for x in range(lower_x + 1, upper_x + 1):
                    total += (
                        slope * x + intercept - adjustment
                    ) // denominator
            else:
                subtotal = 0
                for x in range(upper_x + 1, lower_x + 1):
                    subtotal += (
                        slope * x + intercept - adjustment
                    ) // denominator
                total -= subtotal
            return total

        whole_intercept = intercept // denominator
        if whole_intercept:
            total += (upper_x - lower_x) * whole_intercept
            intercept %= denominator

        whole_slope = slope // denominator
        if whole_slope:
            total += (
                (upper_x - lower_x)
                * (upper_x + lower_x + 1)
                // 2
                * whole_slope
            )
            slope %= denominator

        if slope == 0:
            if intercept == 0 and not include_boundary:
                total -= upper_x - lower_x
            return total

        upper_y = (slope * upper_x + intercept) // denominator
        lower_y = (slope * lower_x + intercept) // denominator
        total += upper_x * upper_y - lower_x * lower_y

        lower_x, upper_x = upper_y, lower_y
        slope, denominator = denominator, slope
        intercept = -intercept
        include_boundary = not include_boundary


def _trapezoid_floor_sum_mod2(
    slope: int,
    intercept: int,
    denominator: int,
    lower_x: int,
    upper_x: int,
    include_boundary: bool,
    x_residue: int,
    y_residue: int,
) -> int:
    if y_residue & 1:
        intercept += denominator
    if x_residue & 1:
        intercept -= slope
        lower_x += 1
        upper_x += 1

    return _trapezoid_floor_sum(
        2 * slope,
        intercept,
        2 * denominator,
        lower_x // 2,
        upper_x // 2,
        include_boundary,
    )


def _primitive_count(n: int) -> int:
    total = 0
    three_halves_n = n + n // 2
    root = isqrt(three_halves_n)
    parity_cases = ((0, 1), (1, 0), (1, 1))

    for i_residue, j_residue in parity_cases:
        max_t = 1

        for s in range(2, root):
            if 3 * (max_t + 1) * (max_t + 1) <= s * s:
                max_t += 1

            if i_residue == j_residue or (s & 1) == 0:
                start_t = ((s - 1) & 1) + 1
                for t in range(start_t, max_t + 1, 2):
                    v_mid = t * n // ((s - t) * (s + t))
                    v_max = n * (s + t) // (s * s + 2 * s * t - t * t)

                    total += _trapezoid_floor_sum_mod2(
                        s, 0, t, 0, v_mid, True, j_residue, i_residue
                    )
                    total += _trapezoid_floor_sum_mod2(
                        t, n, s, v_mid, v_max, True, j_residue, i_residue
                    )
                    total -= _trapezoid_floor_sum_mod2(
                        s + 3 * t,
                        0,
                        s + t,
                        0,
                        v_max,
                        False,
                        j_residue,
                        i_residue,
                    )

        max_u = three_halves_n // root
        start_u = 1 + ((i_residue + 1) & 1)
        for u in range(start_u, max_u + 1, 2):
            max_v_outer = min(n // 2, u - 1)
            start_v = 1 + ((j_residue + 1) & 1)

            for v in range(start_v, max_v_outer + 1, 2):
                split_s = (v + n) // u
                residue_count = 2 if i_residue == j_residue else 1

                for s_residue in range(residue_count):
                    if i_residue != j_residue:
                        s_residue = 0

                    if u * u < 3 * v * v:
                        min_s = root
                        max_s = (
                            n
                            * (3 * v - u)
                            // (2 * u * v + v * v - u * u)
                        )
                        slope0 = u - v
                        slope1 = 3 * v - u
                    else:
                        min_s = max(root, (u + v - 1) // v)
                        max_s = n * u // ((u - v) * (u + v))
                        slope0 = v
                        slope1 = u

                    if max_s < min_s:
                        continue

                    total += _trapezoid_floor_sum_mod2(
                        slope0,
                        0,
                        slope1,
                        min_s - 1,
                        max_s,
                        True,
                        s_residue,
                        s_residue,
                    )
                    if split_s < max_s:
                        total -= _trapezoid_floor_sum_mod2(
                            u,
                            -n,
                            v,
                            max(split_s, min_s - 1),
                            max_s,
                            False,
                            s_residue,
                            s_residue,
                        )

    return total


def solve(n: int = 100_000) -> int:
    """Compute F(n) using primitive parameter floor-sum queries and odd scaling Möbius inversion."""
    if n <= 0:
        return 0
    cached = _cache.get(n)
    if cached is not None:
        return cached

    result = _primitive_count(n)

    k = 3
    quotient = n // k
    while k <= quotient:
        result -= solve(quotient)
        k += 2
        quotient = n // k

    min_k = n // (quotient + 1) if quotient + 1 > 0 else n
    while quotient > 0:
        max_k = n // quotient
        left = (min_k + 1) + (min_k & 1)
        right = max_k - ((max_k + 1) & 1)
        if right >= left:
            result -= solve(quotient) * ((right - left) // 2 + 1)
        quotient -= 1
        min_k = max_k

    _cache[n] = result
    return result


if __name__ == "__main__":
    print(solve())
