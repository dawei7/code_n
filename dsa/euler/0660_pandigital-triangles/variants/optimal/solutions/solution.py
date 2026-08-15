"""Project Euler Problem 660: Pandigital Triangles.

Find the sum of the largest sides of all n-pandigital triangles with 120-degree angles
for 9 <= n <= 18.
"""

from math import gcd, isqrt
from typing import Dict, List, Tuple


def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def _modinv(a: int, m: int) -> int:
    g, x, _ = _egcd(a, m)
    return x % m


def _ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def _precompute_tables(
    base: int,
) -> Tuple[List[int], List[int], List[int], List[int], int, int]:
    t1 = [1 << d for d in range(base)]
    b2 = base * base
    b3 = b2 * base

    t2 = [-1] * (base * base)
    for v in range(base, base * base):
        d0 = v // base
        d1 = v - d0 * base
        if d0 != d1:
            t2[v] = (1 << d0) | (1 << d1)

    t3 = [-1] * b3
    for v in range(b2, b3):
        d0 = v // b2
        r = v - d0 * b2
        d1 = r // base
        d2 = r - d1 * base
        if d0 != d1 and d0 != d2 and d1 != d2:
            t3[v] = (1 << d0) | (1 << d1) | (1 << d2)

    t3z = [-1] * b3
    for v in range(b3):
        d0 = v // b2
        r = v - d0 * b2
        d1 = r // base
        d2 = r - d1 * base
        if d0 != d1 and d0 != d2 and d1 != d2:
            t3z[v] = (1 << d0) | (1 << d1) | (1 << d2)

    return t1, t2, t3, t3z, b2, b3


def _mask_fixed_len(x: int, length: int, _base: int, table_tuple) -> int:
    t1, t2, t3, t3z, _b2, b3 = table_tuple
    if length == 1:
        return t1[x]
    if length == 2:
        return t2[x]
    if length == 3:
        return t3[x]
    if length == 4:
        hi, lo = divmod(x, b3)
        m_hi = t1[hi]
        m_lo = t3z[lo]
        if m_lo == -1 or (m_hi & m_lo):
            return -1
        return m_hi | m_lo
    if length == 5:
        hi, lo = divmod(x, b3)
        m_hi = t2[hi]
        if m_hi == -1:
            return -1
        m_lo = t3z[lo]
        if m_lo == -1 or (m_hi & m_lo):
            return -1
        return m_hi | m_lo
    if length == 6:
        hi, lo = divmod(x, b3)
        m_hi = t3[hi]
        if m_hi == -1:
            return -1
        m_lo = t3z[lo]
        if m_lo == -1 or (m_hi & m_lo):
            return -1
        return m_hi | m_lo
    return -1


def solve(min_base: int = 9, max_base: int = 18) -> int:
    """Compute the sum of largest sides of all n-pandigital triangles for min_base <= n <= max_base."""
    max_d_per_side: Dict[int, int] = {}
    limit: Dict[int, int] = {}
    powb: Dict[int, List[int]] = {}
    combos: Dict[int, List[Tuple[int, int, int]]] = {}
    full_mask: Dict[int, int] = {}
    mod_m: Dict[int, int] = {}
    target: Dict[int, int] = {}
    tables = {}

    for b in range(9, 19):
        if b in (9, 10, 11):
            d_val = 4
        elif b in (12, 13, 14):
            d_val = 5
        elif b in (15, 16, 17, 18):
            d_val = 6
        else:
            d_val = 6
        max_d_per_side[b] = d_val
        pow_list = [1] * (d_val + 1)
        for i in range(1, d_val + 1):
            pow_list[i] = pow_list[i - 1] * b
        powb[b] = pow_list
        limit[b] = pow_list[d_val] - 1

        cs = []
        for da in range(1, d_val + 1):
            for db in range(1, d_val + 1):
                dc = b - da - db
                if 1 <= dc <= d_val:
                    cs.append((da, db, dc))
        combos[b] = cs
        full_mask[b] = (1 << b) - 1
        mod_m[b] = b - 1
        target[b] = 0 if (b % 2 == 0) else (b - 1) // 2
        tables[b] = _precompute_tables(b)

    t1_18, t2_18, t3_18, t3z_18, _b2_18, b3_18 = tables[18]
    full18 = full_mask[18]
    pow18 = powb[18]
    m18 = mod_m[18]

    sums = [0] * 19
    max_a = limit[max_base]
    max_m = isqrt(max_a) + 2

    for m in range(2, max_m):
        disc = 4 * max_a - 3 * m * m
        if disc <= 0:
            continue
        nmax = (-m + isqrt(disc)) // 2
        if nmax >= m:
            nmax = m - 1

        mm = m * m
        for n in range(1, nmax + 1):
            if (m - n) % 3 == 0:
                continue
            if gcd(m, n) != 1:
                continue

            a = mm + m * n + n * n
            if a > max_a:
                break
            b = 2 * m * n + n * n
            c = mm - n * n

            if a <= limit[15]:
                start_base = min_base
            elif a <= limit[16]:
                start_base = max(16, min_base)
            elif a <= limit[17]:
                start_base = max(17, min_base)
            else:
                start_base = 18

            # Fast path for base 18 (6+6+6 digits)
            if max_base >= 18:
                s18 = (a + b + c) % m18
                step18 = 1 if s18 == 0 else 17

                left = _ceil_div(pow18[5], a)
                right = (pow18[6] - 1) // a
                left2 = _ceil_div(pow18[5], b)
                right2 = (pow18[6] - 1) // b
                if left2 > left:
                    left = left2
                if right2 < right:
                    right = right2
                if left <= right:
                    left3 = _ceil_div(pow18[5], c)
                    right3 = (pow18[6] - 1) // c
                    if left3 > left:
                        left = left3
                    if right3 < right:
                        right = right3
                    if left <= right:
                        if left < 1:
                            left = 1
                        if step18 == 1:
                            k = left
                            big_a = a * k
                            big_b = b * k
                            big_c = c * k
                            inc_a, inc_b, inc_c = a, b, c
                        else:
                            k = ((left + 16) // 17) * 17
                            big_a = a * k
                            big_b = b * k
                            big_c = c * k
                            inc_a, inc_b, inc_c = a * 17, b * 17, c * 17

                        while k <= right:
                            hi, lo = divmod(big_a, b3_18)
                            ma = t3_18[hi]
                            if ma != -1:
                                ml = t3z_18[lo]
                                if ml != -1 and (ma & ml) == 0:
                                    ma |= ml
                                    hi, lo = divmod(big_b, b3_18)
                                    mb = t3_18[hi]
                                    if mb != -1:
                                        ml = t3z_18[lo]
                                        if ml != -1 and (mb & ml) == 0:
                                            mb |= ml
                                            if (ma & mb) == 0:
                                                hi, lo = divmod(big_c, b3_18)
                                                mc = t3_18[hi]
                                                if mc != -1:
                                                    ml = t3z_18[lo]
                                                    if ml != -1 and (
                                                        mc & ml
                                                    ) == 0:
                                                        mc |= ml
                                                        if (
                                                            (ma & mc) == 0
                                                            and (mb & mc) == 0
                                                            and (
                                                                ma | mb | mc
                                                            )
                                                            == full18
                                                        ):
                                                            sums[18] += big_a
                            k += step18
                            big_a += inc_a
                            big_b += inc_b
                            big_c += inc_c

            # Other bases (min_base..min(max_base, 17))
            for base in range(start_base, min(max_base + 1, 18)):
                if a > limit[base]:
                    continue

                p = powb[base]
                cs = combos[base]
                t = tables[base]
                fm = full_mask[base]
                m_val = mod_m[base]
                targ = target[base]

                s = (a + b + c) % m_val

                if base % 2 == 0:
                    if s == 0:
                        step = 1
                        residue = 0
                    else:
                        g = gcd(s, m_val)
                        step = m_val // g
                        residue = 0
                else:
                    if s == 0:
                        if targ != 0:
                            continue
                        step = 1
                        residue = 0
                    else:
                        g = gcd(s, m_val)
                        if targ % g:
                            continue
                        step = m_val // g
                        inv = _modinv((s // g) % step, step)
                        residue = ((targ // g) * inv) % step

                for da, db, dc in cs:
                    left = _ceil_div(p[da - 1], a)
                    right = (p[da] - 1) // a
                    if left > right:
                        continue
                    left2 = _ceil_div(p[db - 1], b)
                    right2 = (p[db] - 1) // b
                    if left2 > right2:
                        continue
                    if left2 > left:
                        left = left2
                    if right2 < right:
                        right = right2
                    if left > right:
                        continue
                    left3 = _ceil_div(p[dc - 1], c)
                    right3 = (p[dc] - 1) // c
                    if left3 > right3:
                        continue
                    if left3 > left:
                        left = left3
                    if right3 < right:
                        right = right3
                    if left > right:
                        continue
                    if left < 1:
                        left = 1

                    if step == 1:
                        k = left
                    else:
                        rem = left % step
                        if rem <= residue:
                            k = left + (residue - rem)
                        else:
                            k = left + (step - (rem - residue))

                    big_a = a * k
                    big_b = b * k
                    big_c = c * k
                    inc_a, inc_b, inc_c = a * step, b * step, c * step

                    while k <= right:
                        ma = _mask_fixed_len(big_a, da, base, t)
                        if ma != -1:
                            mb = _mask_fixed_len(big_b, db, base, t)
                            if mb != -1 and (ma & mb) == 0:
                                mc = _mask_fixed_len(big_c, dc, base, t)
                                if (
                                    mc != -1
                                    and (ma & mc) == 0
                                    and (mb & mc) == 0
                                    and (ma | mb | mc) == fm
                                ):
                                    sums[base] += big_a
                        k += step
                        big_a += inc_a
                        big_b += inc_b
                        big_c += inc_c

    return sum(sums[b] for b in range(min_base, max_base + 1))


if __name__ == "__main__":
    print(solve())
