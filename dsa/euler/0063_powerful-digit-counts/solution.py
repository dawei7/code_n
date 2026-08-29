import math


def solve() -> int:
    """Find how many n-digit positive integers exist which are also an n-th power.

    Mathematical Principles Applied:
    1. Base Upper Bound (a < 10):
       If a >= 10, then a^n >= 10^n, which has at least n + 1 digits for all n >= 1.
       Therefore, the base 'a' MUST be a single digit integer: a in {1, 2, 3, 4, 5, 6, 7, 8, 9}.

    2. Logarithmic Exponent Upper Bound:
       We want len(str(a^n)) == n, which is equivalent to 10^(n-1) <= a^n < 10^n.
       Taking base-10 logarithm:
       n - 1 <= n * log10(a) => n * (1 - log10(a)) <= 1 => n <= 1 / (1 - log10(a)).
       - For a = 9: n <= 1 / (1 - log10(9)) = 1 / 0.04576 = 21.85 => n <= 21.
       - For smaller a, the maximum exponent n is strictly smaller.

    3. Closed-Form Count:
       Total count = sum_{a=1}^9 floor( 1 / (1 - log10(a)) ).

    Time Complexity: O(1) constant time execution in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    total_count = 0

    # Iterate base a from 1 to 9 (bases >= 10 always produce >= n+1 digits)
    for a in range(1, 10):
        # Exponent n starts at 1
        n = 1
        # Increment n while a^n has exactly n decimal digits
        while len(str(a**n)) == n:
            total_count += 1
            n += 1

    # Return total count of n-digit n-th powers
    return total_count


if __name__ == "__main__":
    print(solve())
