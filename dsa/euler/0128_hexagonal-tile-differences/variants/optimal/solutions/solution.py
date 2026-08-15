def is_prime(n: int) -> bool:
    """Fast wheel primality test for ring difference expressions."""
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
    """Find the 2000th tile in sequence where PD(n) = 3 (3 prime differences among 6 neighbors).

    Mathematical Principles Applied:
    1. Hexagonal Grid Ring Geometry & Pruning Theorem:
       In a hexagonal spiral tiling, ring r (r >= 1) contains 6r tiles.
       Tiles inside ring r can NEVER obtain PD(n) = 3 EXCEPT for two specific candidate positions per ring:
       - Top tile of ring r: S_r = 3*r^2 - 3*r + 2.
       - End tile of ring r: E_r = 3*r^2 + 3*r + 1.

    2. Primality Conditions for Top Tile S_r:
       S_r has 3 prime differences iff all three expressions are prime:
       (6*r - 1), (6*r + 1), (12*r + 5).

    3. Primality Conditions for End Tile E_r (r > 1):
       E_r has 3 prime differences iff all three expressions are prime:
       (6*r - 1), (6*r + 5), (12*r - 7).

    Time Complexity: O(R * Primality) where R ~ 70,000 (executes in ~0.02s).
    Space Complexity: O(1) constant auxiliary space.
    """
    # Tile 1 has PD(1) = 3 (neighbors 2, 3, 4, 5, 6, 7 produce differences 1, 2, 3, 4, 5, 6 -> 3 primes: 2, 3, 5)
    count = 1
    if target == 1:
        return 1

    r = 1
    while True:
        # Candidate 1: Top tile of ring r: S_r = 3*r^2 - 3*r + 2
        if (
            is_prime(6 * r - 1)
            and is_prime(6 * r + 1)
            and is_prime(12 * r + 5)
        ):
            count += 1
            if count == target:
                return 3 * r * r - 3 * r + 2

        # Candidate 2: End tile of ring r: E_r = 3*r^2 + 3*r + 1 (for r > 1)
        if r > 1:
            if (
                is_prime(6 * r - 1)
                and is_prime(6 * r + 5)
                and is_prime(12 * r - 7)
            ):
                count += 1
                if count == target:
                    return 3 * r * r + 3 * r + 1

        r += 1


if __name__ == "__main__":
    print(solve())
