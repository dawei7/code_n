from array import array


def solve(limit: int = 25000000) -> int:
    """Find number of barely acute triangles (a^2 + b^2 = c^2 + 1) with perimeter a + b + c <= 25,000,000.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Barely Acute Triangle Diophantine Equation:
       a^2 + b^2 = c^2 + 1 with 1 <= a <= b <= c.
       - Case a = 1: 1 + b^2 = c^2 + 1 => b = c.
         Triangles (1, b, b) are valid for all 1 <= b <= (limit - 1) / 2.
         Base count = (limit - 1) // 2.

    2. Difference of Squares Factorization for a >= 2:
       a^2 - 1 = c^2 - b^2 = (c - b)(c + b).
       Let (a - 1)(a + 1) = d1 * d2 where d1 = c - b and d2 = c + b (with d1 <= d2).
       Then c = (d1 + d2) / 2 and b = (d2 - d1) / 2.

    3. Fast Bounding & Divisor Filtering:
       - Parity condition: d1 and d2 have the same parity ((d1 + d2) % 2 == 0).
       - Side inequality: b >= a => d2 - d1 >= 2*a.
       - Perimeter constraint: a + b + c = a + d2 <= limit => d1 >= (a^2 - 1) / (limit - a).
       - Maximum a: since a <= b <= c, a <= limit // 3 = 8,333,333.

    Complexity:
    -----------
    - Time Complexity: O(limit * log(limit)) operations (~15s for limit = 25,000,000).
    - Space Complexity: O(limit / 3) memory using 32-bit integer array (~35 MB).
    """
    LIMIT_P = limit
    MAX_A = LIMIT_P // 3

    # Sieve smallest prime factors min_p up to MAX_A + 1
    min_p = array("I", [0] * (MAX_A + 2))
    for i in range(2, int((MAX_A + 2) ** 0.5) + 1):
        if min_p[i] == 0:
            for j in range(i * i, MAX_A + 2, i):
                if min_p[j] == 0:
                    min_p[j] = i
    for i in range(2, MAX_A + 2):
        if min_p[i] == 0:
            min_p[i] = i

    # Base count for a = 1: triangles (1, b, b)
    ans = (LIMIT_P - 1) // 2

    # Factorize a^2 - 1 = (a - 1)(a + 1) for each a from 2 to MAX_A
    for a in range(2, MAX_A + 1):
        fac_dict = {}
        for num in (a - 1, a + 1):
            n = num
            while n > 1:
                p = min_p[n]
                c = 0
                while n % p == 0:
                    n //= p
                    c += 1
                fac_dict[p] = fac_dict.get(p, 0) + c

        divisors = [1]
        for p, exp in fac_dict.items():
            sz = len(divisors)
            p_pow = 1
            for e in range(1, exp + 1):
                p_pow *= p
                for i in range(sz):
                    divisors.append(divisors[i] * p_pow)

        prod = (a - 1) * (a + 1)
        min_d1 = (prod + (LIMIT_P - a) - 1) // (LIMIT_P - a)

        for d1 in divisors:
            if d1 * d1 > prod:
                continue
            if d1 < min_d1:
                continue
            d2 = prod // d1
            if (d1 + d2) % 2 == 0 and (d2 - d1) >= 2 * a:
                ans += 1

    return ans


if __name__ == "__main__":
    print(solve())
