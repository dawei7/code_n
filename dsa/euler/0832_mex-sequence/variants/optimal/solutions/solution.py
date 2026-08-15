"""Project Euler Problem 832: Mex Sequence.

Mathematical reduction:
The triplets (a, b, c = a ^ b) written on the paper possess a beautiful base-4 structure:
- In each round, a is chosen as the smallest available positive integer.
- The set of all values taken by 'a' across all rounds consists of all positive integers
  whose most significant base-4 digit is 1 (i.e. of the form 1 d_{L-2} ... d_0 in base 4).
- The corresponding b and c have most significant base-4 digits 2 and 3 respectively.
- For each base-4 digit position k with digit d_k:
    d_k = 0 -> (0, 0, 0)_4, sum = 0
    d_k = 1 -> (1, 2, 3)_4, sum = 6 * 4^k
    d_k = 2 -> (2, 3, 1)_4, sum = 6 * 4^k
    d_k = 3 -> (3, 1, 2)_4, sum = 6 * 4^k
  In other words, every non-zero base-4 digit at position k contributes exactly 6 * 4^k
  to (a + b + c), regardless of whether the digit is 1, 2, or 3!

To compute M(n) = sum_{round=1}^n (a + b + c):
- Group 'a' by base-4 length L (each block of length L has 4^{L-1} numbers).
- In block L, the leading digit at position L-1 is always 1, contributing 6 * 4^{L-1} per term.
- The lower L-1 digits simply run through integers 0 to k-1 in base 4.
- The number of non-zero digits at position p in [0, k-1] is computed in O(1) arithmetic.
"""

from __future__ import annotations


def solve(n: int = 10**18, mod: int = 1000000007) -> int:
    """Compute M(n) modulo 1_000_000_007 in O(log_4(n)^2) time."""
    total_sum = 0
    rem = n
    L = 1

    while rem > 0:
        count_in_block = 4 ** (L - 1)
        k = min(rem, count_in_block)

        # Leading digit contribution: 6 * 4^(L-1) for each of the k elements
        leading_contrib = (k % mod) * 6 % mod * pow(4, L - 1, mod) % mod
        total_sum = (total_sum + leading_contrib) % mod

        # Lower L-1 digits contributions across range [0, k - 1]
        for p in range(L - 1):
            period = 4 ** (p + 1)
            full_periods = k // period
            rem_p = k % period

            # In each full period of 4^(p+1), 3 * 4^p elements have non-zero digit at position p
            nonzero_count = full_periods * (3 * (4**p))
            if rem_p > 4**p:
                nonzero_count += rem_p - 4**p

            digit_contrib = (nonzero_count % mod) * 6 % mod * pow(4, p, mod) % mod
            total_sum = (total_sum + digit_contrib) % mod

        rem -= k
        L += 1

    return total_sum % mod


if __name__ == "__main__":
    print(solve())
