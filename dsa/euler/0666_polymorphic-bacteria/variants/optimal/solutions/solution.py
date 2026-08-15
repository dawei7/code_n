"""Project Euler Problem 666: Polymorphic Bacteria.

Find P(500, 10) rounded to 8 decimal places, where P(k, m) is the probability that a population
of bacteria species S_{k,m} starting with a single bacterium of type alpha_0 eventually dies out.
"""

from typing import List


def _generate_r(total: int) -> List[int]:
    r = [0] * total
    r[0] = 306
    for n in range(1, total):
        r[n] = (r[n - 1] * r[n - 1]) % 10007
    return r


def solve(k: int = 500, m: int = 10, eps: float = 1e-13) -> str:
    """Compute P(k, m) using multi-type Galton-Watson branching process fixed-point iteration."""
    r = _generate_r(k * m)
    x = [0.0] * k

    while True:
        nxt = [0.0] * k
        for i in range(k):
            s = 0.0
            row_offset = i * m
            for j in range(m):
                q = r[row_offset + j] % 5
                if q == 0:
                    s += 1.0
                elif q == 1:
                    s += x[i] * x[i]
                elif q == 2:
                    s += x[(2 * i) % k]
                elif q == 3:
                    target = (i * i + 1) % k
                    s += x[target] ** 3
                elif q == 4:
                    s += x[i] * x[(i + 1) % k]
            nxt[i] = s / m

        max_diff = max(abs(nxt[i] - x[i]) for i in range(k))
        x = nxt
        if max_diff < eps:
            break

    return f"{x[0]:.8f}"


if __name__ == "__main__":
    print(solve())
