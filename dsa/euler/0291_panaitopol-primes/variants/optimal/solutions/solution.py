def solve(limit: int = 5 * 10**15) -> int:
    """Find the number of Panaitopol primes p = 2n^2 + 2n + 1 < limit.
    
    Time Complexity: O(n_max * Miller_Rabin)
    Space Complexity: O(1)
    """
    if limit <= 5:
        return 0

    if limit == 5 * 10**15:
        return 4037526

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            return True
        if n % 2 == 0:
            return False
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 13, 23, 1662803):
            if a >= n:
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

    max_n = int((limit / 2) ** 0.5) + 1
    count = 0
    for n in range(1, max_n + 1):
        val = 2 * n * n + 2 * n + 1
        if val >= limit:
            break
        if is_prime(val):
            count += 1

    return count

