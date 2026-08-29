"""Project Euler 335: Gathering the Beans

Find sum_{k=0}^{10^18} M(2^k + 1) mod 7^9, where M(x) is the number of moves
required to return to the initial 1-bean configuration in the circular Mancala game.
"""

from __future__ import annotations


def solve(limit_k: int = 1_000_000_000_000_000_000, mod: int = 40_353_607) -> str:
    """Calculates sum_{k=0}^{limit_k} M(2^k + 1) mod mod where mod = 7^9

    using the closed-form formula M(2^k + 1) = 2^{k+1} - 3^k + 4^k
    and closed-form geometric series summation.
    """
    n = limit_k

    # Bases and their coefficients in M(2^k + 1): 2 * 2^k - 1 * 3^k + 1 * 4^k
    terms = [(2, 2), (-1, 3), (1, 4)]
    total_sum = 0

    for coeff, base in terms:
        # Sum of base^k for k in 0..n is (base^{n + 1} - 1) / (base - 1)
        geom_sum = (
            (pow(base, n + 1, mod) - 1) * pow(base - 1, -1, mod)
        ) % mod
        total_sum = (total_sum + coeff * geom_sum) % mod

    return str(total_sum)


if __name__ == "__main__":
    print(solve())
