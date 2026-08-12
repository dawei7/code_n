import math


def solve(limit: int = 100, digits: int = 100) -> int:
    """Find total of digital sums of first 100 decimal digits for irrational square roots n <= 100.
    
    Time Complexity: O(limit * digits)
    Space Complexity: O(digits)
    """
    total_sum = 0
    # Scale factor for 100 decimal digits (2 * (digits - 1) zeros = 10^198)
    scale = 10 ** (2 * (digits - 1))

    for n in range(1, limit + 1):
        root = math.isqrt(n)
        if root * root == n:
            continue  # Skip rational square roots

        # Integer square root of n * 10^198 gives 100 full digits
        big_root = math.isqrt(n * scale)
        s_digits = str(big_root)[:digits]
        total_sum += sum(int(c) for c in s_digits)

    return total_sum
