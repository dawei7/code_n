"""Project Euler Problem 503: Compromise or Persist.

Find F(10^6), the expected score under the optimal stopping strategy,
rounded to 10 decimal places.
"""


def solve(n: int = 10**6) -> str:
    """Compute F(n) using optimal stopping backward induction on order statistics."""
    expected_score = (n + 1) / 2.0

    for k in range(n - 1, 0, -1):
        scale = (n + 1) / (k + 1)
        j_star = int(expected_score / scale)
        if j_star > k:
            j_star = k

        sum_val = (
            scale * (j_star * (j_star + 1) / 2.0)
            + (k - j_star) * expected_score
        )
        expected_score = sum_val / k

    return f"{expected_score:.10f}"


if __name__ == "__main__":
    print(solve())
