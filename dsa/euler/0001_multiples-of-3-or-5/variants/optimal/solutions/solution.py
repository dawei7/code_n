def solve(n: int = 1000) -> int:
    """Compute the sum of all natural multiples of 3 or 5 strictly below n.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Arithmetic Progressions & Gauss' Formula:
       The multiples of an integer m below n form an arithmetic progression:
           A_m = {m, 2m, 3m, ..., p_m * m}
       where p_m = (n - 1) // m is the number of terms.
       The sum of these multiples is given by:
           sigma(m, n) = m * (1 + 2 + ... + p_m) = m * p_m * (p_m + 1) // 2

    2. Principle of Inclusion-Exclusion (PIE):
       To compute the sum of numbers divisible by 3 OR 5 without double-counting
       numbers divisible by both (multiples of lcm(3, 5) = 15):
           S(n) = sigma(3, n) + sigma(5, n) - sigma(15, n)

    Complexity:
    -----------
    - Time Complexity: O(1) constant-time arithmetic evaluation.
    - Space Complexity: O(1) constant auxiliary space.
    """

    def sum_multiples(m: int, limit: int) -> int:
        """Calculate sum of multiples of m strictly below limit."""
        p = (limit - 1) // m
        return m * p * (p + 1) // 2

    # Compute partial sums dynamically via inclusion-exclusion
    multipliers = [(3, 1), (5, 1), (15, -1)]
    total_sum = 0
    for factor, sign in multipliers:
        total_sum += sign * sum_multiples(factor, n)

    return total_sum


if __name__ == "__main__":
    print(solve())
