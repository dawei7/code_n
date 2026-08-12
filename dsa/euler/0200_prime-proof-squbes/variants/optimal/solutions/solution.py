import math


def is_prime(n: int) -> bool:
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

    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime_proof(n: int) -> bool:
    s = str(n)
    L = len(s)
    for i in range(L):
        orig_digit = ord(s[i]) - 48
        for d in range(10):
            if d == orig_digit:
                continue
            if i == 0 and d == 0:
                continue

            val = int(s[:i] + str(d) + s[i + 1 :])
            if is_prime(val):
                return False
    return True


def solve(target: int = 200) -> int:
    """Find the N-th prime-proof sqube containing contiguous substring '200'.
    
    Time Complexity: O(P^2 * log P) where P is max prime needed.
    Space Complexity: O(P)
    """
    MAX_P = 200000
    is_p = bytearray([1]) * (MAX_P + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(MAX_P**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b'\x00' * len(is_p[i * i :: i])
    primes = [i for i in range(2, MAX_P + 1) if is_p[i]]

    squbes = []
    for i, p in enumerate(primes):
        p2 = p * p
        for j, q in enumerate(primes):
            if i == j:
                continue
            val = p2 * q * q * q
            if val > 3 * 10**11:
                break
            if '200' in str(val):
                squbes.append(val)

    squbes.sort()

    count = 0
    for s in squbes:
        if is_prime_proof(s):
            count += 1
            if count == target:
                return s

    return 0
