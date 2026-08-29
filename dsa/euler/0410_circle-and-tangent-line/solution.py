"""Project Euler Problem 410: Circle and Tangent Line.

Find F(10^8, 10^9) + F(10^9, 10^8), where F(R, X) is the number of integer quadruplets (r, a, b, c)
such that the line through P(a, b) and Q(-a, c) is tangent to x^2 + y^2 = r^2 with 0 < r <= R, 0 < a <= X.
"""

from typing import Callable, List, Tuple


def _build_omega_odd(limit: int) -> bytearray:
    n_odd = limit // 2 + 1
    omega = bytearray(n_odd)
    om = omega
    lim = limit
    for p in range(3, lim + 1, 2):
        if om[p >> 1] == 0:
            step = p << 1
            for m in range(p, lim + 1, step):
                om[m >> 1] += 1
    return omega


def _build_block_prefix(
    limit: int, omega: bytearray, block_size: int
) -> Tuple[List[int], List[int]]:
    num_blocks = limit // block_size + 1
    even = [0] * (num_blocks + 1)
    odd = [0] * (num_blocks + 1)
    om = omega
    b_size = block_size
    even_arr = even
    odd_arr = odd

    for s in range(2, limit + 1, 2):
        oddpart = s // (s & -s)
        even_arr[s // b_size + 1] += 1 << om[oddpart >> 1]

    for s in range(3, limit + 1, 2):
        om_s = om[s >> 1]
        if om_s:
            odd_arr[s // b_size + 1] += 1 << (om_s - 1)

    for i in range(1, len(even_arr)):
        even_arr[i] += even_arr[i - 1]
        odd_arr[i] += odd_arr[i - 1]

    return even, odd


def _make_sum_funcs(
    omega: bytearray,
    even_prefix: List[int],
    odd_prefix: List[int],
    block_size: int,
) -> Tuple[Callable[[int, int], int], Callable[[int, int], int]]:
    b_size = block_size
    om = omega
    even_pref = even_prefix
    odd_pref = odd_prefix

    def sum_even_range(l_val: int, r_val: int) -> int:
        if l_val & 1:
            l_val += 1
        res = 0
        s = l_val
        while s <= r_val:
            oddpart = s // (s & -s)
            res += 1 << om[oddpart >> 1]
            s += 2
        return res

    def sum_odd_range(l_val: int, r_val: int) -> int:
        if l_val % 2 == 0:
            l_val += 1
        res = 0
        s = l_val
        while s <= r_val:
            om_s = om[s >> 1]
            if om_s:
                res += 1 << (om_s - 1)
            s += 2
        return res

    def sum_even(l_val: int, r_val: int) -> int:
        if l_val > r_val:
            return 0
        if l_val & 1:
            l_val += 1
        if l_val > r_val:
            return 0
        bl = l_val // b_size
        br = r_val // b_size
        if bl == br:
            return sum_even_range(l_val, r_val)
        res = even_pref[br] - even_pref[bl + 1]
        res += sum_even_range(l_val, (bl + 1) * b_size - 1)
        res += sum_even_range(br * b_size, r_val)
        return res

    def sum_odd(l_val: int, r_val: int) -> int:
        if l_val > r_val:
            return 0
        if l_val % 2 == 0:
            l_val += 1
        if l_val > r_val:
            return 0
        bl = l_val // b_size
        br = r_val // b_size
        if bl == br:
            return sum_odd_range(l_val, r_val)
        res = odd_pref[br] - odd_pref[bl + 1]
        res += sum_odd_range(l_val, (bl + 1) * b_size - 1)
        res += sum_odd_range(br * b_size, r_val)
        return res

    return sum_even, sum_odd


def _compute_f(
    r_limit: int,
    x_limit: int,
    sum_even: Callable[[int, int], int],
    sum_odd: Callable[[int, int], int],
) -> int:
    m_val = min(r_limit, x_limit)
    res = 0
    s = 1
    while s <= m_val:
        t_val = r_limit // s
        d_val = x_limit // s
        end = min(m_val, r_limit // t_val, x_limit // d_val)

        t_even = t_val // 2
        t_odd = (t_val + 1) // 2
        odd_count = (d_val + 1) // 2
        even_count = d_val // 2
        per_a = 4 * (odd_count * t_odd + even_count * t_even)
        per_b = 4 * t_val * d_val

        res += per_a * sum_even(s, end)
        res += per_b * sum_odd(s, end)
        s = end + 1

    res += 2 * r_limit * x_limit
    return res


def solve() -> int:
    """Compute F(10^8, 10^9) + F(10^9, 10^8) using blocked divisor character summation."""
    configs = [(10**8, 10**9), (10**9, 10**8)]
    limit = min(min(r, x) for r, x in configs)

    block_size = 1 << 10
    omega = _build_omega_odd(limit)
    even_prefix, odd_prefix = _build_block_prefix(limit, omega, block_size)
    sum_even, sum_odd = _make_sum_funcs(
        omega, even_prefix, odd_prefix, block_size
    )

    total = 0
    for r_bound, x_bound in configs:
        total += _compute_f(r_bound, x_bound, sum_even, sum_odd)

    return total


if __name__ == "__main__":
    print(solve())
