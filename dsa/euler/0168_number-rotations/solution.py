def solve(max_digits: int = 100) -> str:
    """Find the last 5 digits of the sum of all numbers N (10 < N < 10^100) that are divisors of their right-rotations.

    Mathematical Principles Applied:
    1. Right-Rotation Algebraic Equation:
       Let N be an L-digit number ending in digit d (1 <= d <= 9).
       Then N can be written as N = 10 * A + d, where A is an (L-1)-digit integer (10^(L-2) <= A < 10^(L-1)).
       Right-rotating N moves digit d to the most significant position:
       N' = d * 10^(L-1) + A.
       If N' is a multiple of N: N' = k * N for integer 1 <= k <= 9.

    2. Linear Diophantine Equation for A:
       d * 10^(L-1) + A = k * (10 * A + d)
       => d * (10^(L-1) - k) = A * (10 * k - 1)
       => A = d * (10^(L-1) - k) / (10 * k - 1).
       A is an integer iff (10 * k - 1) divides d * (10^(L-1) - k).

    3. Fast Range Search & Summation Modulo 10^5:
       Loop L from 2 to 100, last digit d from 1 to 9, multiplier k from 1 to 9.
       If A is valid (10^(L-2) <= A < 10^(L-1)), reconstruct N = 10 * A + d and add N mod 100,000.

    Time Complexity: O(max_digits * 9 * 9) executing in ~0.05s.
    Space Complexity: O(Unique_Numbers) memory for deduplication set.
    """
    MOD = 100000
    total_sum = 0
    found_numbers = set()

    # Loop digit length L from 2 to 100
    for L in range(2, max_digits + 1):
        pow10_L1 = 10 ** (L - 1)
        pow10_L2 = 10 ** (L - 2)

        # Loop last digit d (1..9) and multiplier k (1..9)
        for d in range(1, 10):
            for k in range(1, 10):
                num = d * (pow10_L1 - k)
                den = 10 * k - 1
                if num % den == 0:
                    A = num // den
                    # Verify A has exactly L-1 digits
                    if pow10_L2 <= A < pow10_L1:
                        N = A * 10 + d
                        if N not in found_numbers:
                            found_numbers.add(N)
                            total_sum = (total_sum + N) % MOD

    # Return last 5 digits of total sum formatted as zero-padded 5-character string
    return f"{total_sum % MOD:05d}"


if __name__ == "__main__":
    print(solve())
