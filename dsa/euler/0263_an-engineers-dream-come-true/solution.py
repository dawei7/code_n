"""Project Euler 263: An Engineers' Dream Come True

Find the sum of the first four engineers' paradises n such that:
1. (n-9, n-3), (n-3, n+3), (n+3, n+9) form three consecutive sexy prime pairs.
2. n-8, n-4, n, n+4, n+8 are all practical numbers.
"""

from __future__ import annotations


def solve(target_count: int = 4) -> str:
    """Finds the sum of the first `target_count` engineers' paradises using

    deterministic Miller-Rabin primality testing, Srinivasan practical number verification,
    and modular residue filtering.
    """

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            return True
        if (
            n % 2 == 0
            or n % 3 == 0
            or n % 5 == 0
            or n % 7 == 0
            or n % 11 == 0
            or n % 13 == 0
        ):
            return False
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 7, 61):
            if n <= a:
                continue
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

    def is_practical(m: int) -> bool:
        if m % 2 != 0:
            return False
        temp = m
        c2 = 0
        while temp % 2 == 0:
            c2 += 1
            temp //= 2
        sigma = (1 << (c2 + 1)) - 1

        d = 3
        while d * d <= temp:
            if temp % d == 0:
                if d > sigma + 1:
                    return False
                term = 1
                cur = 1
                while temp % d == 0:
                    temp //= d
                    cur *= d
                    term += cur
                sigma *= term
            d += 2
        if temp > 1:
            if temp > sigma + 1:
                return False
        return True

    found: list[int] = []
    base = 0
    while len(found) < target_count:
        for n in (base + 20, base + 40):
            # Modular sieving:
            rem7 = n % 7
            if rem7 not in (0, 1, 6):
                continue
            rem11 = n % 11
            if rem11 in (2, 3, 8, 9):
                continue
            rem13 = n % 13
            if rem13 in (3, 4, 9, 10):
                continue

            # 1. Four sexy primes
            if not is_prime(n - 9):
                continue
            if not is_prime(n - 3):
                continue
            if not is_prime(n + 3):
                continue
            if not is_prime(n + 9):
                continue

            # 2. Intervening numbers must be composite (consecutive primes condition)
            if is_prime(n - 7) or is_prime(n - 5):
                continue
            if is_prime(n - 1) or is_prime(n + 1):
                continue
            if is_prime(n + 5) or is_prime(n + 7):
                continue

            # 3. Practical numbers check for n-8, n-4, n, n+4, n+8
            if not is_practical(n):
                continue
            if not is_practical(n - 4) or not is_practical(n + 4):
                continue
            if not is_practical(n - 8) or not is_practical(n + 8):
                continue

            found.append(n)
            if len(found) == target_count:
                break
        base += 60

    return str(sum(found))


if __name__ == "__main__":
    print(solve())
