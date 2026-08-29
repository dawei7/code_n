"""Project Euler Problem 401: Sum of Squares of Divisors.

Find SIGMA_2(10^15) mod 10^9, where SIGMA_2(n) = sum_{i=1..n} sigma_2(i).
"""


def solve(n_val: int = 10**15, mod: int = 10**9) -> int:
    """Compute SIGMA_2(n_val) mod mod using hyperbola block summation."""

    def sum_sq(n: int) -> int:
        return (n * (n + 1) * (2 * n + 1) // 6) % mod

    total = 0
    l = 1
    while l <= n_val:
        q = n_val // l
        r = n_val // q

        sq_sum = (sum_sq(r) - sum_sq(l - 1)) % mod
        total = (total + (q % mod) * sq_sum) % mod

        l = r + 1

    return total


if __name__ == "__main__":
    print(solve())
