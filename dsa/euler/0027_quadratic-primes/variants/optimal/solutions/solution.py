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


def solve(limit: int = 1000) -> int:
    """Find product a * b for quadratic n^2 + a*n + b producing maximum consecutive primes.
    
    Time Complexity: O(A * B_primes * N)
    Space Complexity: O(1)
    """
    b_primes = [b for b in range(2, limit + 1) if is_prime(b)]
    max_n = 0
    best_prod = 0

    for b in b_primes:
        for a in range(-limit + 1, limit):
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1
            if n > max_n:
                max_n = n
                best_prod = a * b

    return best_prod
