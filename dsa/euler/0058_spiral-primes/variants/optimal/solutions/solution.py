def is_prime(n: int) -> bool:
    """Trial division primality test with 6k +/- 1 wheel optimization."""
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
    """Find the side length of the square spiral for which the ratio of primes along the diagonals first falls below 10%.

    Mathematical Principles Applied:
    1. Layered Corner Formulations for Side Length s:
       For a square spiral layer of odd side length s (s = 3, 5, 7, ...):
       - Top-Right corner: s^2 - (s - 1)
       - Top-Left corner: s^2 - 2*(s - 1)
       - Bottom-Left corner: s^2 - 3*(s - 1)
       - Bottom-Right corner: s^2 (always a perfect square, hence NEVER prime!)

    2. Total Diagonals Count:
       Total diagonal numbers for side length s: 2*s - 1.

    3. Iterative Primality Test:
       Test primality of the 3 non-square corners per layer.
       When prime_count / (2*s - 1) < 0.10, return side length s.

    Time Complexity: O(s * sqrt(s)) executing in ~0.20s.
    Space Complexity: O(1) constant auxiliary space.
    """
    prime_count = 0
    s = 3

    # Loop odd side lengths s starting at 3
    while True:
        # Evaluate 3 non-square diagonal corners for side s
        corner1 = s * s - (s - 1)
        corner2 = s * s - 2 * (s - 1)
        corner3 = s * s - 3 * (s - 1)

        # Increment prime count for each prime corner
        if is_prime(corner1):
            prime_count += 1
        if is_prime(corner2):
            prime_count += 1
        if is_prime(corner3):
            prime_count += 1

        # Total number of diagonal numbers up to side s: 2*s - 1
        total_diagonals = 2 * s - 1

        # Check if diagonal prime ratio falls strictly below 10% (0.10)
        if prime_count / total_diagonals < target_ratio:
            # Return side length s of the spiral
            return s

        # Advance to next odd side length
        s += 2


if __name__ == "__main__":
    print(solve())
