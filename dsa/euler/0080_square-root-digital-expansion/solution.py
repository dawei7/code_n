import math


def solve(limit: int = 100, digits: int = 100) -> int:
    """Find the total sum of the first 100 decimal digits for all irrational square roots of n <= 100.

    Mathematical Principles Applied:
    1. Integer Scaling Method for Decimal Digit Expansion:
       To extract D decimal digits of sqrt(n), multiply n by 10^(2*(D-1)).
       The integer square root satisfies:
       isqrt(n * 10^(2*(D-1))) = floor( sqrt(n) * 10^(D-1) ).
       This exact BigInt integer contains the first D decimal digits of sqrt(n)!

    2. Filtering Perfect Squares:
       If isqrt(n)^2 == n, sqrt(n) is an integer (rational), so skip.

    3. Summing 100 Digits per Irrational Root:
       Convert big_root to string, take the first 100 characters, and sum integer digits.

    Time Complexity: O(limit * log2(digits)) executing in ~0.002s.
    Space Complexity: O(digits) memory to store BigInt string.
    """
    total_digital_sum = 0

    # Scaling multiplier: 10^(2 * 99) = 10^198 to extract 100 decimal digits
    scale = 10 ** (2 * (digits - 1))

    # Iterate n from 1 up to limit = 100
    for n in range(1, limit + 1):
        root = math.isqrt(n)

        # Skip perfect squares (rational roots)
        if root * root == n:
            continue

        # Compute 100-digit integer square root: isqrt(n * 10^198)
        big_root = math.isqrt(n * scale)

        # Extract first 100 characters and sum individual digits
        s_digits = str(big_root)[:digits]
        total_digital_sum += sum(int(c) for c in s_digits)

    # Return total sum of digital expansions for all 90 irrational square roots
    return total_digital_sum


if __name__ == "__main__":
    print(solve())
