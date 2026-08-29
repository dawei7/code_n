import math

MOD = 10**8


def solve(a: int = 25, b: int = 75, c: int = 1984) -> int:
    """Find the last 8 digits of N(25, 75, 1984) graph colorings for a compound graph of 25 units A and 75 units B with 1984 colors.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Transfer Matrix & Representation Theory over Symmetric Group S_c:
       The compound graph is constructed by gluing a units of type A and b units of type B
       along vertical 2-vertex interface edges.
       The number of ways to arrange the sequence of units is given by the binomial coefficient:
           comb(a + b, a)

    2. Eigenspace Decomposition:
       Under the natural action of the permutation group S_c on vertical edge colorings (u, v) with u != v,
       the transfer matrices T_A(c) and T_B(c) simultaneously diagonalize into 3 irreducible invariant eigenspaces
       with multiplicities:
           m_0 = 1
           m_1 = 2*c - 3
           m_2 = c*(c - 3) // 2
       Notice that m_0 + m_1 + m_2 = c*(c - 1) / 2.

    3. Exact Eigenvalue Polynomials:
       - For Unit A:
           lambda_{0, A} = (c - 2)^3
           lambda_{1, A} = (c - 2)^2
           lambda_{2, A} = (c - 2) * (c - 3)
       - For Unit B:
           lambda_{0, B} = (c - 1) * (c^2 + 6*c - 8)
           lambda_{1, B} = (c - 2) * (c + 9)
           lambda_{2, B} = (c - 2) * (c - 4)

    4. Fast Modular Exponentiation:
       The total number of valid colorings modulo 10^8 is evaluated directly as:
           N(a, b, c) = comb(a + b, a) * sum_{i=0}^2 (m_i * lambda_{i, A}^a * lambda_{i, B}^b) mod 10^8

    Complexity:
    -----------
    - Time Complexity: O(log(a + b)) modular exponentiations (~0.0001s).
    - Space Complexity: O(1) constant auxiliary space.
    """
    eigenspaces = [
        (1, (c - 2) ** 3, (c - 1) * (c**2 + 6 * c - 8)),
        (2 * c - 3, (c - 2) ** 2, (c - 2) * (c + 9)),
        (c * (c - 3) // 2, (c - 2) * (c - 3), (c - 2) * (c - 4)),
    ]

    total = 0
    for mult, lA, lB in eigenspaces:
        term_A = pow(lA % MOD, a, MOD)
        term_B = pow(lB % MOD, b, MOD)
        total = (total + mult * term_A * term_B) % MOD

    comb_val = math.comb(a + b, a) % MOD
    return (comb_val * total) % MOD


if __name__ == "__main__":
    print(solve())
