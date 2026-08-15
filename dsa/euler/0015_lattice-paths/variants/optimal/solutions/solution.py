import math


def solve(n: int = 20) -> int:
    """Compute the number of routes through an n x n grid moving only right and down.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Combinatorial Lattice Path Formulation:
       In an n x n grid, any valid path from the top-left vertex (0, 0) to the
       bottom-right vertex (n, n) moving only Right (R) and Down (D) consists of
       exactly n Right steps and n Down steps.
       The total length of every path is n + n = 2n steps.

    2. Central Binomial Coefficient:
       The total number of distinct paths is the number of ways to choose which n
       of the 2n total steps are Down steps (or Right steps):
           Paths(n) = binom(2n, n) = (2n)! / (n!)^2

    3. Multiplicative Evaluation:
       The binomial coefficient can be evaluated without factorials via:
           binom(2n, n) = prod_{k=1}^n [(n + k) // k]
       or using Python's math.comb(2 * n, n).

    Complexity:
    -----------
    - Time Complexity: O(n) exact arithmetic steps.
    - Space Complexity: O(1) constant auxiliary memory.
    """
    # Evaluate central binomial coefficient binom(2n, n) dynamically
    ans = 1
    for k in range(1, n + 1):
        ans = ans * (n + k) // k

    return ans


if __name__ == "__main__":
    print(solve())
