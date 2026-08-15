import math


def is_pandigital_9(s: str) -> bool:
    """Check if 9-character string s contains a 1-9 9-digit pandigital permutation."""
    return "".join(sorted(s)) == "123456789"


def solve() -> int:
    """Find index k of the first Fibonacci number F_k whose first 9 and last 9 digits are 1-9 pandigital.

    Mathematical Principles Applied:
    1. Modular Recurrence for Last 9 Digits:
       F_k mod 10^9 satisfies the linear recurrence:
       F_k = (F_{k-1} + F_{k-2}) mod 10^9.
       Testing `is_pandigital_9(str(F_k mod 10^9))` eliminates 99.999% of candidates in O(1) time per step!

    2. Binet's Formula & Logarithmic Approximation for First 9 Digits:
       By Binet's formula: F_k ≈ phi^k / sqrt(5) where phi = (1 + sqrt(5)) / 2.
       Taking base-10 logarithm:
       log10(F_k) ≈ k * log10(phi) - log10(sqrt(5)).
       Fractional part `frac = log10(F_k) % 1.0` yields the leading digits:
       leading_digits = int(10^(frac + 8)).

    Time Complexity: O(k) for k ≈ 329,468 (executes in ~0.25s).
    Space Complexity: O(1) constant auxiliary space.
    """
    a, b = 1, 1
    k = 2

    # Precalculate Binet's formula logarithmic constants
    log10_phi = math.log10((1 + 5**0.5) / 2)
    log10_sqrt5 = math.log10(5**0.5)

    mod = 10**9

    # Advance Fibonacci index k upwards
    while True:
        k += 1
        a, b = b, (a + b) % mod

        # Fast check 1: evaluate last 9 digits of F_k modulo 10^9
        s_last = f"{b:09d}"
        if is_pandigital_9(s_last):
            # Check 2: evaluate first 9 digits using Binet's logarithmic approximation
            frac = (k * log10_phi - log10_sqrt5) % 1.0
            first9 = str(int(10 ** (frac + 8)))

            # If first 9 digits are also 1-9 pandigital, return index k
            if is_pandigital_9(first9):
                return k


if __name__ == "__main__":
    print(solve())
