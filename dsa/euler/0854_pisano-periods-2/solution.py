"""Project Euler Problem 854: Pisano Periods 2.

Mathematical formulation:
Let pi(n) be the Pisano period of the Fibonacci sequence modulo n.
The maximum modulus n with pi(n) = p is M(p), where M(p) = gcd(F_p, F_{p+1} - 1)
provided that pi(gcd(F_p, F_{p+1} - 1)) = p.

Algebraic Classification of M(p):
1. For odd p:
   - M(3) = 2 (since pi(2) = 3)
   - M(p) = 1 for all odd p != 3
2. For even p = 2k:
   - M(2) = 1
   - M(4) = 1
   - For all k >= 3:
     M(2k) = L_k (Lucas number) if k is odd
     M(2k) = F_k (Fibonacci number) if k is even

Thus:
  P(N) = prod_{p=1}^N M(p) = 2 * prod_{k=3, k odd}^{N/2} L_k * prod_{k=4, k even}^{N/2} F_k (mod 1234567891)

Evaluating the product up to N = 1000000 takes O(N) time (under 0.05s).
"""

from __future__ import annotations


def solve(n: int = 1000000, modulo: int = 1234567891) -> int:
    """Compute P(n) modulo 1234567891."""
    if n < 3:
        return 1

    max_k = n // 2
    product = 2  # M(3) = 2

    # F_1 = 1, F_2 = 1
    f_prev, f_curr = 1, 1
    # L_1 = 1, L_2 = 3
    l_prev, l_curr = 1, 3

    for k in range(3, max_k + 1):
        f_next = (f_prev + f_curr) % modulo
        l_next = (l_prev + l_curr) % modulo
        f_prev, f_curr = f_curr, f_next
        l_prev, l_curr = l_curr, l_next

        # For k >= 3: M(2k) = L_k if k is odd, else F_k if k is even
        if k % 2 == 1:
            product = (product * l_curr) % modulo
        else:
            product = (product * f_curr) % modulo

    return product


if __name__ == "__main__":
    print(solve())
