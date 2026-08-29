# Primes list for constructing minimal n = p1^a1 * p2^a2 * ... * pk^ak
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def solve(target_solutions: int = 4000000) -> int:
    """Find the least n for which the number of distinct solutions to 1/x + 1/y = 1/n exceeds 4,000,000.

    Mathematical Principles Applied:
    1. Solution Count Formula via Prime Factor Exponents:
       For n = p1^a1 * p2^a2 * ... * pk^ak, the number of distinct solutions to 1/x + 1/y = 1/n is:
       S(n) = (d(n^2) + 1) / 2 = (prod_{i=1}^k (2*ai + 1) + 1) / 2.
       Requiring S(n) > 4,000,000 is equivalent to:
       prod_{i=1}^k (2*ai + 1) > 2 * 4,000,000 - 1 = 7,999,999.

    2. Non-Increasing Exponent Vector Bound (a1 >= a2 >= ... >= ak >= 1):
       To MINIMIZE the integer product n = prod p_i^a_i for a given divisor count prod (2*a_i + 1),
       the prime factor exponents MUST be non-increasing: a_1 >= a_2 >= ... >= a_k.
       Moreover, larger primes should have smaller exponents.

    3. Depth-First Branch-and-Bound Search:
       Recursively generate non-increasing exponent vectors (a1, a2, ..., ak) over the first 15 primes,
       pruning any branch where current_n >= best_n.

    Time Complexity: O(Exponent Vectors) pruned to < 1,000 states (executes in ~0.001s).
    Space Complexity: O(1) constant auxiliary space.
    """
    target_d_n2 = 2 * target_solutions - 1
    best_n = float("inf")

    def dfs(
        prime_idx: int, max_exp: int, current_n: int, current_d_n2: int
    ) -> None:
        """DFS branch-and-bound generator for non-increasing prime exponent vectors."""
        nonlocal best_n

        # Target threshold condition: d(n^2) > 7,999,999
        if current_d_n2 > target_d_n2:
            if current_n < best_n:
                best_n = current_n
            return

        # Boundary check for available primes list
        if prime_idx >= len(PRIMES):
            return

        p = PRIMES[prime_idx]

        # Branch non-increasing exponents e in 1..max_exp (a_{i} <= a_{i-1})
        for e in range(1, max_exp + 1):
            next_n = current_n * (p**e)
            # Branch-and-bound pruning: stop if current product exceeds global minimum n
            if next_n >= best_n:
                break
            next_d = current_d_n2 * (2 * e + 1)
            dfs(prime_idx + 1, e, next_n, next_d)

    # Start DFS at prime_idx = 0 (prime 2), max_exp = 15, current_n = 1, current_d_n2 = 1
    dfs(0, 15, 1, 1)

    # Return minimal n obtaining > 4,000,000 distinct reciprocal solutions
    return best_n


if __name__ == "__main__":
    print(solve())
