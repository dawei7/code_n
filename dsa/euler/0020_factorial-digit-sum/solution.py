import math


def solve(n: int = 100) -> int:
    """Find the sum of the digits in the number n! (100!).

    Mathematical Principles Applied:
    1. Exact Factorial Computation:
       100! is a 158-digit integer (since log10(100!) = sum_{k=1}^{100} log10(k) ≈ 157.97).
       Python's math.factorial(100) computes 100! as an exact arbitrary-precision integer.

    2. Digital Sum Mapping:
       Convert 100! to a base-10 string representation and sum the integer value of each
       character digit.

    Time Complexity: O(n log^2 n) for factorial computation and decimal string conversion.
    Space Complexity: O(n log n) memory to store 158-digit string.
    """
    # Compute 100! as an exact big integer using C-optimized math.factorial
    factorial_val = math.factorial(n)

    # Convert factorial value to base-10 string representation
    factorial_str = str(factorial_val)

    # Sum each decimal digit
    digit_sum = sum(int(d) for d in factorial_str)

    # Return total sum of digits of n!
    return digit_sum


if __name__ == "__main__":
    print(solve())
