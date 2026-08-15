"""Project Euler 322: Binomial Coefficients Divisible by 10

Find T(10^18, 10^12 - 10), where T(m, n) is the number of binomial coefficients
binom{i}{n} that are divisible by 10 for n <= i < m.
"""

from __future__ import annotations


def solve(m_exp: int = 18, n_exp: int = 12) -> str:
    """Calculates T(10^m_exp, 10^n_exp - 10) using Lucas' Theorem, Principle of Inclusion-Exclusion (PIE):

    T(m, n) = (m - n) - (C2 + C5 - C_both), base-2 digit DP for C2, base-5 prefix expansion for C5,
    and modular residue filtering for C_both.
    """
    m = 10**m_exp
    n = 10**n_exp - 10

    # 1. Compute C2: count i in [n, m - 1] with (i & n) == n via base-2 Digit DP
    m_bits: list[int] = []
    temp_m = m
    while temp_m > 0:
        m_bits.append(temp_m % 2)
        temp_m //= 2
    num_bits = len(m_bits)

    memo: dict[tuple[int, bool], int] = {}

    def digit_dp(idx: int, is_less: bool) -> int:
        if idx == -1:
            return 1 if is_less else 0
        state = (idx, is_less)
        if state in memo:
            return memo[state]

        n_bit = (n >> idx) & 1
        m_bit = m_bits[idx]
        total = 0
        allowed_bits = [1] if n_bit == 1 else [0, 1]

        for b in allowed_bits:
            if not is_less and b > m_bit:
                continue
            total += digit_dp(idx - 1, is_less or (b < m_bit))

        memo[state] = total
        return total

    c2 = digit_dp(num_bits - 1, False)

    # 2. Compute C5: count i in [n, m - 1] with i_k >= n_k in base 5 via prefix recursion
    n5: list[int] = []
    temp_n = n
    while temp_n > 0:
        n5.append(temp_n % 5)
        temp_n //= 5

    c5 = 0
    cur_p = 5 ** len(n5)

    def search5(idx: int, cur_val: int, cur_pow: int) -> None:
        nonlocal c5
        if idx == len(n5):
            if cur_val < m:
                c5 += (m - 1 - cur_val) // cur_pow + 1
            return
        for d in range(n5[idx], 5):
            search5(idx + 1, cur_val + d * cur_pow, cur_pow * 5)

    search5(0, 0, 1)

    # 3. Compute C_both: count i with (i & n) == n AND (i_k >= n_k in base 5)
    # Filter candidates using lower-order binary residues
    ell = n_exp
    mod_low = 1 << ell
    n_low = n % mod_low
    a = 5 ** len(n5)
    a_low = a % mod_low
    inv_a_low = pow(a_low, -1, mod_low)
    valid_x = [x for x in range(mod_low) if (x & n_low) == n_low]

    prefixes: list[int] = []

    def gen_p(idx: int, cur_val: int, cur_pow: int) -> None:
        if idx == len(n5):
            prefixes.append(cur_val)
            return
        for d in range(n5[idx], 5):
            gen_p(idx + 1, cur_val + d * cur_pow, cur_pow * 5)

    gen_p(0, 0, 1)

    c_both = 0
    for v in prefixes:
        max_k = (m - 1 - v) // a
        if max_k < 0:
            continue
        v_low = v % mod_low
        for x in valid_x:
            k_rem = ((x - v_low) * inv_a_low) % mod_low
            k = k_rem
            while k <= max_k:
                if (k * a + v) & n == n:
                    c_both += 1
                k += mod_low

    non_div = c2 + c5 - c_both
    ans = (m - n) - non_div

    return str(ans)


if __name__ == "__main__":
    print(solve())
