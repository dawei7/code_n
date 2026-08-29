"""Project Euler Problem 1007: Alternating Difference.

Mathematical Formulation:
F_0 = 0, F_1 = 1, F_k = F_{k-1} + F_{k-2}.
A(n) is the sum of values over all C_n binary bracketings of F_0 - F_1 - ... - F_n.
Coupled 1D convolution recurrence:
A(n) = sum_{i=0}^{n-1} C_{n-1-i} A_i - sum_{i=0}^{n-1} C_i (F_{i+1} B_{n-1-i} + F_i A_{n-1-i}) mod 10^9+9.
"""

from __future__ import annotations


def solve(n_target: int = 100, mod: int = 1000000009) -> str:
    """Compute A(n) mod (10^9+9) using the 1D convolution recurrence."""
    c_arr = [0] * (n_target + 1)
    c_arr[0] = 1
    for i in range(n_target):
        c_arr[i + 1] = (c_arr[i] * (4 * i + 2) % mod) * pow(i + 2, mod - 2, mod) % mod

    f_arr = [0] * (2 * n_target + 5)
    f_arr[0] = 0
    f_arr[1] = 1
    for i in range(2, len(f_arr)):
        f_arr[i] = (f_arr[i - 1] + f_arr[i - 2]) % mod

    a_arr = [0] * (n_target + 1)
    b_arr = [0] * (n_target + 1)
    a_arr[0] = 0
    b_arr[0] = 1

    for n in range(1, n_target + 1):
        t1_a = sum(c_arr[n - 1 - i] * a_arr[i] for i in range(n)) % mod
        t2_a = sum(c_arr[i] * (f_arr[i + 1] * b_arr[n - 1 - i] + f_arr[i] * a_arr[n - 1 - i]) for i in range(n)) % mod
        a_arr[n] = (t1_a - t2_a) % mod

        t1_b = sum(c_arr[n - 1 - i] * b_arr[i] for i in range(n)) % mod
        t2_b = sum(c_arr[i] * (f_arr[i + 2] * b_arr[n - 1 - i] + f_arr[i + 1] * a_arr[n - 1 - i]) for i in range(n)) % mod
        b_arr[n] = (t1_b - t2_b) % mod

    return str(a_arr[n_target] % mod)


if __name__ == "__main__":
    print(solve())
