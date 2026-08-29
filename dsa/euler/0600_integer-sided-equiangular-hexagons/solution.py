"""Project Euler Problem 600: Integer Sided Equiangular Hexagons.

Find H(55106), where H(n) is the number of distinct integer sided equiangular
convex hexagons with perimeter <= n up to congruence.
"""


def solve(n: int = 55106) -> int:
    """Compute H(n) using the partition generating function 1 / ((1-x)(1-x^2)(1-x^3)(1-x^4)(1-x^6))."""
    m = n - 6
    if m < 0:
        return 0

    coins = (1, 2, 3, 4, 6)
    dp = [0] * (m + 1)
    dp[0] = 1
    for c in coins:
        for i in range(c, m + 1):
            dp[i] += dp[i - c]
    return dp[m]


if __name__ == "__main__":
    print(solve())
