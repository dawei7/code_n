"""Project Euler Problem 617: Mirror Power Sequence.

Find D(10^18), where D(N) is the sum over n=2..N of the number of valid (n, e)-MPS sequences.
"""

from typing import List, Set


def _pow_capped(base: int, exp: int, cap: int) -> int:
    result = 1
    a = base
    e = exp
    while e:
        if e & 1:
            result *= a
            if result > cap:
                return cap + 1
        e >>= 1
        if e:
            a *= a
            if a > cap:
                a = cap + 1
    return result


def _int_nth_root(n: int, k: int) -> int:
    if k <= 1:
        return n
    if n < 2:
        return n
    lo, hi = 1, 1
    while _pow_capped(hi, k, n) <= n:
        hi <<= 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if _pow_capped(mid, k, n) <= n:
            lo = mid
        else:
            hi = mid
    return lo


def _max_t_for_b1(n_limit: int, e: int) -> int:
    if n_limit < 4:
        return 1
    hi = _int_nth_root(n_limit, e) + 1
    lo = 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid + pow(mid, e) <= n_limit:
            lo = mid
        else:
            hi = mid
    return lo


def _count_for_exponent(n_limit: int, e: int) -> int:
    total = 0
    t_max = _max_t_for_b1(n_limit, e)
    total += t_max - _int_nth_root(t_max, e)

    if n_limit <= 4:
        return total

    max_exp_for_2 = (n_limit - 2).bit_length() - 1
    possible_bs: List[int] = []
    b = 2
    while True:
        exp = e**b
        if exp > max_exp_for_2:
            break
        if 2 + (1 << exp) > n_limit:
            break
        possible_bs.append(b)
        b += 1

    if not possible_bs:
        return total

    max_t_limit = 0
    for b_val in possible_bs:
        exp = e**b_val
        max_t_limit = max(max_t_limit, _int_nth_root(n_limit - 2, exp))

    u_max = _int_nth_root(max_t_limit, e)
    non_primitive: Set[int] = {pow(u, e) for u in range(2, u_max + 1)}

    for b_val in possible_bs:
        exp = e**b_val
        t_limit = _int_nth_root(n_limit - 2, exp)
        for t in range(2, t_limit + 1):
            if t in non_primitive:
                continue

            p = [t]
            x = t
            for _ in range(b_val):
                x = pow(x, e)
                p.append(x)
            top = p[b_val]

            cnt_a = 0
            for a in range(b_val):
                if p[a] + top <= n_limit:
                    cnt_a += 1
                else:
                    break
            total += b_val * cnt_a

    return total


def solve(n_limit: int = 10**18) -> int:
    """Compute D(N) = sum_{n=2}^N C(n) across all valid exponents e >= 2."""
    total = 0
    e = 2
    while (1 << e) + 2 <= n_limit:
        total += _count_for_exponent(n_limit, e)
        e += 1
    return total


if __name__ == "__main__":
    print(solve())
