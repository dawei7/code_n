import math


def power(base: int, exp: int, mod: int) -> int:
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res


def mod_sqrt(a: int, p: int) -> int:
    if a == 0:
        return 0
    if p == 2:
        return a
    if power(a, (p - 1) // 2, p) != 1:
        return -1
    if p % 4 == 3:
        return power(a, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    z = 2
    while power(z, (p - 1) // 2, p) not in (0, p - 1):
        z += 1

    c = power(z, q, p)
    x = power(a, (q + 1) // 2, p)
    t = power(a, q, p)
    m = s

    while t != 1:
        i = 0
        temp = t
        while temp != 1 and i < m:
            temp = (temp * temp) % p
            i += 1
        b = power(c, 1 << (m - i - 1), p)
        x = (x * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return x


def solve(limit: int = 75000000) -> int:
    """Find number of barely obtuse triangles (a^2 + b^2 = c^2 - 1) with perimeter <= limit.
    
    Time Complexity: O(limit * log(log(limit))) via quadratic polynomial sieve
    Space Complexity: O(limit / 6)
    """
    LIMIT_P = limit
    MAX_K = (LIMIT_P - 1) // 6
    MAX_VAL = 4 * MAX_K * MAX_K + 1
    MAX_PRIME = int(math.sqrt(MAX_VAL)) + 1

    is_p = bytearray([1]) * (MAX_PRIME + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(math.sqrt(MAX_PRIME)) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b'\x00' * len(is_p[i * i :: i])

    rem = [4 * k * k + 1 for k in range(MAX_K + 1)]
    pf_list = [[] for _ in range(MAX_K + 1)]

    for p in range(5, MAX_PRIME + 1, 4):
        if not is_p[p]:
            continue
        r1 = mod_sqrt(p - 1, p)
        if r1 == -1:
            continue
        r2 = p - r1

        inv2 = (p + 1) // 2
        k1 = (r1 * inv2) % p
        k2 = (r2 * inv2) % p

        for k_root in (k1, k2):
            start_k = k_root if k_root > 0 else k_root + p
            for k in range(start_k, MAX_K + 1, p):
                count = 0
                while rem[k] % p == 0:
                    rem[k] //= p
                    count += 1
                pf_list[k].append((p, count))

    ans = 0
    for k in range(1, MAX_K + 1):
        a = 2 * k
        pf = list(pf_list[k])
        if rem[k] > 1:
            pf.append((rem[k], 1))

        divisors = [1]
        for p_val, exp in pf:
            sz = len(divisors)
            p_pow = 1
            for e in range(1, exp + 1):
                p_pow *= p_val
                for i in range(sz):
                    divisors.append(divisors[i] * p_pow)

        prod = 4 * k * k + 1
        for d1 in divisors:
            if d1 * d1 > prod:
                continue
            d2 = prod // d1
            if d2 - d1 < 2 * a:
                continue
            if a + d2 <= LIMIT_P:
                ans += 1

    return ans
