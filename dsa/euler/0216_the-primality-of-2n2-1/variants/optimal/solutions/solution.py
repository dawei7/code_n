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


def solve(limit: int = 50000000) -> int:
    """Find number of n <= limit for which t(n) = 2*n^2 - 1 is prime.
    
    Time Complexity: O(limit * log(log(limit)))
    Space Complexity: O(limit + sqrt(2 * limit^2))
    """
    LIMIT_N = limit
    MAX_T = 2 * LIMIT_N * LIMIT_N - 1
    MAX_P = int(math.sqrt(MAX_T)) + 1

    is_p = bytearray([1]) * (MAX_P + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(math.sqrt(MAX_P)) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b'\x00' * len(is_p[i * i :: i])

    is_prime_t = bytearray([1]) * (LIMIT_N + 1)
    is_prime_t[0] = is_prime_t[1] = 0

    for p in range(2, MAX_P + 1):
        if not is_p[p]:
            continue
        if p % 8 not in (1, 7):
            continue

        target = (p + 1) // 2
        r1 = mod_sqrt(target, p)
        if r1 == -1:
            continue
        r2 = p - r1

        for r in (r1, r2):
            start = r if r > 0 else r + p
            for n in range(start, LIMIT_N + 1, p):
                if 2 * n * n - 1 > p:
                    is_prime_t[n] = 0

    return sum(1 for n in range(2, LIMIT_N + 1) if is_prime_t[n])
