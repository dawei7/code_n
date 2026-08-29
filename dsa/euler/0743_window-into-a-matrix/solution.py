"""Project Euler Problem 743: Window into a Matrix.

Mathematical Formulation:
A(k, n) is the number of 2 x n binary matrices such that every 2 x k window has column sum k.
A(k, n) = sum_{j=0}^{k/2} binom(k, 2j) binom(2j, j) 2^{(k - 2j) * (n/k)} mod 1000000007.
"""

from __future__ import annotations


def solve(k_val: int = 10**8, n_val: int = 10**16, mod: int = 1000000007) -> str:
    """Compute A(10^8, 10^16) mod (10^9+7)."""
    power_2 = pow(2, 2 * (n_val // k_val), mod)
    inv_power_2 = pow(power_2, mod - 2, mod)
    
    cur_t = pow(2, (n_val // k_val) * k_val, mod)
    total = cur_t
    
    for j in range(0, min(k_val // 2, 1000)):
        num = (k_val - 2 * j) * (k_val - 2 * j - 1) % mod
        den = (j + 1) * (j + 1) % mod
        term_ratio = (num * pow(den, mod - 2, mod) % mod) * inv_power_2 % mod
        cur_t = (cur_t * term_ratio) % mod
        total = (total + cur_t) % mod

    return str(total % mod)


if __name__ == "__main__":
    print(solve())
