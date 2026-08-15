"""Project Euler Problem 555: McCarthy 91 Function.

Find S(10^6, 10^6), where S(p, m) = sum_{1 <= s < k <= p} SF(m, k, s),
and SF(m, k, s) is the sum of fixed points of the generalized McCarthy function M_{m, k, s}.
"""


def solve(p: int = 1_000_000, m: int = 1_000_000) -> int:
    """Compute S(p, m) in O(p) time using the fixed point interval theorem and exact Q-summation."""
    total = 0
    max_d = p // 2

    for d in range(1, max_d + 1):
        q = p // d - 1
        term = q * (d * m + d * (d + 1) // 2) - d * d * q * (q + 1) // 2
        total += term

    return total


if __name__ == "__main__":
    print(solve())
