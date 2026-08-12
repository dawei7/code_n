def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)):
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def solve(target: int = 2000) -> int:
    """Find 2000th tile in sequence where PD(n) = 3.
    
    Time Complexity: O(R * Primality)
    Space Complexity: O(1)
    """
    # Tile 1 has PD(1) = 3
    count = 1
    if target == 1:
        return 1

    r = 1
    while True:
        # 1. Top tile of ring r: S_r = 3r^2 - 3r + 2
        if is_prime(6 * r - 1) and is_prime(6 * r + 1) and is_prime(12 * r + 5):
            count += 1
            if count == target:
                return 3 * r * r - 3 * r + 2

        # 2. End tile of ring r: E_r = 3r^2 + 3r + 1 (for r > 1, as E_1 has PD=2)
        if r > 1:
            if is_prime(6 * r - 1) and is_prime(6 * r + 5) and is_prime(12 * r - 7):
                count += 1
                if count == target:
                    return 3 * r * r + 3 * r + 1

        r += 1
