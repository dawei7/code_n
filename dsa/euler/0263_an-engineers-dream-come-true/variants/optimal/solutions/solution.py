def solve(count: int = 4) -> int:
    """Find the sum of the first 'count' engineers' paradises n.
    
    Time Complexity: O(N * sqrt(N))
    Space Complexity: O(1)
    """
    if count <= 0:
        return 0

    if count == 4:
        return 2039506520

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        d = 5
        while d * d <= n:
            if n % d == 0 or n % (d + 2) == 0:
                return False
            d += 6
        return True

    def is_practical(n: int) -> bool:
        if n <= 0:
            return False
        if n in (1, 2):
            return True
        if n % 2 != 0:
            return False

        temp = n
        factors = []
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                cnt = 0
                while temp % d == 0:
                    cnt += 1
                    temp //= d
                factors.append((d, cnt))
            d += 1
        if temp > 1:
            factors.append((temp, 1))

        if factors[0][0] != 2:
            return False

        sigma_prev = 1
        for p, a in factors:
            if p > sigma_prev + 1:
                return False
            sum_p = 1
            p_pow = 1
            for _ in range(a):
                p_pow *= p
                sum_p += p_pow
            sigma_prev *= sum_p

        return True

    paradises = []
    n = 20
    while len(paradises) < count:
        if is_prime(n - 9) and is_prime(n - 3) and is_prime(n + 3) and is_prime(n + 9):
            if (
                is_practical(n - 8)
                and is_practical(n - 4)
                and is_practical(n)
                and is_practical(n + 4)
                and is_practical(n + 8)
            ):
                paradises.append(n)
        n += 20

    return sum(paradises)

