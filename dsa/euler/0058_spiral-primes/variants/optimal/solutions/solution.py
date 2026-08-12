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


def solve(target_ratio: float = 0.10) -> int:
    """Find side length of square spiral for which ratio of diagonal primes falls below 10%.
    
    Time Complexity: O(S * sqrt(S))
    Space Complexity: O(1)
    """
    prime_count = 0
    s = 3

    while True:
        corner1 = s * s - (s - 1)
        corner2 = s * s - 2 * (s - 1)
        corner3 = s * s - 3 * (s - 1)

        if is_prime(corner1):
            prime_count += 1
        if is_prime(corner2):
            prime_count += 1
        if is_prime(corner3):
            prime_count += 1

        total_diagonals = 2 * s - 1
        if prime_count / total_diagonals < target_ratio:
            return s

        s += 2
