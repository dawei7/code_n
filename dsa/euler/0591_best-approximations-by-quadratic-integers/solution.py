"""Project Euler Problem 591: Best Approximations by Quadratic Integers.

Find the sum of |I_d(BQA_d(pi, 10^13))| for all non-square d < 100,
where BQA_d(x, n) is the quadratic integer a + b*sqrt(d) with |a|, |b| <= n
closest to x.
"""

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, getcontext
from math import isqrt
from typing import List, Tuple


def _frac_dec(x: Decimal) -> Decimal:
    return x - x.to_integral_value(rounding=ROUND_FLOOR)


def _ceil_int_dec(x: Decimal) -> int:
    return int(x.to_integral_value(rounding=ROUND_CEILING))


def _nearest_int_dec(x: Decimal) -> int:
    return int(x.to_integral_value(rounding=ROUND_HALF_EVEN))


def _chudnovsky_pi(digits: int) -> Decimal:
    getcontext().prec = digits + 30
    c_const = Decimal(426880) * Decimal(10005).sqrt()
    n_terms = digits // 14 + 3

    m_val = 1
    l_val = 13591409
    x_val = 1
    k_val = 6
    s_val = Decimal(l_val)

    for i in range(1, n_terms):
        m_val = (m_val * (k_val * k_val * k_val - 16 * k_val)) // (i * i * i)
        l_val += 545140134
        x_val *= -262537412640768000
        s_val += Decimal(m_val * l_val) / Decimal(x_val)
        k_val += 12

    pi_val = c_const / s_val
    getcontext().prec = digits
    return +pi_val


def _is_square(n: int) -> bool:
    r = isqrt(n)
    return r * r == n


def _sqrt_cf_period(d_val: int) -> Tuple[int, List[int]]:
    a0 = isqrt(d_val)
    if a0 * a0 == d_val:
        raise ValueError("d_val is a perfect square")

    m = 0
    d = 1
    a = a0
    period: List[int] = []
    while True:
        m = d * a - m
        d = (d_val - m * m) // d
        a = (a0 + m) // d
        period.append(a)
        if a == 2 * a0:
            break
    return a0, period


def _best_b_positive(
    alpha: Decimal, beta: Decimal, b_bound: int, period: List[int]
) -> int:
    if b_bound <= 0:
        return 0

    a_cf: List[int] = [0]
    q_arr: List[int] = [1]
    q_minus1 = 0

    delta: List[Decimal] = [alpha]
    delta_minus1 = Decimal(1)

    k = 1
    extra = 6
    while True:
        ak = period[(k - 1) % len(period)]
        a_cf.append(ak)

        qk = ak * q_arr[k - 1] + q_minus1
        q_minus1 = q_arr[k - 1]
        q_arr.append(qk)

        if k == 1:
            delta_k = -Decimal(ak) * delta[0] + delta_minus1
        else:
            delta_k = -Decimal(ak) * delta[k - 1] + delta[k - 2]
        delta.append(delta_k)

        if qk > b_bound:
            extra -= 1
            if extra <= 0:
                break

        k += 1
        if k > 500:
            break

    max_i = len(a_cf) - 1
    b_digits: List[int] = [0]
    beta_rem = beta
    for i in range(1, max_i + 1):
        ratio = beta_rem / delta[i - 1]
        bi = _ceil_int_dec(ratio)
        if bi > a_cf[i]:
            bi = a_cf[i]
        if bi < 0:
            bi = 0
        b_digits.append(bi)
        beta_rem = Decimal(bi) * delta[i - 1] - beta_rem

    prefix: List[int] = [0]
    s_cum = 0
    for i in range(1, len(b_digits)):
        s_cum += b_digits[i] * q_arr[i - 1]
        prefix.append(s_cum)

    candidates_right = {0}
    for k2 in range(1, (len(b_digits) - 1) // 2 + 1):
        idx_even = 2 * k2
        idx_odd = 2 * k2 - 1
        if idx_even >= len(b_digits):
            break
        p_val = prefix[idx_odd]
        step = q_arr[idx_odd]
        for j in range(b_digits[idx_even]):
            n_cand = p_val + j * step
            if 0 <= n_cand <= b_bound:
                candidates_right.add(n_cand)

    candidates_left = {0}
    for k2 in range(0, (len(b_digits) - 2) // 2 + 1):
        idx = 2 * k2
        idx_next = idx + 1
        if idx_next >= len(b_digits):
            break
        p_val = prefix[idx]
        step = q_arr[idx]
        for j in range(b_digits[idx_next]):
            n_cand = p_val + j * step
            if 0 <= n_cand <= b_bound:
                candidates_left.add(n_cand)

    best_r_n = 0
    best_r_gap = Decimal(1)
    for n_cand in candidates_right:
        x_val = _frac_dec(alpha * Decimal(n_cand))
        gap = x_val - beta
        if gap < 0:
            gap += 1
        if gap < best_r_gap:
            best_r_gap = gap
            best_r_n = n_cand

    best_l_n = 0
    best_l_gap = Decimal(1)
    for n_cand in candidates_left:
        x_val = _frac_dec(alpha * Decimal(n_cand))
        gap = beta - x_val
        if gap < 0:
            gap += 1
        if gap < best_l_gap:
            best_l_gap = gap
            best_l_n = n_cand

    return best_r_n if best_r_gap < best_l_gap else best_l_n


def _bqa_pi_d(
    d_val: int, n: int, pi_val: Decimal, beta_pi: Decimal
) -> Tuple[int, int]:
    sqrt_d = Decimal(d_val).sqrt()
    a0, period = _sqrt_cf_period(d_val)
    alpha = sqrt_d - Decimal(a0)

    b_pos_bound = int(
        ((Decimal(n) + pi_val) / sqrt_d).to_integral_value(rounding=ROUND_FLOOR)
    )
    b_pos_bound = min(max(b_pos_bound, 0), n)

    b_neg_bound = int(
        ((Decimal(n) - pi_val) / sqrt_d).to_integral_value(rounding=ROUND_FLOOR)
    )
    b_neg_bound = min(max(b_neg_bound, 0), n)

    b_pos = _best_b_positive(alpha, beta_pi, b_pos_bound, period)
    t_val = _best_b_positive(alpha, Decimal(1) - beta_pi, b_neg_bound, period)
    b_neg = -t_val

    def candidate_ab(b: int) -> Tuple[int, int, Decimal]:
        a_real = pi_val - Decimal(b) * sqrt_d
        a = _nearest_int_dec(a_real)
        if a > n:
            a = n
        elif a < -n:
            a = -n
        err = abs(Decimal(a) + Decimal(b) * sqrt_d - pi_val)
        return a, b, err

    a1, b1, e1 = candidate_ab(b_pos)
    a2, b2, e2 = candidate_ab(b_neg)
    return (a2, b2) if e2 < e1 else (a1, b1)


def solve(n: int = 10**13) -> int:
    """Sum |I_d(BQA_d(pi, n))| for all non-square d < 100 using Ostrowski alpha-numeration."""
    getcontext().prec = 140
    pi_val = _chudnovsky_pi(130)
    beta_pi = _frac_dec(pi_val)

    total = 0
    for d in range(2, 100):
        if _is_square(d):
            continue
        a, _ = _bqa_pi_d(d, n, pi_val, beta_pi)
        total += abs(a)
    return total


if __name__ == "__main__":
    print(solve())
