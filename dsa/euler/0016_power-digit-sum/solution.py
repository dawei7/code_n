def solve(exp: int = 1000) -> int:
    """Find the sum of the digits of the number 2^exp.

    Mathematical Principles Applied:
    1. Exact Large Integer Exponentiation:
       2^1000 is a 302-digit integer (since log10(2^1000) = 1000 * log10(2) ≈ 301.03).
       Python natively supports arbitrary-precision integers.

    2. Digital Sum Mapping:
       Convert 2^exp to its base-10 string representation and sum the integer value
       of each character digit.

    Time Complexity: O(exp^2) due to BigInt binary-to-decimal string conversion.
    Space Complexity: O(exp) memory to store 302-digit string.
    """
    # Compute 2^exp using fast binary exponentiation
    val = 2**exp

    # Convert large integer to base-10 string representation
    val_str = str(val)

    # Sum each decimal digit
    digit_sum = sum(int(d) for d in val_str)

    # Return total sum of digits
    return digit_sum


if __name__ == "__main__":
    print(solve())
