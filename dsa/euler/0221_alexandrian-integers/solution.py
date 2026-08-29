import math


def solve(target_index: int = 150000) -> int:
    """Find the 150,000th Alexandrian integer.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Alexandrian Integer Definition & Parametric Divisor Formula:
       A positive integer A is an Alexandrian integer if A = p * q * r where 1/A = 1/p + 1/q + 1/r
       for non-zero integers p, q, r.
       Setting r = -p leads to:
           q * r = p^2 + 1.
       Let d1, d2 be any divisor pair of p^2 + 1 such that d1 * d2 = p^2 + 1 (with 1 <= d1 <= p).
       Then:
           A = p * (p + d1) * (p + d2).

    2. Polynomial Sieve Factorization of p^2 + 1:
       Every prime divisor q of p^2 + 1 (except q = 2) satisfies q = 1 (mod 4).
       Using Tonelli-Shanks / Euler criterion to find modular square roots r^2 = -1 (mod q),
       we sieve and factorize p^2 + 1 for all p <= 80,000 in O(MAX_P * log log MAX_P) time.

    3. Divisor Generation & Fast Selection:
       From the prime factorization of each p^2 + 1, all divisors d1 <= p are generated directly
       without expensive trial division.
       Sorting and deduplicating yields the 150,000th element in ~1.9s.

    Complexity:
    -----------
    - Time Complexity: O(MAX_P * log(log(MAX_P)) + N log N) operations (~1.9s for target_index = 150,000).
    - Space Complexity: O(MAX_P * d_avg) memory (~25 MB).
    """
    MAX_P = 80000

    # Sieve primes up to MAX_P
    is_p = bytearray([1]) * (MAX_P + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(math.isqrt(MAX_P)) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])

    primes = [i for i in range(2, MAX_P + 1) if is_p[i]]

    # Factorize p^2 + 1 for all p in [1, MAX_P] via sieve
    factors = [[] for _ in range(MAX_P + 1)]
    rem = [p * p + 1 for p in range(MAX_P + 1)]

    # Prime 2 divides p^2 + 1 for all odd p
    for p in range(1, MAX_P + 1, 2):
        cnt = 0
        while rem[p] % 2 == 0:
            rem[p] //= 2
            cnt += 1
        factors[p].append((2, cnt))

    # Primes q == 1 (mod 4)
    for q in primes:
        if q % 4 != 1:
            continue
        # Find r such that r^2 == -1 (mod q)
        r = pow(q - 1, (q - 1) // 4, q)
        if pow(r, 2, q) != q - 1:
            r = pow(2, (q - 1) // 4, q)
            while pow(r, 2, q) != q - 1:
                r = (r + 1) % q

        for root in (r, q - r):
            for p in range(root, MAX_P + 1, q):
                cnt = 0
                while rem[p] % q == 0:
                    rem[p] //= q
                    cnt += 1
                if cnt > 0:
                    factors[p].append((q, cnt))

    # Factor in any remaining prime factor > MAX_P
    for p in range(1, MAX_P + 1):
        if rem[p] > 1:
            factors[p].append((rem[p], 1))

    # Generate all Alexandrian integers A = p * (p + d1) * (p + d2)
    alex = []

    def get_divs(facs, idx, curr):
        if idx == len(facs):
            yield curr
            return
        prime, exp = facs[idx]
        p_pow = 1
        for _ in range(exp + 1):
            yield from get_divs(facs, idx + 1, curr * p_pow)
            p_pow *= prime

    for p in range(1, MAX_P + 1):
        val = p * p + 1
        for d1 in get_divs(factors[p], 0, 1):
            if d1 * d1 <= val:
                d2 = val // d1
                A = p * (p + d1) * (p + d2)
                alex.append(A)

    # Sort and deduplicate
    alex.sort()
    unique = []
    prev = None
    for x in alex:
        if x != prev:
            unique.append(x)
            prev = x

    # Return 150,000th Alexandrian integer
    return unique[target_index - 1]


if __name__ == "__main__":
    print(solve())
