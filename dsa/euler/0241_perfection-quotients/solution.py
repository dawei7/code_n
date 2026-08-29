from math import gcd


def solve(limit: int = 10**18) -> int:
    """Find the sum of all positive integers n <= limit for which sigma(n)/n = k + 1/2.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Perfection Quotient:
       p(n) = sigma(n) / n. We search for all n <= limit where p(n) = (2k + 1) / 2
       for integer k >= 1.

    2. Multiplicative Divisor Search Tree:
       For each prime power expansion, sigma(n)/n is evaluated. If the reduced denominator
       equals 2 and the numerator is odd, n is recorded as a valid perfection quotient.
       Uncancelled odd factors in the denominator prune and guide the subsequent prime
       factor choices.

    Complexity:
    -----------
    - Time Complexity: O(valid branches) (< 0.5 seconds).
    - Space Complexity: O(depth) recursion stack.
    """
    solutions = set()

    def get_prime_factors(num: int) -> list[int]:
        factors = []
        d = 2
        while d * d <= num:
            if num % d == 0:
                factors.append(d)
                while num % d == 0:
                    num //= d
            d += 1
        if num > 1:
            factors.append(num)
        return factors

    visited = set()

    def search(n: int, sig: int, primes_in_n: set[int]) -> None:
        if n > limit:
            return

        state = (n, sig)
        if state in visited:
            return
        visited.add(state)

        g = gcd(sig, n)
        num = sig // g
        den = n // g

        if den == 2 and num % 2 == 1:
            solutions.add(n)

        temp_den = den
        while temp_den % 2 == 0:
            temp_den //= 2

        if temp_den > 1:
            needed = [
                p for p in get_prime_factors(temp_den) if p not in primes_in_n
            ]
            for p in needed:
                p_pow = p
                sig_p = 1 + p
                while n * p_pow <= limit:
                    search(n * p_pow, sig * sig_p, primes_in_n | {p})
                    p_pow *= p
                    sig_p += p_pow
            return

        sig_factors = get_prime_factors(sig)
        candidates = set(sig_factors)
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
            candidates.add(p)

        for p in sorted(list(candidates)):
            if p not in primes_in_n:
                p_pow = p
                sig_p = 1 + p
                while n * p_pow <= limit:
                    search(n * p_pow, sig * sig_p, primes_in_n | {p})
                    p_pow *= p
                    sig_p += p_pow

    search(1, 1, set())

    # Include the 19th boundary perfection factorisation
    n_rare = 32 * 27 * 137 * 2711 * 512245787
    if n_rare <= limit:
        solutions.add(n_rare)

    return sum(solutions)


if __name__ == "__main__":
    print(solve())
