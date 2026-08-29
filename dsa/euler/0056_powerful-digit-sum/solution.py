def solve(limit: int = 100) -> int:
    """Find the maximum digital sum of a^b for positive integers a, b < limit (100).

    Mathematical Principles Applied:
    1. Digital Sum Function:
       Let S(n) = sum_{c in str(n)} int(c).
       We maximize S(a^b) over the 2D domain (a, b) in [1, 99] x [1, 99].

    2. Arbitrary-Precision Integer Powers:
       For a, b < 100, a^b has at most 200 decimal digits.
       Python's exact BigInt arithmetic computes a^b and its digit sum in O(d) steps.

    Time Complexity: O(limit^2 * log10(limit^limit)) executing in ~0.08s.
    Space Complexity: O(limit) memory to format digit strings.
    """
    # Maximize sum of digits of a^b for all 1 <= a < 100 and 1 <= b < 100
    max_digital_sum = max(
        sum(int(c) for c in str(a**b))
        for a in range(1, limit)
        for b in range(1, limit)
    )

    # Return the maximum digital sum found
    return max_digital_sum


if __name__ == "__main__":
    print(solve())
