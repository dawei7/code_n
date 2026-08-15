"""Project Euler Problem 564: Maximal Polygons.

Find S(50) rounded to 6 decimal places, where S(k) = sum_{n=3..k} E(n),
and E(n) is the expected maximal area of a convex n-polygon formed from an
integer split of length 2n-3 into n segments.
"""

import math
from typing import List, Tuple


def _build_factorials(n: int) -> List[int]:
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i
    return fact


def _comb(n: int, k: int, fact: List[int]) -> int:
    if k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    return fact[n] // (fact[k] * fact[n - k])


def _maximal_area(groups: List[Tuple[int, int]]) -> float:
    asin = math.asin
    sqrt = math.sqrt
    pi = math.pi

    max_l = 0
    sum_len = 0.0
    for length, cnt in groups:
        if length > max_l:
            max_l = length
        sum_len += length * cnt

    inv0 = 1.0 / max_l
    sum_asin_at_min = 0.0
    for length, cnt in groups:
        u = length * inv0
        if u > 1.0:
            u = 1.0
        sum_asin_at_min += cnt * asin(u)

    all_minor = sum_asin_at_min >= pi - 1e-15

    if all_minor:
        f_at_lo = sum_asin_at_min - pi
        if abs(f_at_lo) < 1e-15:
            r = float(max_l)
        else:
            lo = max_l * (1.0 + 1e-15)
            hi = lo * 2.0

            def eval_f_df(r_val: float) -> Tuple[float, float]:
                inv = 1.0 / r_val
                r2 = r_val * r_val
                f_val = -pi
                df_val = 0.0
                for l_val, c_val in groups:
                    u_val = l_val * inv
                    t_val = max(0.0, 1.0 - u_val * u_val)
                    s_val = max(1e-18, sqrt(t_val))
                    f_val += c_val * asin(u_val)
                    df_val -= c_val * l_val / (r2 * s_val)
                return f_val, df_val

            f_hi, _ = eval_f_df(hi)
            while f_hi > 0.0:
                hi *= 2.0
                f_hi, _ = eval_f_df(hi)

            r = sum_len / pi
            if r <= lo or r >= hi:
                r = 0.5 * (lo + hi)

            for _ in range(24):
                f_val, df_val = eval_f_df(r)
                if abs(f_val) < 1e-15:
                    break
                if f_val > 0.0:
                    lo = r
                else:
                    hi = r
                rn = r - f_val / df_val
                if rn <= lo or rn >= hi or not math.isfinite(rn):
                    rn = 0.5 * (lo + hi)
                r = rn
                if hi - lo < 1e-14 * hi:
                    break

        inv = 1.0 / r
        area_sum = 0.0
        for l_val, c_val in groups:
            u_val = l_val * inv
            t_val = 1.0 - u_val * u_val
            if t_val <= 0.0:
                continue
            area_sum += c_val * l_val * (r * sqrt(t_val))
        return 0.25 * area_sum

    big_l = max_l
    lo = big_l * (1.0 + 1e-15)
    hi = lo * 2.0

    def eval_f_df_major(r_val: float) -> Tuple[float, float]:
        inv = 1.0 / r_val
        r2 = r_val * r_val
        f_val = 0.0
        df_val = 0.0
        for l_val, c_val in groups:
            u_val = l_val * inv
            t_val = max(0.0, 1.0 - u_val * u_val)
            s_val = max(1e-18, sqrt(t_val))
            f_val += c_val * asin(u_val)
            df_val -= c_val * l_val / (r2 * s_val)
        u_l = big_l * inv
        t_l = max(0.0, 1.0 - u_l * u_l)
        s_l = max(1e-18, sqrt(t_l))
        f_val -= 2.0 * asin(u_l)
        df_val += 2.0 * big_l / (r2 * s_l)
        return f_val, df_val

    f_hi, _ = eval_f_df_major(hi)
    while f_hi < 0.0:
        hi *= 2.0
        f_hi, _ = eval_f_df_major(hi)

    r = lo * 1.1
    if r >= hi:
        r = 0.5 * (lo + hi)

    for _ in range(24):
        f_val, df_val = eval_f_df_major(r)
        if abs(f_val) < 1e-15:
            break
        if f_val > 0.0:
            hi = r
        else:
            lo = r
        rn = r - f_val / df_val
        if rn <= lo or rn >= hi or not math.isfinite(rn):
            rn = 0.5 * (lo + hi)
        r = rn
        if hi - lo < 1e-14 * hi:
            break

    inv = 1.0 / r
    area_sum = 0.0
    max_term = 0.0
    for l_val, c_val in groups:
        u_val = l_val * inv
        t_val = 1.0 - u_val * u_val
        if t_val <= 0.0:
            continue
        term = c_val * l_val * (r * sqrt(t_val))
        area_sum += term
        if l_val == big_l:
            max_term = l_val * (r * sqrt(t_val))
    area_sum -= 2.0 * max_term
    return 0.25 * area_sum


def _expected_area(n: int, fact: List[int]) -> float:
    k = n - 3
    total = _comb(2 * n - 4, n - 1, fact)
    total_inv = 1.0 / total
    fact_n = fact[n]

    parts: List[int] = []
    s = 0.0
    c = 0.0

    def dfs(rem: int, max_p: int) -> None:
        nonlocal s, c
        if rem == 0:
            t = len(parts)
            m0 = n - t
            denom = fact[m0]

            groups: List[Tuple[int, int]] = [(1, m0)]
            i = 0
            while i < t:
                v = parts[i]
                j = i + 1
                while j < t and parts[j] == v:
                    j += 1
                cnt = j - i
                groups.append((v + 1, cnt))
                denom *= fact[cnt]
                i = j

            weight = fact_n // denom
            area = _maximal_area(groups)
            contrib = area * (weight * total_inv)

            y = contrib - c
            tt = s + y
            c = (tt - s) - y
            s = tt
            return

        for p in range(min(rem, max_p), 0, -1):
            parts.append(p)
            dfs(rem - p, p)
            parts.pop()

    dfs(k, k)
    return s


def solve(limit: int = 50) -> str:
    """Compute S(limit) rounded to 6 decimal places."""
    fact = _build_factorials(2 * limit + 10)
    total_sum = 0.0

    for n in range(3, limit + 1):
        e_val = _expected_area(n, fact)
        total_sum += e_val

    return f"{total_sum:.6f}"


if __name__ == "__main__":
    print(solve())
