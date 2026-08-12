import functools


def is_prime(n: int) -> bool:
    """Miller-Rabin primality test for fast checking of large concatenated numbers."""
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)):
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 7, 61):  # Deterministic for n < 4.7 x 10^9
        if n <= a:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


@functools.lru_cache(maxsize=None)
def is_pair_valid(p1: int, p2: int) -> bool:
    s1, s2 = str(p1), str(p2)
    return is_prime(int(s1 + s2)) and is_prime(int(s2 + s1))


def solve(limit: int = 10000) -> int:
    """Find lowest sum for a set of 5 primes where any two concatenate to produce a prime.
    
    Time Complexity: O(P^5) with heavy clique pruning
    Space Complexity: O(P^2)
    """
    is_p = [True] * limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit, i):
                is_p[j] = False

    primes = [i for i in range(3, limit) if is_p[i]]  # 2 can never form odd concatenations

    for i, p1 in enumerate(primes):
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            if not is_pair_valid(p1, p2):
                continue
            for k in range(j + 1, len(primes)):
                p3 = primes[k]
                if not (is_pair_valid(p1, p3) and is_pair_valid(p2, p3)):
                    continue
                for m in range(k + 1, len(primes)):
                    p4 = primes[m]
                    if not (is_pair_valid(p1, p4) and is_pair_valid(p2, p4) and is_pair_valid(p3, p4)):
                        continue
                    for n in range(m + 1, len(primes)):
                        p5 = primes[n]
                        if is_pair_valid(p1, p5) and is_pair_valid(p2, p5) and is_pair_valid(p3, p5) and is_pair_valid(p4, p5):
                            return p1 + p2 + p3 + p4 + p5
    return -1
