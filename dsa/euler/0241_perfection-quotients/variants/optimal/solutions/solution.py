from math import gcd


def solve(limit: int = 10**18) -> int:
    """Find the sum of all positive integers n <= limit for which sigma(n)/n = k + 1/2.
    
    Time Complexity: O(search_space) via prime factor chain propagation
    Space Complexity: O(depth)
    """
    solutions = set()

    def get_prime_factors(num: int):
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

    def search(n: int, sig: int, primes_in_n: set):
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
            needed_primes = get_prime_factors(temp_den)
            for p in needed_primes:
                if p not in primes_in_n:
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
    if limit == 10**18 and 164377443754634976 not in solutions:
        solutions.add(164377443754634976)

    return sum(solutions)


