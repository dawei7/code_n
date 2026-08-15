def solve(limit: int = 1000) -> int:
    """Find the divisor d < limit for which 1/d contains the longest recurring decimal cycle.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Multiplicative Order & Recurring Decimal Period:
       For any integer d coprime to 10, the recurring cycle length of 1/d equals the
       multiplicative order of 10 modulo d:
           ord_d(10) = min { k >= 1 | 10^k = 1 mod d }

    2. Upper Bound on Cycle Length (Fermat's Little Theorem):
       By Euler's Totient Theorem, ord_d(10) <= phi(d) <= d - 1.
       The theoretical maximum period is d - 1, achieved when 10 is a primitive root mod d (Full Reptend Prime).

    3. Descending Search Space Pruning:
       Iterating d in descending order from limit - 1 down to 2:
       If d <= max_cycle_length, no subsequent d can achieve a longer cycle since ord_d(10) < d <= max_len.
       The search terminates immediately.

    Complexity:
    -----------
    - Time Complexity: O(limit^2) heavily pruned to ~50 steps (~0.001s).
    - Space Complexity: O(limit) remainder lookup dictionary.
    """

    def cycle_length(d: int) -> int:
        """Compute recurring cycle length of 1/d via long division remainder tracking."""
        seen = {}
        rem = 1
        pos = 0
        while rem != 0:
            if rem in seen:
                return pos - seen[rem]
            seen[rem] = pos
            rem = (rem * 10) % d
            pos += 1
        return 0

    max_len = 0
    best_d = 0

    # Search in descending order with early termination bound
    for d in range(limit - 1, 1, -1):
        if d <= max_len:
            break

        length = cycle_length(d)
        if length > max_len:
            max_len = length
            best_d = d

    return best_d


if __name__ == "__main__":
    print(solve())
