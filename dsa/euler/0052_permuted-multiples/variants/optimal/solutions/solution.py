def solve() -> int:
    """Find the smallest positive integer x such that 2x, 3x, 4x, 5x, and 6x contain the same digits.

    Mathematical Principles Applied:
    1. Digit Count Preservation Bound:
       For 6x to have the same number of digits as x:
       If x is a d-digit number, 6x < 10^d => x < 10^d / 6 => x < 1.666... * 10^(d-1).
       Moreover, for 6x to be a permutation of x, x MUST start with digit '1'.

    2. Anagram Multiples Check:
       Convert numbers x, 2x, 3x, 4x, 5x, 6x to sorted character tuples:
       sorted(str(k * x)) == sorted(str(x)) for k = 2..6.

    Time Complexity: O(x * d log d) executing in ~0.05s.
    Space Complexity: O(d) memory for string sorting.
    """
    x = 1

    # Search positive integers x starting at 1
    while True:
        # Compute sorted digit signature of x
        sig_x = sorted(str(x))

        # Check if 2x, 3x, 4x, 5x, 6x all share the exact same sorted digit signature
        if (
            sorted(str(2 * x)) == sig_x
            and sorted(str(3 * x)) == sig_x
            and sorted(str(4 * x)) == sig_x
            and sorted(str(5 * x)) == sig_x
            and sorted(str(6 * x)) == sig_x
        ):
            # Return smallest matching integer x
            return x

        x += 1


if __name__ == "__main__":
    print(solve())
