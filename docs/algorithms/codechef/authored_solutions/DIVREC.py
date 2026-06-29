import sys
import math
import random
from collections import Counter


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
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


def pollard(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        c = random.randrange(1, n - 1)
        x = random.randrange(0, n - 1)
        y = x
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d


def factor(n: int, out: list[int]) -> None:
    if n == 1:
        return
    if is_prime(n):
        out.append(n)
        return
    d = pollard(n)
    factor(d, out)
    factor(n // d, out)


def sigma(n: int) -> int:
    factors = []
    factor(n, factors)
    counts = Counter(factors)
    result = 1
    for p, exp in counts.items():
        result *= (p ** (exp + 1) - 1) // (p - 1)
    return result


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, a, b = data[idx:idx + 3]
        idx += 3
        numerator = x * b
        if numerator % a != 0:
            out.append("-1")
            continue
        n = numerator // a
        out.append(str(n if n > 0 and sigma(n) == x else -1))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
