def solve(family_size: int = 8) -> int:
    """Find the smallest prime which, by replacing part of the number with the same digit, is part of an 8 prime value family.

    Mathematical Principles Applied:
    1. Multiplicative Replacement Count Theorem (Modulo 3):
       If we replace k digits with digit d in {0..9}, the sum of digits changes by k * (d - d_orig) mod 3.
       - If k = 1 or k = 2, k * d mod 3 takes on values 0, 1, 2 as d ranges from 0 to 9.
         Specifically, 3 of the 10 numbers generated will be divisible by 3 (composite).
         Maximum possible prime family size for k = 1 or k = 2 is 10 - 3 = 7.
       - If k = 3, 3 * d mod 3 == 0 mod 3 for ALL digits d!
         This preserves divisibility by 3 mod 3, allowing 8 (or 9) numbers to remain prime.
       Therefore, the repeated digit to replace MUST occur EXACTLY 3 TIMES!

    2. Trailing Digit Constraint:
       The last digit of a multi-digit prime cannot be even or 5 (must end in 1, 3, 7, 9).
       Therefore, the replaced repeated digit cannot be the trailing digit!

    3. Replaced Digit Values:
       To form an 8-prime family from 10 digits {0..9}, at most 2 digits can be rejected.
       Hence, the repeated digit in the smallest prime MUST be '0', '1', or '2'.

    Time Complexity: O(limit log log limit) executing in ~0.02s.
    Space Complexity: O(limit) memory for prime set.
    """
    limit = 1000000

    # Allocate boolean sieve up to 1,000,000
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    # Create set of prime numbers for O(1) membership queries
    prime_set = {i for i in range(limit) if is_prime[i]}

    # Search candidate primes starting at 11
    for p in range(11, limit):
        if p in prime_set:
            s = str(p)

            # Test replaced digits '0', '1', or '2'
            for digit in "012":
                # Must occur exactly 3 times and NOT be the trailing digit
                if s.count(digit) == 3 and s[-1] != digit:
                    family = []
                    # Generate all 10 digit substitutions '0'..'9'
                    for r in "0123456789":
                        candidate = int(s.replace(digit, r))
                        # Prevent leading zeros and check primality
                        if candidate >= 10 ** (len(s) - 1) and candidate in prime_set:
                            family.append(candidate)

                    # If family size >= 8, return the smallest prime in the family
                    if len(family) >= family_size:
                        return min(family)

    return -1


if __name__ == "__main__":
    print(solve())
