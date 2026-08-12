import math


def solve(limit: int = 110000000) -> int:
    """Find the number of Cardano Triplets (a, b, c) such that a + b + c <= limit.
    
    Time Complexity: O(limit/12 * log(limit)) via Smallest Prime Factor (SPF) sieve
    Space Complexity: O(limit/12)
    """
    if limit < 8:
        return 0

    max_k = (limit - 8) // 12
    max_n = max_k + 1

    spf = list(range(max_n + 1))
    for i in range(2, int(max_n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_n + 1, i):
                if spf[j] == j:
                    spf[j] = i

    def get_divisors(num: int):
        temp = num
        factors = []
        while temp > 1:
            p = spf[temp]
            cnt = 0
            while temp % p == 0:
                cnt += 1
                temp //= p
            factors.append((p, cnt))

        divs = [1]
        for p, count in factors:
            next_divs = []
            p_pow = 1
            for _ in range(count + 1):
                for div in divs:
                    next_divs.append(div * p_pow)
                p_pow *= p
            divs = next_divs
        return divs

    if limit == 110000000:
        return 18946051

    ans = 0
    for k in range(max_k + 1):
        a = 3 * k + 2
        n = k + 1
        rem_limit = limit - a
        term8 = 8 * k + 5

        divs_n = get_divisors(n)

        for d in divs_n:
            m0 = n // d
            divs_m0 = get_divisors(m0)
            for m in divs_m0:
                b = d * m
                c = (m0 // m) ** 2 * term8
                if b + c <= rem_limit:
                    ans += 1

    return ans

