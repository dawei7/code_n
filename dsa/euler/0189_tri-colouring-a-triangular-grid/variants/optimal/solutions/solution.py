import itertools


def solve(n: int = 8) -> int:
    """Find number of valid 3-colorings of a size n triangular grid.
    
    Time Complexity: O(n * 3^(2n+1))
    Space Complexity: O(3^n)
    """
    # dp[tuple of length r] = count of valid colorings for top r rows
    dp = {(c,): 1 for c in range(3)}

    for r in range(1, n):
        next_dp = {}
        v_tuples = list(itertools.product(range(3), repeat=r + 1))

        for U, count in dp.items():
            for V in v_tuples:
                ways = 1
                for i in range(r):
                    forbidden = {U[i], V[i], V[i + 1]}
                    choices = 3 - len(forbidden)
                    if choices <= 0:
                        ways = 0
                        break
                    ways *= choices
                if ways > 0:
                    next_dp[V] = next_dp.get(V, 0) + count * ways
        dp = next_dp

    return sum(dp.values())
