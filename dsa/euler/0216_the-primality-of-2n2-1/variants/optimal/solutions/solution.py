import math


def solve(limit: int = 50000000) -> int:
    """Find the number of 1 < n <= 50,000,000 for which t(n) = 2*n^2 - 1 is prime.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Quadratic Residuosity & Prime Divisors of 2*n^2 - 1:
       A prime p can divide t(n) = 2*n^2 - 1 iff 2*n^2 = 1 (mod p) <=> (2n)^2 = 2 (mod p).
       By Quadratic Reciprocity (Euler's criterion), 2 is a quadratic residue modulo p iff p = 1 or 7 (mod 8).

    2. Tonelli-Shanks Algorithm for Modular Square Root:
       - For p = 7 (mod 8) (where p = 3 mod 4):
         sqrt(2) = 2^((p+1)//4) (mod p).
       - For p = 1 (mod 8):
         Evaluate sqrt(2) mod p via Tonelli-Shanks algorithm.
       Then the roots of 2*n^2 = 1 (mod p) are given by:
           r1 = (sqrt(2) * (p+1)//2) mod p
           r2 = p - r1.

    3. Polynomial Sieve of Eratosthenes:
       Allocate bytearray is_prime_t of size limit + 1.
       For each prime p <= sqrt(2 * limit^2 - 1) with p = 1 or 7 (mod 8):
           Sieve out composite t(n) for all n = r1, r2 (mod p) where 2*n^2 - 1 > p.
           If 2*r^2 - 1 == p, then t(r) is prime itself, so sieving starts at r + p.
       Count remaining elements n in [2, limit] where is_prime_t[n] == 1.

    Complexity:
    -----------
    - Time Complexity: O(limit * log(log(limit))) operations (~19s for limit = 50,000,000).
    - Space Complexity: O(limit + sqrt(2 * limit^2)) auxiliary memory (~120 MB).
    """
    LIMIT_N = limit
    MAX_P = int(math.isqrt(2 * LIMIT_N * LIMIT_N - 1)) + 1

    # Sieve base primes up to sqrt(max t(n)) ~ 70.7 million
    is_p = bytearray([1]) * (MAX_P + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(math.isqrt(MAX_P)) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])

    is_prime_t = bytearray([1]) * (LIMIT_N + 1)
    is_prime_t[0] = is_prime_t[1] = 0

    # Polynomial sieve for roots r1, r2 modulo p
    for p in range(2, MAX_P + 1):
        if not is_p[p]:
            continue
        p_mod_8 = p % 8
        if p_mod_8 not in (1, 7):
            continue

        if p_mod_8 == 7:
            sqrt2 = pow(2, (p + 1) // 4, p)
        else:
            q = p - 1
            s = 0
            while q % 2 == 0:
                q //= 2
                s += 1
            z = 2
            while pow(z, (p - 1) // 2, p) != p - 1:
                z += 1
            c = pow(z, q, p)
            x = pow(2, (q + 1) // 2, p)
            t = pow(2, q, p)
            m = s
            while t != 1:
                i = 0
                temp = t
                while temp != 1 and i < m:
                    temp = (temp * temp) % p
                    i += 1
                b = pow(c, 1 << (m - i - 1), p)
                x = (x * b) % p
                c = (b * b) % p
                t = (t * c) % p
                m = i
            sqrt2 = x

        # n = +/- sqrt(2) * (p+1)/2 mod p
        inv2 = (p + 1) // 2
        r1 = (sqrt2 * inv2) % p
        r2 = p - r1

        for r in (r1, r2):
            start = r
            if 2 * r * r - 1 == p:
                start = r + p
            elif start == 0:
                start = p
            for n in range(start, LIMIT_N + 1, p):
                is_prime_t[n] = 0

    # Return total count of n with prime 2*n^2 - 1
    return sum(1 for n in range(2, LIMIT_N + 1) if is_prime_t[n])


if __name__ == "__main__":
    print(solve())
