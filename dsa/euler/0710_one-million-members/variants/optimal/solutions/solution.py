"""Project Euler Problem 710: One Million Members.

Find the least value of n > 42 such that t(n) is divisible by one million, where t(n) is the number
of palindromic compositions (twopals) of n containing at least one 2.
"""


def solve(target_mod: int = 1_000_000, min_n: int = 42) -> int:
    """Find least n > min_n such that t(n) % target_mod == 0 using linear recurrence for non-2 compositions."""
    c_prev2 = 1  # c[0]
    c_prev1 = 1  # c[1]
    c_cur = 1  # c[2]

    s_prev2 = 1  # S_c[0]
    s_prev1 = 2  # S_c[1]
    s_cur = 3  # S_c[2]

    pow2 = 4  # 2^2
    m = 2

    while True:
        m += 1
        c_next = (2 * c_cur - c_prev1 + c_prev2) % target_mod
        c_prev2 = c_prev1
        c_prev1 = c_cur
        c_cur = c_next

        s_prev2 = s_prev1
        s_prev1 = s_cur
        s_cur = (s_cur + c_cur) % target_mod

        pow2 = (pow2 * 2) % target_mod

        # Even n = 2*m: N(2m) = c[m] + S_c[m-2]
        n_even = 2 * m
        if n_even > min_n:
            n_even_val = (c_cur + s_prev2) % target_mod
            if (pow2 - n_even_val) % target_mod == 0:
                return n_even

        # Odd n = 2*m + 1: N(2m+1) = S_c[m]
        n_odd = 2 * m + 1
        if n_odd > min_n:
            n_odd_val = s_cur % target_mod
            if (pow2 - n_odd_val) % target_mod == 0:
                return n_odd


if __name__ == "__main__":
    print(solve())
