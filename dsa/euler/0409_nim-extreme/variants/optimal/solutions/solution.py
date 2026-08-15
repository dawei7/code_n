"""Project Euler Problem 409: Nim Extreme.

Find W(10^7) mod 1,000,000,007, where W(n) is the number of winning nim positions
of n distinct non-empty piles of size < 2^n.
"""

from array import array


def solve(n_val: int = 10_000_000, mod: int = 1_000_000_007) -> int:
    """Compute W(n_val) mod mod using Walsh-Hadamard transform algebraic closed-form evaluation."""
    q = pow(2, n_val, mod)
    q_minus_1 = (q - 1) % mod

    # Total ordered n-tuples of distinct nonzero elements: P(q-1, n)
    total = 1
    fact = 1
    term = q_minus_1
    for i in range(1, n_val + 1):
        total = (total * term) % mod
        term = (term - 1) % mod
        fact = (fact * i) % mod

    inv_fact = pow(fact, mod - 2, mod)
    comb_q_minus_1_n = (total * inv_fact) % mod

    # E_n = (-1)^n * sum_{r=0}^{floor(n/2)} (-1)^r * C(q/2, r)
    m = n_val // 2
    if m == 0:
        s = 1
    else:
        inv = array("I", [0]) * (m + 1)
        inv[1] = 1
        for i in range(2, m + 1):
            inv[i] = (mod - (mod // i) * inv[mod % i]) % mod

        n_half = pow(2, n_val - 1, mod)
        binom = 1
        s = 1
        for r in range(1, m + 1):
            term = (n_half - r + 1) % mod
            binom = (binom * term) % mod
            binom = (binom * inv[r]) % mod
            if r & 1:
                s = (s - binom) % mod
            else:
                s = (s + binom) % mod

    e_n = (-s) % mod if (n_val & 1) else s

    inv_q = pow(q, mod - 2, mod)
    losing = (fact * inv_q) % mod
    losing = (losing * (comb_q_minus_1_n + q_minus_1 * e_n)) % mod

    return (total - losing) % mod


if __name__ == "__main__":
    print(solve())
