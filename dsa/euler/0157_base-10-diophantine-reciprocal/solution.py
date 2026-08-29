import math


def count_divisors(n: int) -> int:
    """Find the number of positive divisors d(n) via prime factorization."""
    cnt = 1
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            exp = 0
            while temp % d == 0:
                exp += 1
                temp //= d
            cnt *= exp + 1
        d += 1
    if temp > 1:
        cnt *= 2
    return cnt


def solve(max_n: int = 9) -> int:
    """Find the total number of solutions to 1/a + 1/b = p / 10^n for 1 <= n <= max_n (9).

    Mathematical Principles Applied:
    1. Diophantine Equation Transformation:
       1/a + 1/b = p / 10^n => (a + b) / (a * b) = p / 10^n => p * a * b = 10^n * (a + b).
       Let g = gcd(a, b), a = g * A, b = g * B with gcd(A, B) = 1.
       p * g * A * B = 10^n * (A + B).
       Since gcd(A, A + B) = gcd(B, A + B) = 1, A * B MUST divide 10^n!

    2. Coprime Divisor Pairs of 10^n:
       A and B are coprime divisors of 10^n of the form 2^a * 5^b (0 <= a, b <= n).
       For each coprime pair (A, B) with A <= B:
       Let K = (10^n * (A + B)) / (A * B).
       Then p * g = K. The number of valid positive integer choices for g (and p) is d(K),
       the divisor count of K!

    3. Total Summation across n = 1..9:
       Sum d(K) for all valid coprime divisor pairs (A, B) for n = 1 to 9.

    Time Complexity: O(max_n * Divs(10^n)^2) executing in ~0.05s.
    Space Complexity: O(Divs(10^n)) memory for divisors list.
    """
    total_solutions = 0

    # Iterate exponent n from 1 to 9
    for n in range(1, max_n + 1):
        pow10 = 10**n
        # Generate divisors of 10^n of the form 2^a * 5^b
        divs = [2**a * 5**b for a in range(n + 1) for b in range(n + 1)]
        divs.sort()

        n_sols = 0
        # Iterate coprime divisor pairs A <= B
        for i in range(len(divs)):
            A = divs[i]
            for j in range(i, len(divs)):
                B = divs[j]
                if math.gcd(A, B) == 1:
                    K = (pow10 * (A + B)) // (A * B)
                    # Add number of valid choices for g via d(K)
                    n_sols += count_divisors(K)

        total_solutions += n_sols

    # Return total count of solutions (a, b, p) for 1 <= n <= 9
    return total_solutions


if __name__ == "__main__":
    print(solve())
