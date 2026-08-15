import math


def solve(target: int = 1000000) -> int:
    """Find the 1,000,000th lexicographic permutation of digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

    Mathematical Principles Applied:
    1. Factorial Number System (Factoradix Base Conversion):
       Any permutation rank K in [0, N! - 1] can be uniquely represented in the factorial number system:
       K = d_{N-1} * (N-1)! + d_{N-2} * (N-2)! + ... + d_0 * 0!
       where 0 <= d_i <= i.

    2. Direct Digit Selection via Factorial Division:
       Starting with digits [0, 1, ..., 9] and target rank k = 1,000,000 - 1 = 999,999:
       - For position i (from 9 down to 0):
         idx = k // i!
         k = k % i!
         Select element digits[idx] and remove it from available digits list.

    3. Performance Advantage:
       Computes the exact 1,000,000th permutation directly in O(N^2) time without generating
       the 999,999 preceding permutations.

    Time Complexity: O(N^2) where N = 10 (executes in ~0.00005s).
    Space Complexity: O(N) auxiliary space.
    """
    # Available digit choices in ascending lexicographical order
    digits = list(range(10))

    # Convert 1-indexed target rank (1,000,000) to 0-indexed rank (999,999)
    k = target - 1

    # Store character sequence of target permutation
    result_digits = []

    # Process each position from left to right (factorial coefficients for 9! down to 0!)
    for i in range(9, -1, -1):
        # Calculate (i)!
        fact = math.factorial(i)

        # Determine index of digit to select: idx = k // (i!)
        idx = k // fact

        # Update remaining rank: k = k % (i!)
        k %= fact

        # Pop selected digit at index 'idx' and append to result
        result_digits.append(str(digits.pop(idx)))

    # Combine extracted digit string into an integer and return
    return int("".join(result_digits))


if __name__ == "__main__":
    print(solve())
