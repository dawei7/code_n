def solve(max_digits: int = 100) -> str:
    """Find last 5 digits of sum of all numbers N (10 < N < 10^max_digits) that are divisors of their right-rotation.
    
    Time Complexity: O(max_digits * 9 * 9)
    Space Complexity: O(Unique_Numbers)
    """
    MOD = 100000
    total_sum = 0
    found_numbers = set()

    for L in range(2, max_digits + 1):
        pow10_L1 = 10**(L - 1)
        pow10_L2 = 10**(L - 2)

        for d in range(1, 10):
            for k in range(1, 10):
                num = d * (pow10_L1 - k)
                den = 10 * k - 1
                if num % den == 0:
                    A = num // den
                    if pow10_L2 <= A < pow10_L1:
                        N = A * 10 + d
                        if N not in found_numbers:
                            found_numbers.add(N)
                            total_sum = (total_sum + N) % MOD

    return f"{total_sum % MOD:05d}"
