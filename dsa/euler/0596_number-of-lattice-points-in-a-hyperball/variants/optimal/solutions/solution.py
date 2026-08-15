"""Project Euler Problem 596: Number of Lattice Points in a Hyperball.

Find T(10^8) mod 1000000007, where T(r) is the number of lattice points
in the 4-dimensional hyperball x^2 + y^2 + z^2 + t^2 <= r^2.
"""

_MOD = 1000000007


def _sum_sigma(n_val: int) -> int:
    total = 0
    i = 1
    while i <= n_val:
        q = n_val // i
        j = n_val // q
        sum_d = ((i + j) * (j - i + 1) // 2) % _MOD
        total = (total + (q % _MOD) * sum_d) % _MOD
        i = j + 1
    return total


def solve(r: int = 10**8) -> int:
    """Compute T(r) modulo 1000000007 using Jacobi's four-square theorem and Dirichlet hyperbola divisor sums."""
    n_val = r * r
    results = [_sum_sigma(m) for m in (n_val, n_val // 4)]
    s1, s4 = results[0], results[1]
    return (1 + 8 * (s1 - 4 * s4)) % _MOD


if __name__ == "__main__":
    print(solve())
